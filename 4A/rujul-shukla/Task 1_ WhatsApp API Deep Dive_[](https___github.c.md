<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Task 1: WhatsApp API Deep Dive

[](https://github.com/confersolutions/utd-innovation-lab-2026/blob/main/4A/README.md#task-1-whatsapp-api-deep-dive)
Compare the following platforms:
Meta Business Platform (direct API)
Twilio
MessageBird
Find 2 NEW providers (not listed above) — research emerging WhatsApp API providers
Deliverable: whatsapp-api-comparison.md
Include: pricing models, rate limits, India vs US support, conversation-based vs session-based pricing, webhook capabilities, ease of integration

Here is a concise comparison you can adapt into `whatsapp-api-comparison.md` for your repo.

## Platforms Compared

- Meta WhatsApp Business Platform (Cloud API – direct)
- Twilio
- MessageBird
- Vonage (new)
- 360dialog (new)


### High‑level summary

| Provider | Pricing model on top of Meta | Main billing unit now | Typical extra fee level | India \& US support | Webhooks \& integration ease |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Meta Cloud API (direct) | No markup by Meta itself; infra cost is on you [^1_1] | Per‑message (template) from Jul 2025 [^1_2][^1_1] | 0, but you must host your own services | Global, including India \& US [^1_3][^1_4] | Native webhooks, REST/Graph API, highest flexibility but more DevOps [^1_3][^1_4][^1_5] |
| Twilio | Per‑message markup of 0.005 USD on every in/out message, on top of Meta rates [^1_6][^1_7] | Per‑message, mapped internally to Meta’s per‑message charges [^1_6][^1_7] | Medium–high; every message gets a flat uplift [^1_6][^1_7] | Global, strong India + US coverage [^1_6][^1_7] | Mature webhooks and SDKs, relatively easy integration [^1_8] |
| MessageBird | Meta fees + BSP/platform markup (not fully public, varies by plan) [^1_1][^1_9] | Per‑message (follows Meta), conversation tiers still reflected in rate‑limit tiers [^1_1][^1_9] | Medium; common BSP‑style markup [^1_1] | Global, including India \& US [^1_9] | Webhook‑driven, REST API, good docs; slightly more setup than Twilio [^1_9] |
| Vonage | Meta per‑message fee + Vonage per‑message platform fee [^1_10][^1_11] | Per‑message for both Meta and Vonage components [^1_10][^1_11] | Low–medium; tiers and small per‑message platform fee [^1_10][^1_11] | Global, strong US and India support [^1_10][^1_11] | Unified Messages API, webhooks, decent tooling [^1_11] |
| 360dialog | Flat monthly license per number (≈ 50 USD) + Meta rates; no per‑message markup [^1_12] | Per‑message (Meta) but your BSP cost is flat subscription [^1_12] | Low at scale; predictable flat fee [^1_12] | Global, widely used in India \& US via partners [^1_12] | Direct Meta Cloud API access, sandbox, clean docs [^1_12] |


***

## Pricing models

### Meta WhatsApp Business Platform (direct)

- Meta changed from conversation‑based to **per‑message** billing for template messages on Jul 1, 2025.[^1_2][^1_1]
- You pay Meta’s official country‑ and category‑based rates (Marketing, Utility, Authentication) with no extra markup from Meta itself.[^1_1][^1_2]
- Example India Meta rates: marketing templates around ₹0.88, utility and authentication around ₹0.125 per message.[^1_2]


### Twilio

- Twilio keeps a **per‑message** model and simply passes Meta’s fee plus a flat markup of **0.005 USD per message**, applied to both outgoing and incoming traffic.[^1_6][^1_7]
- So if Meta charges 0.035 USD for a US marketing message, total becomes about 0.04 USD via Twilio.[^1_6]
- They emphasize pay‑as‑you‑go; there is no large mandatory monthly commitment, but at volume the markup adds up.[^1_7][^1_6]


### MessageBird

- MessageBird follows Meta’s pricing and adds its own BSP/platform fee, often via subscription plus per‑message markup (exact public tables are sparse).[^1_1]
- Like other BSPs, typical markup bands fall in the 0.005–0.02 USD per conversation or equivalent per‑message range, depending on contract.[^1_1]
- Higher tiers (Enterprise) get negotiated pricing but still layered on top of Meta’s base fees.[^1_1]


### Vonage (new)

- Vonage now uses **per‑message pricing** for WhatsApp to align with Meta’s 2025 change.[^1_10][^1_11]
- Total price = WhatsApp fee (Meta) + Vonage platform fee, both charged per message, with platform fee as low as 0.00015 USD in some tiers.[^1_10]
- Meta fees themselves are tiered; over certain per‑message volume thresholds, you get incremental discounts for that message type and region.[^1_10]


### 360dialog (new)

- 360dialog charges a **flat monthly license** per phone number, starting around 50 USD, with **no per‑message markup** on Meta fees.[^1_12]
- You pay Meta at list price and a predictable subscription to 360dialog, which is attractive at medium–high volume because your BSP cost does not scale with messages.[^1_12]

***

## Rate limits

### Meta Cloud API (all BSPs ultimately inherit these)

- Meta controls **conversation initiation tiers**: new numbers often start at 250 business‑initiated conversations per 24 hours, then can scale to 2,000, 10,000, 100,000 and potentially unlimited based on quality score.[^1_4][^1_1]
- Technical throughput: Cloud API starts at about **80 messages per second per phone number**, with automatic upgrades up to 1,000 mps for high‑tier, high‑quality senders.[^1_5][^1_13]


### Twilio

- Twilio itself does not expose a separate WhatsApp‑specific hard cap; instead, you are bound by Meta’s per‑day conversation and mps limits, plus Twilio’s general API safety limits.[^1_8][^1_4]
- Good practice is to throttle sends in your app to remain under Meta’s 80 mps default and respect tier‑based daily conversation caps.[^1_4][^1_5]


### MessageBird

- MessageBird surfaces Meta‑style **tiered rate limits** where Tier 1 numbers can send to about 1,000 customers/day, Tier 2 to about 10,000, and higher tiers as Meta upgrades.[^1_9]
- Under the hood, they are using the same Meta throughput rules (80–1,000 mps) and apply internal safety throttling.[^1_9][^1_4]


### Vonage

- Vonage is similarly constrained by Meta: daily business‑initiated conversation caps and 80 mps default throughput, with upgrade to higher throughput for qualifying accounts.[^1_11][^1_5]
- Their messages API handles retry and queuing, but they recommend obeying Meta’s limits to avoid errors.[^1_11][^1_5]


### 360dialog

- 360dialog connects you directly to Meta’s Cloud API, so rate limits are effectively **Meta’s own**: 80 mps default, up to 1,000 mps on upgrade, and conversation tiers scaling with quality.[^1_13][^1_5][^1_12]
- At scale, you design your own throttling and back‑off logic using Meta’s limits and error codes.[^1_5][^1_13]

***

## India vs US support

- **Meta direct**: Supports WhatsApp Business messaging globally; India and US are both fully covered with region‑specific per‑message pricing.[^1_3][^1_2][^1_1]
- **Twilio**: Offers WhatsApp in both India and US; pricing differs by recipient country because Meta’s underlying rates differ.[^1_7][^1_6]
- **MessageBird**: Global BSP with official support for India and US numbers; pricing tables reflect Meta’s country‑specific fees plus BSP markup.[^1_9][^1_1]
- **Vonage**: Provides WhatsApp messaging for US and India, with per‑message Meta+Vonage pricing per country and category.[^1_11][^1_10]
- **360dialog**: Works globally, widely adopted in India and US through partners and direct onboarding; you still pay Meta’s regional prices.[^1_12][^1_1]

***

## Conversation‑ vs session‑based pricing

The underlying Meta model has moved, but you may still see older terminology.

- Historically, WhatsApp charged **per conversation**: one paid template opened a 24‑hour window with free session messages.[^1_14][^1_1]
- Since July 2025, Meta charges **per template message** sent, so most providers are effectively **per‑message** now, although the 24‑hour service window for customer‑initiated traffic still matters for when certain messages are free.[^1_2][^1_1]

By provider:

- **Meta direct**: Per‑message billing for template messages, with 24‑hour customer‑care windows where service replies and many utility templates can be free; not sold as “conversations” anymore.[^1_2][^1_1]
- **Twilio**: Positions pricing as per‑message and explicitly adds 0.005 USD on top of each Meta‑billed message, regardless of whether the conversation is business‑initiated or service.[^1_6][^1_7]
- **MessageBird**: Adopts Meta’s current per‑message model but often explains plans in terms of monthly conversation volume and tiers for marketing vs service templates.[^1_1]
- **Vonage**: Now explicitly labels its pricing as **per‑message**, replacing its earlier conversation‑based approach.[^1_11]
- **360dialog**: Your cost to 360dialog is not per message, but Meta still bills per message; from your perspective: flat subscription (BSP) + per‑message Meta.[^1_12][^1_1]

***

## Webhook capabilities

### Meta WhatsApp Business Platform (direct)

- Uses the Facebook Graph Webhooks system; you register a callback URL and verify a token.[^1_3]
- Webhooks deliver message events, status updates, and template notifications in near real time.[^1_3]


### Twilio

- Twilio exposes incoming message and status callbacks via regular HTTPS webhooks that you configure per WhatsApp number or messaging service.[^1_8]
- You can handle delivery receipts, read status, and incoming messages with simple webhook endpoints, with language‑specific helper libraries.[^1_8]


### MessageBird

- MessageBird uses webhooks to push incoming messages and status events to your backend; you configure them in the dashboard.[^1_9]
- Their API lets you manage channels (including WhatsApp) and receive all message events through a unified webhook format.[^1_9]


### Vonage

- Vonage’s Messages API requires inbound and status webhooks for WhatsApp; you provide URLs for receiving messages and delivery receipts.[^1_11]
- All channels (SMS, WhatsApp, etc.) share the same webhook pattern, simplifying integration.[^1_11]


### 360dialog

- 360dialog exposes webhooks directly from Meta’s Cloud API: you set your webhook URL, verify a token, and receive message/status events.[^1_12]
- Because it is close to “pure” Cloud API, payloads and behavior closely track Meta’s docs.[^1_3][^1_12]

***

## Ease of integration

### Meta direct

- Requires you to work with the Facebook Graph API, host your own middleware, manage auth tokens, handle scaling, and build tooling.[^1_5][^1_3]
- Very flexible and lowest raw cost, but highest engineering and DevOps burden.[^1_3][^1_1]


### Twilio

- Offers strong language SDKs, good documentation, test credentials, and a unified messaging model (SMS + WhatsApp) through the same APIs.[^1_8]
- Typically the **easiest** path if you already use Twilio; you trade simplicity for the per‑message markup.[^1_6][^1_8]


### MessageBird

- Provides REST APIs, a dashboard, and additional tools like flows and inbox; onboarding is straightforward but slightly more opinionated than Twilio.[^1_1][^1_9]
- Integration effort is moderate; good fit for omnichannel setups using their broader CPaaS stack.[^1_9][^1_1]


### Vonage

- Uses a unified Messages API for WhatsApp, SMS, etc., which simplifies multi‑channel implementations.[^1_11]
- Webhooks and API patterns are consistent; integration is comparable to Twilio in complexity, with fewer SDK ecosystems but clear docs.[^1_11]


### 360dialog

- Designed for developers: you get direct access to Meta Cloud API with added onboarding and tools, plus a sandbox for testing.[^1_12]
- Documentation is concise and you avoid high‑level abstractions; ideal if you want Meta‑native behavior without building your own BSP layer.[^1_1][^1_12]

***

## How you might position them in your `.md`

If you want to keep `whatsapp-api-comparison.md` tight, you can:

- Use one overview table (like the first one) plus a short subsection per category (pricing, rate limits, geography, webhooks, integration).[^1_7][^1_4][^1_10][^1_5][^1_2][^1_6][^1_8][^1_3][^1_12][^1_9][^1_1][^1_11]
- Call out trade‑offs explicitly (e.g., Meta/360dialog = cheapest but more engineering, Twilio/Vonage = easier but ongoing per‑message markup).[^1_10][^1_6][^1_12][^1_11]

You can copy‑paste and adapt the tables and bullet points above directly into your repo file.
<span style="display:none">[^1_15][^1_16][^1_17][^1_18]</span>

<div align="center">⁂</div>

[^1_1]: https://waslo.io/blog/whatsapp-business-api-pricing-guide

[^1_2]: https://www.matrixhive.com/blog/whatsapp-business-api-pricing-in-india-the-real-numbers-december-2025

[^1_3]: https://developers.facebook.com/documentation/business-messaging/whatsapp/about-the-platform

[^1_4]: https://www.wati.io/en/blog/whatsapp-business-api/whatsapp-api-rate-limits/

[^1_5]: https://www.wuseller.com/whatsapp-business-knowledge-hub/scale-whatsapp-cloud-api-master-throughput-limits-upgrades-2026

[^1_6]: https://www.spurnow.com/en/blogs/whatsapp-business-api-pricing-explained

[^1_7]: https://respond.io/blog/whatsapp-business-api-pricing

[^1_8]: https://www.twilio.com/docs/whatsapp/api

[^1_9]: https://developers.messagebird.com/docs/whatsapp/number-quality-ratings/

[^1_10]: https://api.support.vonage.com/hc/en-us/articles/19800233069084-WhatsApp-Pricing

[^1_11]: https://developer.vonage.com/en/messages/concepts/whatsapp

[^1_12]: https://decisiontele.com/news/best-whatsapp-api-provider.html

[^1_13]: https://learn.doubletick.io/troubleshoot-errors/understanding-whatsapp-error-code-131056-pair-rate-limit

[^1_14]: https://elfsight.com/blog/whatsapp-business-api-overview/

[^1_15]: https://chatmitra.com/pricing/

[^1_16]: https://www.twilio.com/docs/verify/api/programmable-rate-limits

[^1_17]: https://www.twilio.com/docs/verify/api/service-rate-limits

[^1_18]: https://www.twilio.com/docs/verify/api/rate-limits-and-timeouts


---

# explain the current whatsapp business api

The current WhatsApp Business API (now officially called the **WhatsApp Business Platform / Cloud API**) is a server‑side API for mid‑to‑large businesses to integrate WhatsApp into their own systems rather than using the phone apps. It’s built for automation, multi‑agent support, and deep integration with CRMs, e‑commerce, and internal tools.[^2_2][^2_3]

## Core concepts

- **Who it’s for**: Designed for businesses that need multi‑agent access, automation, broadcasts, and integrations (CRM, e‑commerce, support tools), not for individuals or very small merchants who can live on the WhatsApp Business app.[^2_3]
- **How you access it**:
    - Either directly via Meta’s Cloud API (through Meta Business Manager), or
    - Indirectly via a Business Solution Provider (BSP) platform built on top of the API.[^2_2][^2_3]
- **Requirements**: Verified Meta Business Manager, a dedicated phone number (not simultaneously used in the regular app), and mandatory two‑factor authentication for the business account.[^2_2]


## Key capabilities vs the app

Compared with the free WhatsApp Business app, the API gives you:

- **Multi‑agent, multi‑device support**: Many agents can respond from one number through a shared inbox on a platform, instead of being limited to a handful of logged‑in devices.[^2_3]
- **Automation \& chatbots**: Keyword auto‑replies, routing bots, FAQ flows, and integration with custom or third‑party chatbots.[^2_3][^2_2]
- **Rich interactive elements**:
    - Reply buttons and list messages for guided choices.
    - **WhatsApp Flows** – embedded forms and mini‑flows in chat for bookings, surveys, and lead qualification.[^2_2]
- **Broadcasts and marketing**: Official, high‑volume, compliant broadcasts (templates) with segmentation, scheduling, and analytics, which are not possible safely with the regular app without risking bans.[^2_3][^2_2]
- **Green‑tick verification and branded profiles**: Possibility of an “official business account” badge plus richer business profile, which increases customer trust.[^2_3]


## Technical model (Cloud API)

At a technical level, the current platform works like this:

- **REST API**: You send and receive messages via HTTPS endpoints hosted by Meta (Cloud API) or by your BSP.[^2_2]
- **Webhooks**: Incoming messages, delivery/read receipts, and status changes are pushed to your backend via webhooks you configure.[^2_2]
- **Templates vs session messages**:
    - Pre‑approved **message templates** for outbound notifications (marketing, utility, authentication).
    - Free‑form **session messages** within a 24‑hour window after a user message, mainly for support.[^2_6][^2_2]
- **IDs \& upcoming usernames**: Meta is introducing **business‑scoped user IDs (BSUID)** and “usernames,” so businesses may increasingly work with an abstract user id instead of a raw phone number for privacy.[^2_4]


## Pricing and limits (2025–2026 model)

- **Pricing**:
    - Meta has moved from strictly “conversation‑based” pricing toward **per‑message pricing for templates**, with different rates by country and category (marketing, utility, authentication).[^2_6]
    - Customer‑initiated 24‑hour support windows often allow free‑form replies (no extra Meta fee) once opened.[^2_6]
- **Rate limits**:
    - Messaging is constrained by **daily messaging tiers** and throughput per number. As verification/quality improves, businesses can scale to large volumes (on the order of 100K+ daily messages in newer tiers).[^2_4]
    - Meta is rolling out **portfolio pacing**, which lets large campaigns send in batches and automatically pause/slow if there are negative feedback signals.[^2_4]


## 2026+ updates and direction

Recent and near‑term changes focus on scale, privacy, and advanced customer journeys:

- **Relaxed messaging tiers**: Old 2K/10K tiers are being replaced with higher default limits (e.g., 100K daily after verification), making it easier for verified businesses to scale.[^2_4]
- **Usernames \& BSUID**: Hiding phone numbers more often, encouraging businesses to store and use BSUID as the primary customer key in CRMs.[^2_4]
- **New engagement features**: Expanding interactive formats like coupons, countdown timers, and advanced promo tools to drive marketing performance.[^2_5][^2_2]
- **More automation \& analytics**: Ecosystem tools on top of the API increasingly add funnels, performance tracking (e.g., revenue attribution from WhatsApp), and deeper omnichannel analytics.[^2_3][^2_2]

If you tell me whether you care more about architecture, pricing, or what this means for your project (e.g., UTD lab work), I can zoom in on that slice and keep it very practical.
<span style="display:none">[^2_1][^2_7]</span>

<div align="center">⁂</div>

[^2_1]: https://www.reddit.com/r/whatsapp/comments/1q1pc4r/what_changes_do_you_expect_in_whatsapp_business/

[^2_2]: https://chatarmin.com/en/blog/whats-app-business-api-integration

[^2_3]: https://blog.omnichat.ai/whatsapp-business-vs-whatsapp-business-api/

[^2_4]: https://woztell.com/whatsapp-api-2026-updates-pacing-limits-usernames/

[^2_5]: https://mtalkz.com/meta-introduced-new-features-in-whatsapp-for-business/

[^2_6]: https://www.spurnow.com/en/blogs/whatsapp-business-api-pricing-explained

[^2_7]: https://www.activecampaign.com/blog/whatsapp-guide


---

# explain thsi in simpler terms

Think of the WhatsApp Business API as a way for a company to plug WhatsApp directly into its own software, instead of using the WhatsApp app on a phone.

## What it is

- It’s for **businesses that get lots of messages** and need many team members or bots to reply.
- It’s not an app you open; it’s a **backend API** your code or a platform (like Twilio, etc.) connects to.


## What you can do with it

- **Many agents, one number**: Your whole support or sales team can answer customers from the same WhatsApp number through a shared inbox or custom tool.
- **Bots and automation**: You can build chatbots, auto‑replies, and flows (like “press 1 for support, 2 for sales”) directly in WhatsApp.
- **Structured messages**: Buttons, lists, and small forms (for booking, surveys, checkout steps) so users tap instead of typing.
- **Broadcasts / campaigns**: Send approved promotional or update messages to many customers at once, in a compliant way.


## How the messaging works

- There are two basic message types:
    - **Templates**: Pre‑approved messages you use to start or continue conversations (e.g., “Your order has shipped” or a promo).
    - **Session messages**: Free‑form replies your agents send **within 24 hours** after a customer messages you.
- You connect through HTTPS (normal web requests) and **webhooks**:
    - You send messages via API calls.
    - WhatsApp sends you incoming messages and status updates to your webhook URL.


## How pricing basically works

- WhatsApp charges the business (or the provider you use) **for template messages**, and the price depends on:
    - The country of the user.
    - The type of message (marketing vs utility vs authentication).
- Replies inside the 24‑hour support window are usually **much cheaper or free** from WhatsApp’s side.
- If you use a third‑party provider, they often add a **small extra fee** per message or a **monthly subscription**.


## Limits and scale

- New numbers start with **lower limits** on how many people you can message per day.
- As your business is verified and users react well (no spam complaints), WhatsApp automatically **raises your limits** so you can message more people and send faster.


## Where it’s going (big picture)

- More focus on **privacy** (moving toward internal IDs instead of raw phone numbers).
- More **interactive features** (flows, forms, coupons, etc.) to turn WhatsApp into a mini “app” for your business.
- Higher default **sending limits** so serious businesses can run big campaigns and support operations fully inside WhatsApp.

If you tell me whether you’re thinking about support, marketing, or a specific project, I can restate this specifically for that use case in one short diagram/flow.

---

# what is the Meta Business Platform (direct API)

Meta’s “Business Platform (direct API)” is basically the official way to talk to WhatsApp **directly with Meta**, without going through Twilio, MessageBird, etc.

### What it is

- It’s the **official WhatsApp Cloud API** hosted by Meta.
- Your backend calls Meta’s HTTP endpoints, and Meta sends webhooks back to your server with new messages and statuses.
- You manage everything in **Meta Business Manager**: phone numbers, templates, webhooks, access tokens.


### How it works at a high level

1. You create a Meta developer + business account and add a WhatsApp Business account.
2. You connect a phone number (this number won’t be used in a normal WhatsApp app).
3. Your server:
    - Sends messages via Meta’s Cloud API endpoints.
    - Receives incoming messages and events at your webhook URL.
4. You build your own logic (or UI) on top: bots, routing, integrations with CRM, etc.

### Why it’s called “direct API”

- With Twilio/MessageBird, you call their APIs and they talk to Meta for you (they add UX, inbox, extra features, and extra fees).
- With the **direct API**, you talk straight to Meta:
    - No CPaaS markup on Meta’s message fees.
    - But you must build/host your own middleware, inbox, monitoring, etc.


### What you get

- Full access to WhatsApp features: templates, interactive buttons/lists, flows, media, etc.
- High scale (once Meta trusts your business/number).
- Fast access to new features because Meta runs the infrastructure.


### Trade‑offs (simple view)

- **Pros**
    - Cheapest at scale (you pay Meta’s prices, not someone else’s markup).
    - Most control and flexibility (you design your own stack).
- **Cons**
    - More engineering/DevOps work: you must handle authentication, scaling, retries, logging, dashboards, etc.
    - No built‑in UI; you must build or adopt one.

If you want, I can draw a simple block diagram (text) showing “your backend ↔ Meta direct API” vs “your backend ↔ Twilio ↔ Meta” so you can drop it straight into your notes.
<span style="display:none">[^4_1][^4_2][^4_3][^4_4][^4_5][^4_6][^4_7][^4_8][^4_9]</span>

<div align="center">⁂</div>

[^4_1]: https://chatarmin.com/en/blog/whatsapp-cloudapi

[^4_2]: https://www.zoko.io/post/future-trends-whatsapp-api-improvements

[^4_3]: https://flowcall.co/blog/whatsapp-business-api-pricing-2026

[^4_4]: https://www.linkedin.com/pulse/whatsapp-business-api-2026-updates-portfolio-pacing-100k-messaging-yvdhc

[^4_5]: https://developers.facebook.com/documentation/business-messaging/whatsapp/calling

[^4_6]: https://www.reddit.com/r/WhatsappBusinessAPI/comments/1qj6a5b/why_does_meta_require_developers_to_maintain_a/

[^4_7]: https://www.connverz.com/whatsapp-cloud-api-integration-guide-for-developers-in-2026/

[^4_8]: https://www.unipile.com/whatsapp-api-a-complete-guide-to-integration/

[^4_9]: https://developers.facebook.com/blog/post/2025/03/19/introducing-api-solutions-for-whatsapp-business-users-launched/


---

# what is twilio

Twilio is a cloud **communications** company that gives developers APIs to add things like SMS, WhatsApp, voice calls, and email into their own apps.[^5_1][^5_2]

## In simple terms

- Twilio is a “CPaaS” (Communications Platform as a Service) – basically a toolbox in the cloud for sending messages and making calls from code.[^5_5][^5_1]
- Instead of you dealing with phone carriers, WhatsApp, email servers, etc., Twilio handles that complexity and gives you simple APIs.[^5_2][^5_1]


## What you can do with Twilio

- Send/receive SMS, WhatsApp, and other messages from your app.[^5_1][^5_5]
- Make and receive phone calls (voice) over the internet.[^5_4][^5_5]
- Send transactional and marketing emails (via Twilio SendGrid).[^5_5][^5_1]
- Verify users with one‑time passcodes and other security checks.[^5_1][^5_5]


## Why people use it

- It scales globally (180+ countries) and hides telecom complexity for you.[^5_6][^5_1]
- It has good docs, SDKs, and lots of examples, so devs can integrate quickly.[^5_3][^5_1]
- Many products (like ride‑sharing apps or delivery apps) quietly use Twilio under the hood to send you texts and call notifications.[^5_2][^5_5]

If you want, next I can explain specifically what Twilio’s WhatsApp API layer does compared to calling Meta’s API directly.
<span style="display:none">[^5_7][^5_8]</span>

<div align="center">⁂</div>

[^5_1]: https://www.twilio.com/en-us/cpaas

[^5_2]: https://www.twilio.com/docs/glossary/what-is-a-platform

[^5_3]: https://www.infotech.com/software-reviews/products/twilio-cpaas?c_id=211

[^5_4]: https://www.twilio.com/en-us/resource-center/what-is-twilio-an-introduction-to-the-leading-customer-engagement-platform

[^5_5]: https://www.twilio.com/en-us/resource-center/what-is-cpaas-guide

[^5_6]: https://www.twilio.com/en-us

[^5_7]: https://www.onsip.com/voip-resources/voip-fundamentals/what-is-cpaas-communications-platform-as-a-service-explained

[^5_8]: https://hr.mcleanco.com/software-reviews/categories/communications-platform-as-a-service/compare/twilio-cpaas-vs-aws-communication-developer-services


---

# compare twilio and Meta Business Platform (direct API) in simple terms

Here’s the simple, practical difference between **Twilio** and **Meta Business Platform (direct WhatsApp API)**.

## One‑line idea

- **Meta direct** = talk **straight to WhatsApp** yourself.
- **Twilio** = talk to **Twilio**, and Twilio talks to WhatsApp for you.[^6_1][^6_2]

***

## Cost

- **Meta direct**
    - You pay **only Meta’s WhatsApp fees** (per template message, price depends on country and type).[^6_3]
    - No extra per‑message markup from Meta.
- **Twilio**
    - You pay **Meta’s WhatsApp fee + Twilio’s fee**.
    - Twilio’s fee for WhatsApp is **0.005 USD per message (sent or received)**.[^6_4][^6_5][^6_6]

So Twilio is usually **more expensive per message**, but you get convenience.[^6_6][^6_3]

***

## Setup and complexity

- **Meta direct (Cloud API)**
    - You must create a Meta developer + business account, connect a number, manage tokens, webhooks, scaling, logs, dashboards, etc.[^6_7][^6_8]
    - More **DevOps + backend work**, but full control.[^6_8][^6_7]
- **Twilio**
    - You sign up on Twilio, buy/attach a number, flip some settings, and use their **single messaging API** for WhatsApp.[^6_2][^6_9]
    - Easier onboarding, lots of docs and SDKs; less infrastructure for you to manage.[^6_10][^6_11]

***

## Features around the API

- **Meta direct**
    - Gives raw WhatsApp features: templates, media, interactive buttons, flows, webhooks.[^6_12][^6_8]
    - No built‑in inbox UI, routing, analytics; you build or buy those separately.[^6_7][^6_8]
- **Twilio**
    - Same WhatsApp features (templates, interactive messages) but wrapped in Twilio’s **Programmable Messaging API**.[^6_9][^6_2]
    - Plus extras: sandbox, debugging tools, web console, unified API for SMS + WhatsApp, good documentation.[^6_11][^6_2]

***

## When to pick which (intuition)

- **Choose Meta direct** if:
    - You want **lowest cost at scale** and have engineers/infra to manage webhooks, queues, dashboards, etc.[^6_13][^6_8]
- **Choose Twilio** if:
    - You want the **simplest integration**, already use Twilio for SMS/voice, or don’t want to deal with Meta’s developer and infra details.[^6_1][^6_10]

If you tell me your project size (e.g., “student prototype” vs “real startup”), I can say clearly: “Use X for your use case and here’s why.”
<span style="display:none">[^6_14][^6_15]</span>

<div align="center">⁂</div>

[^6_1]: https://blog.peppercloud.com/types-of-whatsapp-crm-integrations-whatsapp-twilio-vs-whatsapp-cloud-api-vs-whatsapp-web/

[^6_2]: https://www.twilio.com/en-us/blog/insights/best-practices/sms-vs-whatsapp-for-business

[^6_3]: https://www.spurnow.com/en/blogs/whatsapp-business-api-pricing-explained

[^6_4]: https://www.twilio.com/en-us/whatsapp/pricing

[^6_5]: https://textus.com/blog/twilio-pricing

[^6_6]: https://chatarmin.com/en/blog/whats-app-api-pricing

[^6_7]: https://www.connverz.com/whatsapp-cloud-api-integration-guide-for-developers-in-2026/

[^6_8]: https://chatarmin.com/en/blog/whatsapp-cloudapi

[^6_9]: https://www.twilio.com/en-us/messaging/channels/whatsapp

[^6_10]: https://wasenderapi.com/blog/wasenderapi-vs-twilio-vs-360dialog-the-ultimate-whatsapp-api-comparison-for-businesses-in-2025

[^6_11]: https://www.twilio.com/en-us/resource-center/what-is-twilio-an-introduction-to-the-leading-customer-engagement-platform

[^6_12]: https://developers.facebook.com/blog/post/2025/03/19/introducing-api-solutions-for-whatsapp-business-users-launched/

[^6_13]: https://flowcall.co/blog/whatsapp-business-api-pricing-2026

[^6_14]: https://www.zoko.io/post/whatsapp-business-api-vs-twilio

[^6_15]: https://www.twilio.com/en-us/changelog/meta-is-updating-whatsapp-pricing-on-july-1--2025


---

# <q>ou get convenienc</q> how is it more convenient

It’s more convenient mainly because Twilio hides Meta’s complexity and gives you a smoother developer experience.

### 1. Setup \& onboarding

- With **Meta direct**, you deal with: Meta Developer account, Business Manager, WhatsApp Business account, app review, tokens, number onboarding, and webhook verification yourself.[^7_1][^7_2]
- With **Twilio**, you mostly: create a Twilio project, enable WhatsApp, configure a sandbox/number, and start sending via one messaging API – far fewer Meta‑specific steps.[^7_3][^7_4]


### 2. One API for many channels

- Twilio uses a **single messaging API** for SMS, WhatsApp, and other channels.[^7_4][^7_3]
- That means your code is almost the same whether you send an SMS or a WhatsApp message; you don’t have to learn multiple vendor‑specific APIs.[^7_5][^7_3]


### 3. Better tooling out of the box

- Twilio gives you: logs in the console, message inspectors, test credentials, SDKs for many languages, and ready‑made code samples.[^7_3][^7_5]
- Meta direct gives you the raw API and webhooks; things like dashboards, retries, queues, error alerts, and debugging tools are on you to build.[^7_2][^7_1]


### 4. Less infra \& operations work

- Twilio already handles scale, retries, and telecom edge cases as part of their platform.[^7_6][^7_7]
- With Meta direct, your own service must manage: scaling under load, idempotency, error handling, monitoring, and sometimes regional hosting decisions.[^7_1][^7_2]

So you pay Twilio a small fee per message because they save you time on setup, integration, debugging, and operations, especially helpful for small teams or prototypes.[^7_8][^7_9][^7_10]

<div align="center">⁂</div>

[^7_1]: https://chatarmin.com/en/blog/whatsapp-cloudapi

[^7_2]: https://www.connverz.com/whatsapp-cloud-api-integration-guide-for-developers-in-2026/

[^7_3]: https://www.twilio.com/en-us/blog/insights/best-practices/sms-vs-whatsapp-for-business

[^7_4]: https://www.twilio.com/en-us/messaging/channels/whatsapp

[^7_5]: https://www.twilio.com/en-us/resource-center/what-is-twilio-an-introduction-to-the-leading-customer-engagement-platform

[^7_6]: https://www.twilio.com/en-us/cpaas

[^7_7]: https://www.twilio.com/en-us/resource-center/what-is-cpaas-guide

[^7_8]: https://www.spurnow.com/en/blogs/whatsapp-business-api-pricing-explained

[^7_9]: https://www.twilio.com/en-us/whatsapp/pricing

[^7_10]: https://textus.com/blog/twilio-pricing


---

# what is messagebird

MessageBird (now rebranded as **Bird**) is a cloud communications and customer engagement platform, similar in spirit to Twilio.

In simple terms:

- It lets businesses talk to customers on **many channels from one place**: WhatsApp, SMS, email, voice calls, Instagram, Facebook Messenger, Telegram, etc.
- Developers can use **APIs** to send and receive messages, while non‑technical teams can use visual tools (like an inbox and flow builder) to handle conversations and automation.
- It includes a **shared inbox** so support/sales teams can see and reply to all customer messages in one UI, plus features like routing, analytics, and automations.
- For WhatsApp specifically, it acts as a **WhatsApp Business API provider**: it connects your business to WhatsApp, manages the infrastructure, and adds extra tools (templates UI, flows, inbox) on top.

If you want, next I can compare MessageBird/Bird to Twilio in the same “convenience vs cost vs tooling” style you used for Twilio vs Meta direct.
<span style="display:none">[^8_1][^8_2][^8_3][^8_4][^8_5][^8_6][^8_7][^8_8][^8_9]</span>

<div align="center">⁂</div>

[^8_1]: https://blogs.zoftwarehub.com/messagebird-in-2025-detailed-review-expert-analysis/

[^8_2]: https://thecxlead.com/tools/messagebird-review/

[^8_3]: https://www.callbell.eu/en/how-messagebird-works/index.html

[^8_4]: https://www.ematicsolutions.com/messagebird/

[^8_5]: https://rootstack.com/en/blog/all-about-messagebird-and-its-service-cloud

[^8_6]: https://bird.com/en-us/

[^8_7]: https://bird.com/en-us/support

[^8_8]: https://www.pipelinersales.com/crm/apps/messagebird/

[^8_9]: https://bird.com/en-us/smb


---

# compare MessageBird with Twilio

Here’s a simple, side‑by‑side comparison of **MessageBird (Bird)** and **Twilio**.

## Big picture

- **Twilio**: Very **developer‑first toolkit** for SMS, WhatsApp, voice, email, etc. Lots of APIs, super flexible, but feels “technical.”
- **MessageBird/Bird**: More **business‑app + APIs**. Strong on omnichannel inbox and visual automation for support/marketing teams, not just developers.


## Ease of use

- **Twilio**
    - Console feels like a big toolbox: powerful, but you pick and wire everything yourself.
    - Best if you’re comfortable reading docs, writing code, and designing your own flows.
- **MessageBird**
    - Puts more emphasis on a **ready UI**: omnichannel shared inbox, flow builder, visual automations.
    - Friendlier to non‑technical support/marketing teams out of the box.


## Features (practically)

- Both can: send/receive WhatsApp, SMS, etc., and integrate by API.
- **Twilio special strengths**:
    - Large product surface (Programmable SMS, Voice, Video, Flex contact‑center, SendGrid email).
    - Lots of language SDKs and integrations; “lego blocks” to build anything.
- **MessageBird strengths**:
    - Omnichannel inbox and automation is more “batteries‑included.”
    - Good if you want one place where agents live all day handling WhatsApp + other channels.


## Pricing feel (high level)

- Both: pay‑as‑you‑go per message/interaction, plus some add‑on products.
- Twilio often has **very transparent per‑message prices but adds markups** and extra costs (e.g., for registrations, some carrier fees), which can surprise you at scale.
- MessageBird’s raw per‑SMS/WhatsApp prices tend to be in the **same ballpark**; sometimes slightly cheaper in a given region, but it depends on country and volume.
- In practice, you usually choose based on **tooling + workflow fit**, not tiny price differences.


## When to choose which

- Pick **Twilio** if:
    - You have devs who like APIs and want maximum flexibility.
    - You already use Twilio (e.g., for SMS/voice/email) and want to add WhatsApp in the same stack.
    - You don’t mind building or integrating your own inbox/automation UI.
- Pick **MessageBird/Bird** if:
    - You care a lot about an **omnichannel inbox** and visual flow builder for non‑technical teams.
    - You want an “all‑in‑one” engagement/CRM‑ish layer rather than just comms plumbing.

If you tell me your use case (class project vs startup, marketing vs support), I can say very concretely: “Go with X and here’s exactly why for you.”
<span style="display:none">[^9_1][^9_2][^9_3][^9_4][^9_5][^9_6][^9_7][^9_8][^9_9]</span>

<div align="center">⁂</div>

[^9_1]: https://www.courier.com/integrations/compare/messagebird-vs-twilio

[^9_2]: https://textellent.com/blog/twilio-vs-messagebird/

[^9_3]: https://www.smscountry.com/blog/twilio-vs-messagebird-vs-smscountry/

[^9_4]: https://respond.io/blog/twilio-vs-messagebird-vs-respondio

[^9_5]: https://nocodedev.com/twilio-versus-messagebird-in-a-no-code-development-fight/

[^9_6]: https://ably.com/compare/bird-vs-twilio

[^9_7]: https://www.reddit.com/r/SaaS/comments/1quypzk/twilio_vs_smaller_sms_providers_anyone_actually/

[^9_8]: https://www.youtube.com/watch?v=-nL2p2fxub8

[^9_9]: https://www.g2.com/compare/messagebird-bird-vs-twilio


---

# who are 2 new emerging WhatsApp API providers who would be best for my product as a multi-channel engagement platform for my non-profit

Two good “emerging but mature enough” options for a **multi‑channel engagement platform for a non‑profit** are:

1. **Trengo**
2. **SleekFlow**

I’ll explain why and how they compare to what you need.

***

## 1. Trengo – team‑friendly, multichannel hub

Trengo is a customer engagement platform that sits on top of WhatsApp Business API and other channels (email, Instagram, Messenger, etc.).

Why it fits a non‑profit:

- **True multichannel inbox**: One shared inbox for WhatsApp, email, website chat, Facebook, Instagram, and more. This is great if volunteers or staff switch channels but you want a single view of each beneficiary/donor.
- **Collaboration first**: You can assign conversations, add internal notes, tag messages (e.g., “donor”, “intake”, “urgent”), and build simple workflows without heavy coding.
- **Automation with guardrails**: You can create basic flows like “route WhatsApp messages that mention ‘food’ to the food‑aid team”, or send auto‑replies after hours, without having to build a full bot from scratch.
- **Good fit for non‑technical teams**: Staff can live in Trengo’s UI, while you (or another dev) handle only the lighter integration (webhooks, syncing contacts, etc.).
- **Non‑profit angle**: Their pricing and tooling are oriented to SMBs and mid‑market; that usually gives more flexibility in negotiating non‑profit discounts than ultra‑enterprise players.

For your use case: Trengo can essentially *be* your “multi‑channel engagement layer” where WhatsApp is just one of several channels, which is what you described.

***

## 2. SleekFlow – AI‑powered omnichannel journeys

SleekFlow is another newer‑wave WhatsApp BSP that leans hard into omnichannel and automation.

Why it fits a non‑profit:

- **Omnichannel + journeys**: It supports WhatsApp, SMS, social channels, and web chat, and lets you design journeys like “new volunteer → welcome series” or “new beneficiary → intake questions → assign to caseworker”.
- **Flow builder \& templates**: No‑code flows to automate common paths (RSVP to an event, confirm attendance, collect basic info, send follow‑up reminders). That’s powerful for resource‑constrained non‑profits that still need structured processes.
- **Team inbox \& roles**: Similar to Trengo, it has a shared inbox with roles, assignment, and notes, so multiple coordinators can handle incoming WhatsApp and social messages.
- **Analytics**: You get basic analytics on campaign engagement and response times, which can help you report impact (e.g., “X people reached, Y responded”) to donors or leadership.
- **API + integrations**: If you later want to connect to a CRM or a custom database, SleekFlow exposes APIs and some standard integrations so you don’t get boxed in.

For your use case: SleekFlow is strong if you want to orchestrate **end‑to‑end journeys** (onboarding, reminders, follow‑ups) across channels without writing a ton of custom code.

***

## Which is “best” for you?

For a non‑profit multi‑channel engagement platform, your constraints are usually:

- Limited engineering bandwidth
- Volunteer/staff turnover → need a simple UI
- Need to be on **WhatsApp + at least one or two other channels**
- Tight budget, possibly looking for non‑profit discounts

**My recommendation:**

- Start with **Trengo** if your priority is: “One shared inbox where our small team can handle WhatsApp + email + social quickly, with light automation.”
- Consider **SleekFlow** if your priority is: “We want visual automation and journeys (onboarding, reminders, campaigns) across channels, and we’re willing to invest a bit more time in setup.”

If you tell me:

- which channels you 100% must support (e.g., WhatsApp + email + Instagram), and
- roughly how many monthly active contacts you expect (tens, hundreds, thousands),

I can give you a very concrete “pick X, ignore Y for now” plus how you might structure your non‑profit flows on that platform.
<span style="display:none">[^10_1][^10_2][^10_3][^10_4][^10_5][^10_6][^10_7][^10_8]</span>

<div align="center">⁂</div>

[^10_1]: https://www.linkedin.com/pulse/top-10-whatsapp-business-api-providers-2026-ged2c

[^10_2]: https://trengo.com/blog/whatsapp-business-api-partners

[^10_3]: https://wanotifier.com/best-whatsapp-business-api-providers/

[^10_4]: https://sleekflow.io/en-us/blog/best-whatsapp-api-providers

[^10_5]: https://prelude.so/blog/best-whatsapp-business-solution-providers

[^10_6]: https://www.reddit.com/r/WhatsAppBusiness_API/comments/1qh0525/best_whatsapp_business_api_provider_for_small/

[^10_7]: https://www.youtube.com/watch?v=To2JBH96RsI

[^10_8]: https://chatarmin.com/en/blog/whats-app-business-api-integration


---

# what about zixflow or retell

Zixflow and Retell are both in the “newer wave” of WhatsApp API / messaging providers, but they focus on slightly different things.

## Zixflow (WhatsApp + CRM‑ish)

- **What it is**: A SaaS platform that combines WhatsApp messaging with light CRM and marketing automation. It’s positioned more like an “all‑in‑one engagement tool” than a pure low‑level API provider.
- **WhatsApp angle**:
    - Uses the official WhatsApp Business API under the hood, giving you broadcasts, campaigns, templates, basic CRM, and automation flows.
    - Good fit if you want a **UI + automation** (teams, campaigns, pipelines) and only light custom coding.
- **Pricing style (roughly)**:
    - Subscription plans (starter/business tiers) plus Meta’s message costs.
    - Often marketed with a free or low‑cost starter tier for small teams, then higher tiers as you add users or features.
- **When it makes sense**:
    - You want WhatsApp + email/SMS + simple sales/marketing workflows in one place.
    - Non‑technical team members will live in the tool; WhatsApp is just one of the channels.


## Retell (voice/AI‑first, with WhatsApp via API)

“Retell” can refer to a couple of products, but the one people usually mean in this space is an **AI calling / AI agent platform** that can also plug into channels like WhatsApp via APIs or integrations.

- **What it is**: Think “AI agent that can talk to customers” (often voice‑first) with APIs to connect it to phone, web, or messaging channels.
- **WhatsApp angle**:
    - Rather than being a WhatsApp BSP itself, it typically **sits on top of a WhatsApp provider** (or your own Cloud API setup).
    - The value is in the **AI conversation logic** (LLM agent, routing, workflows), not in the raw WhatsApp connectivity.
- **When it makes sense**:
    - You already have or can get WhatsApp connectivity (e.g., Meta direct, Twilio, other BSP), and you want **smart AI conversations** on that channel.
    - Your main differentiator is AI/voice automation, not the underlying WhatsApp plumbing.


## How to talk about them in your assignment

If your prof wants “emerging WhatsApp API providers,” you can:

- Treat **Zixflow** as a **WhatsApp‑capable BSP/engagement platform** (official API under the hood, subscription + Meta fees, CRM‑ish tooling).
- Treat **Retell** as an **AI agent layer that can connect to WhatsApp** via other providers, so it’s more of an “AI front‑end” than a pure BSP.

For your comparison file, you can either (a) pick Zixflow as one of your two new providers and pair it with something more directly comparable like 360dialog/Vonage, or (b) include Retell but clearly label it as “AI layer on top of WhatsApp providers,” not a traditional BSP.
<span style="display:none">[^11_1][^11_10][^11_2][^11_3][^11_4][^11_5][^11_6][^11_7][^11_8][^11_9]</span>

<div align="center">⁂</div>

[^11_1]: https://decisiontele.com/news/best-whatsapp-api-provider.html

[^11_2]: https://chatmitra.com/chatmitra-vs-zixflow/

[^11_3]: https://blog.stackademic.com/ultimate-list-of-45-whatsapp-business-api-solution-providers-6b33f9abeec8

[^11_4]: https://wabaconnect.com/10-top-whatsapp-business-api-providers-in-2025/

[^11_5]: https://www.capterra.com/p/240699/Zixflow/

[^11_6]: https://www.getapp.com/sales-software/a/sales-simplify/

[^11_7]: https://gallabox.com/compare/zixflow

[^11_8]: https://www.softwareadvice.com/crm/sales-simplify-profile/

[^11_9]: https://zixflow.com

[^11_10]: https://www.heyy.io/blog/whatsapp-automation-tools


---

# give me 2 emerging WhatsApp API providers

Two good “emerging” (newer‑wave, not the old-school Twilio/MessageBird) WhatsApp API providers you can use in your comparison are:

1. **Zixflow**
2. **WANotifier**

### 1. Zixflow – WhatsApp + light CRM/engagement

- What it is: an AI‑flavored engagement tool that combines WhatsApp campaigns, basic CRM, and automation flows in one SaaS product. It’s built more like a mini HubSpot‑for‑WhatsApp than a barebones API gateway.
- Why it counts as “emerging”: it’s relatively new compared with Twilio/MessageBird/Infobip and is only recently appearing in “best WhatsApp tools” lists and comparison blogs.
- Why it could fit your non‑profit, multi‑channel idea:
    - Has WhatsApp campaigns, sequences, and contact management out of the box, so staff can send outreach or reminders without you writing a full backend.
    - Offers some multi‑channel capabilities (email/SMS and sales‑pipeline style views), which aligns with your “multi‑channel engagement platform” concept.
    - Better suited if you want a UI‑driven tool with *some* APIs, rather than a pure developer platform.

In your markdown you can position Zixflow as:
> “Emerging engagement‑first WhatsApp provider with built‑in CRM and campaign tooling, better for small orgs that want UI + light automation rather than deep custom code.”

***

### 2. WANotifier – transparent pricing, 0% markup

- What it is: a newer WhatsApp Business API provider focused on bulk campaigns, flows, and a shared inbox, marketed heavily on “no markup on Meta’s WhatsApp fees.”
- Why it counts as “emerging”: it’s relatively new compared with classic BSPs and is just now showing up near the top of 2025–2026 “best WhatsApp API providers” lists.
- Why it could fit your non‑profit, multi‑channel idea:
    - Shared inbox and basic CRM‑style segmentation, which works well for a small team coordinating outreach to beneficiaries/volunteers.
    - Strong automation primitives (drip campaigns, flows, chatbots) so you can run onboarding or reminder sequences without a big engineering team.
    - Very transparent, low‑markup pricing, which is attractive for a budget‑constrained non‑profit (you mostly pay Meta’s message cost plus a modest SaaS fee).

In your markdown you can position WANotifier as:
> “Emerging WhatsApp BSP optimized for campaigns and automation, with shared inbox and 0% message markup, making it appealing for cost‑sensitive teams.”

***

If you want, I can now give you a short table row for each (Zixflow + WANotifier) with the same columns you’re already using: pricing model, rate limits (high‑level), India vs US, webhooks, ease of integration—so you can paste them straight into `whatsapp-api-comparison.md`.
<span style="display:none">[^12_1][^12_2][^12_3][^12_4][^12_5][^12_6][^12_7][^12_8]</span>

<div align="center">⁂</div>

[^12_1]: https://www.linkedin.com/pulse/top-10-whatsapp-business-api-providers-2026-ged2c

[^12_2]: https://trengo.com/blog/whatsapp-business-api-partners

[^12_3]: https://wanotifier.com/best-whatsapp-business-api-providers/

[^12_4]: https://sleekflow.io/en-us/blog/best-whatsapp-api-providers

[^12_5]: https://prelude.so/blog/best-whatsapp-business-solution-providers

[^12_6]: https://www.reddit.com/r/WhatsAppBusiness_API/comments/1qh0525/best_whatsapp_business_api_provider_for_small/

[^12_7]: https://www.youtube.com/watch?v=To2JBH96RsI

[^12_8]: https://chatarmin.com/en/blog/whats-app-business-api-integration

