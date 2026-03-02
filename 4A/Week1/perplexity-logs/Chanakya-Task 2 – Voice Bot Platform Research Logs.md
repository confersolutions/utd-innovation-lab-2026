\# Task 2 – Voice Bot Platform Evaluation  
Research Logs (Process Documentation)

\---

\#\# Research Session 1 – Understanding Real-Time Voice AI

\*\*Initial Queries:\*\*  
\- best real-time voice ai agents 2026  
\- what is real time ai voice  
\- how does latency work in conversational ai  
\- stt llm tts pipeline explanation  
\- what is acceptable latency for ai voice

\*\*What I Was Trying to Understand:\*\*  
\- What “real-time” technically means.  
\- Whether latency is a single metric or multiple components.  
\- What delay feels natural in a live support call.

\*\*What I Learned:\*\*  
\- Real-time voice \= streaming STT → LLM → TTS pipeline.  
\- Latency is cumulative (speech recognition \+ reasoning \+ synthesis \+ telephony).  
\- Sub-2 second response is ideal for natural interaction.

\*\*What Confused Me:\*\*  
\- Vendors use “real-time” without consistent benchmarks.  
\- No standardized latency disclosure across platforms.

\*\*Dead End:\*\*  
\- Many tools marketed as “voice AI” were only TTS engines.

\*\*Refinement:\*\*  
\- Separate voice engines from full conversational voice agents.

\---

\#\# Research Session 2 – Customer Support Readiness

\*\*Initial Queries:\*\*  
\- which voice ai platforms can handle customer support  
\- inbound ai receptionist comparison  
\- voice ai interruption handling barge-in  
\- retell vs polyai vs cognigy

\*\*What I Was Trying to Understand:\*\*  
\- Which platforms can handle real inbound support.  
\- Difference between outbound automation vs structured support systems.

\*\*What I Learned:\*\*  
\- Outbound platforms ≠ customer support systems.  
\- Support requires escalation logic and multi-turn reliability.

\*\*What Confused Me:\*\*  
\- Hard to assess production readiness from marketing pages.  
\- Case studies lacked technical breakdown.

\*\*Dead End:\*\*  
\- Over-prioritizing voice realism instead of workflow capability.

\*\*Refinement:\*\*  
\- Shifted focus to webhook capability \+ escalation \+ CRM integration.

\---

\#\# Research Session 3 – Webhooks & Integration Capability

\*\*Initial Queries:\*\*  
\- voice ai webhook api support  
\- tool calling in voice agents  
\- crm integration voice ai  
\- twilio sip integration ai voice

\*\*What I Was Trying to Understand:\*\*  
\- How voice connects to CRM and WhatsApp.  
\- Whether structured action triggers are supported.

\*\*What I Learned:\*\*  
\- Webhooks are essential for structured flows (registrations, confirmations).  
\- Tool-calling enables CRM logging and follow-up automation.  
\- Telephony integration varies significantly.

\*\*What Confused Me:\*\*  
\- API claims often lacked detailed payload examples.  
\- Hard to verify webhook reliability in real-time flows.

\*\*Dead End:\*\*  
\- Reviewing generic API pages without practical flow testing.

\*\*Refinement:\*\*  
\- Evaluate platforms using structured test scenarios (name capture, language switch, interruption handling).

\---

\#\# Research Session 4 – Multilingual Capability

\*\*Initial Queries:\*\*  
\- multilingual voice ai hindi support  
\- elevenlabs hindi support  
\- retell ai multilingual  
\- language switching voice ai

\*\*What I Was Trying to Understand:\*\*  
\- Whether Hindi support was conversational or just TTS.  
\- Whether language switching works mid-conversation.

\*\*What I Learned:\*\*  
\- Some platforms support Hindi TTS but weak Hindi comprehension.  
\- Language switching can break conversation context.

\*\*What Confused Me:\*\*  
\- Marketing lists do not differentiate STT vs TTS vs LLM language fluency.

\*\*Dead End:\*\*  
\- Assuming language lists imply conversational reliability.

\*\*Refinement:\*\*  
\- Added multilingual stress testing to evaluation framework.

\---

\#\# Research Session 5 – Pricing Model Comparison

\*\*Initial Queries:\*\*  
\- voice ai pricing per minute vs character based  
\- elevenlabs character pricing conversion  
\- blended cost voice ai stack  
\- how to estimate cost at 1k 10k 100k users

\*\*What I Was Trying to Understand:\*\*  
\- How to fairly compare pricing models.  
\- How to scale cost projections logically.

\*\*What I Learned:\*\*  
\- Pricing models vary: per-minute, character-based, modular, enterprise contracts.  
\- Modular stacks create blended hidden costs (STT \+ TTS \+ LLM \+ telephony).

\*\*What Confused Me:\*\*  
\- Enterprise vendors do not publish rates.  
\- Exact scaling requires usage assumptions.

\*\*Dead End:\*\*  
\- Trying to standardize all vendors into one pricing metric.

\*\*Refinement:\*\*  
\- Document pricing model type \+ modeling assumptions instead of exact equivalency.

\---

\#\# Research Session 6 – Architecture & Orchestration Impact

\*\*Initial Queries:\*\*  
\- voice agent architecture with orchestration layer  
\- n8n vs make integration voice  
\- voice to whatsapp automation  
\- session management voice bot

\*\*What I Was Trying to Understand:\*\*  
\- How voice integrates with WhatsApp and web flows.  
\- Where session state should live.  
\- Shared backend vs separate bot instances.

\*\*What I Learned:\*\*  
\- Orchestration layer is critical for multi-channel deployment.  
\- Voice must trigger WhatsApp confirmations and CRM updates.  
\- Session strategy impacts continuity across channels.

\*\*What Confused Me:\*\*  
\- Whether session state should live inside the voice platform or external database.  
\- User identity consistency across channels.

\*\*Dead End:\*\*  
\- Treating voice as an isolated channel initially.

\*\*Refinement:\*\*  
\- Evaluate platforms based on integration primitives and architecture compatibility.

\---

End of Task 2 Research Logs  
