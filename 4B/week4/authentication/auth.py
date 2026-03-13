from fastapi import Request, Depends, HTTPException
from sqlalchemy.orm import Session

from database.models import get_db
from .phone_verification import authenticate_phone_user
from .session_manager import generate_session, validate_session


async def verify_whatsapp_request(request: Request, db: Session = Depends(get_db)):
    """
    FastAPI dependency/helper to authenticate incoming WhatsApp webhook requests.

    Returns:
        {
            "user": User,
            "conversation": Conversation,
            "session": SessionState,
            "message_text": str,
            "phone_number": str,
            "profile_name": str | None
        }

    If the payload contains no user message (e.g. read receipts), returns:
        {"status": "ignored"}
    """
    # Parse JSON payload
    try:
        payload = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid JSON payload")

    # Extract phone number, profile name, and message text from WhatsApp Cloud payload
    try:
        entry = payload.get("entry", [{}])[0]
        changes = entry.get("changes", [{}])[0]
        value = changes.get("value", {})
        messages = value.get("messages", [])

        # Ignore non-message events
        if not messages:
            return {"status": "ignored"}

        message = messages[0]
        phone_number = message.get("from")
        if not phone_number:
            raise HTTPException(status_code=400, detail="Missing sender phone number")

        contacts = value.get("contacts", [])
        profile_name = None
        if contacts:
            profile_name = contacts[0].get("profile", {}).get("name")

        # Cloud API represents text as {"body": "..."}
        message_text = (
            message.get("text", {}).get("body")
            if isinstance(message.get("text"), dict)
            else None
        )

        if not message_text or not message_text.strip():
            # No meaningful text to process
            return {"status": "ignored"}

    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(
            status_code=400,
            detail=f"Malformed WhatsApp payload: {exc}",
        )

    # Authenticate user + conversation
    try:
        user, conversation = authenticate_phone_user(
            db=db,
            phone_number=phone_number,
            name=profile_name,
        )
    except Exception as exc:
        raise HTTPException(
            status_code=401,
            detail=f"User authentication failed: {exc}",
        )

    # Session handling:
    # If caller sends X-Session-Token and it is valid, reuse it.
    # Otherwise create a new session.
    session_token = request.headers.get("X-Session-Token")
    session = (
        validate_session(db=db, session_token=session_token)
        if session_token
        else None
    )

    if not session or str(session.user_id) != str(user.id):
        session = generate_session(db=db, user_id=user.id)

    return {
        "user": user,
        "conversation": conversation,
        "session": session,
        "message_text": message_text.strip(),
        "phone_number": phone_number,
        "profile_name": profile_name,
    }
