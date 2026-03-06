# Task 5: Conversation Analytics Specification (JKYog WhatsApp Bot)
**Owner:** Harshith Bharathbhushan  
**Team:** 4A — Conversational UX & Design  
**Project:** JKYog Multi-Channel Engagement Platform  
**Date:** March 6, 2026

---

## 1. Executive Summary
This document defines the comprehensive tracking methodology for the JKYog WhatsApp bot. By leveraging the specific interaction hooks integrated into the team's conversational design—including unique node identifiers from Rujul’s JSON trees and explicit error triggers from Chanakya’s scripts—this framework allows for real-time monitoring of user behavior, system reliability, and mission-aligned growth.

---

## 2. Key Performance Indicators (KPIs)
The bot’s success will be evaluated against three primary categories of metrics:

### A. Business & Mission Success (ROI)
* **Donation Conversion Rate:** Percentage of users who initiate a donation inquiry (`DR_1`) and progress to a successful sponsorship or tax receipt outcome.
* **Event Registration Volume:** Total successful sign-ups captured via the `VI_4` (Upcoming Events) and `VI_6` (Event Details) interaction paths.
* **Volunteer Lead Generation:** Number of users successfully expressing interest in volunteer opportunities via the FAQ/Inquiry flows.

### B. User Engagement & UX Quality
* **Goal Completion Rate (GCR):** Percentage of users who reach the final resolution nodes (e.g., `VI_9` for inquiries or successful receipt confirmation).
* **Average Session Depth:** The mean number of message exchanges per session, indicating the richness of user engagement.
* **Language Adoption Trends:** Tracking `record_lang_switch` events (from Nikita's logic) to identify demand for English, Hindi, and Gujarati content.

### C. Technical Reliability & Resilience
* **Fallthrough Rate:** Frequency of `log_intent_fail` events relative to total interactions.
* **Human Handoff Rate:** Percentage of sessions requiring escalation to a volunteer via Chanakya’s `log_human_escalation_fail` path.
* **System Latency:** Monitoring `log_fallback_timeout` events to ensure backend API stability (Target: < 1.5s).

---

## 3. Funnel Analysis & Drop-off Identification
Using the `node_id` architecture established in the team's JSON files, we track the user journey through three primary funnels to identify friction points.

| Target Funnel | Entry Node | Key Milestone Checkpoint | Success/End Node |
| :--- | :--- | :--- | :--- |
| **Donations** | `node_id: DR_1` | `node_id: DR_3` (Sponsorship) | `goal_reached_donations` |
| **Visitor Inquiries** | `node_id: VI_1` | `node_id: VI_2` (Timings) | `node_id: VI_9` (End) |
| **Directions** | `node_id: TD_1` | `node_id: TD_4` (Parking) | `goal_reached_directions` |



**Abandonment Strategy:** If data shows high traffic at `DR_1` but a significant drop-off before `DR_2` (Make a Donation), we will flag the "Start" node for content optimization to improve user motivation and CTA clarity.

---

## 4. Effectiveness & Intelligence Metrics
We will evaluate the bot's "Intelligence" using the following automated triggers:
* **Context Recovery Success:** Percentage of users who successfully resume a conversation after a `log_context_loss` event.
* **Deflection Efficiency:** The ratio of queries resolved by the bot without redirection to the website or manual human intervention.
* **Sentiment Shift:** Tracking the change in user tone from the initial greeting (`start` nodes) to the final interaction using natural language processing in the data transformation layer.

---

## 5. Technical Data Integration & Team Alignment
This analytics framework is operationalized through the following "Data Hooks" provided by Team 4A:

1. **Unique State IDs (Rujul):** All decision nodes (Inquiries, Directions, Donations) use specific `node_id` prefixes (`DR_`, `VI_`, `TD_`) for granular path tracking.
2. **Metadata Logging (Ananth):** The state machine logs `session_id`, `user_id`, `detected_intent`, and `communication_channel` at every state transition.
3. **Fallback Telemetry (Chanakya):** Five specific fallback scenarios emit unique event logs (`log_intent_fail`, `log_fallback_timeout`, `log_context_loss`, `log_human_escalation_fail`) for technical debugging.
4. **Localization Tracking (Nikita):** Language switches capture the `source` and `target` languages, enabling linguistic preference mapping across the devotee community.

---

## 6. Data Lifecycle & Visualization
Interaction data will follow a structured lifecycle to ensure data quality and business value:
1. **Raw Ingestion:** Immediate capture of WhatsApp webhooks and system event logs into a centralized cloud storage layer.
2. **Data Refinement:** Automated transformation processes to clean logs, calculate session durations, and mask sensitive PII (Personally Identifiable Information).
3. **Executive Reporting:** Final cleaned metrics are pushed to the JKYog Board Dashboard for real-time ROI monitoring and system health checks.
