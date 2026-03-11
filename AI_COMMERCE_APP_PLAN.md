# AI Commerce Assistant App Plan

## 1) One-page product spec

### Product name (working)
**DealMate AI**

### Problem
People waste time browsing multiple marketplaces and still struggle with:
- finding fair prices,
- avoiding scams,
- writing good listings,
- negotiating confidently.

### Target users
1. **Buyers** looking for used electronics under budget.
2. **Casual sellers** who want to list quickly and get fair value.

### Core value proposition
"Tell the app what you want to buy or sell, and AI handles the hard parts: pricing, listing quality, comparisons, and negotiation help."

### Primary use cases
- Buyer says: "Find me a used iPhone 13 under $400 near me in good condition."
- Seller uploads photos + short notes; app drafts title/description and suggested price.
- User receives guidance for offers/counter-offers.

### MVP scope (narrow)
- **Category:** smartphones only.
- **Geography:** one city/region.
- **Sources:** 2–3 marketplaces.
- **No in-app payments** (redirect users to external listing/purchase flow).

### Success metrics (first 90 days post-launch)
- 7-day retention > 20%.
- 30% of seller users publish an AI-generated listing.
- Buyer sessions leading to at least one saved listing > 40%.
- Scam-flag precision > 70% on reviewed cases.

---

## 2) MVP feature list

### Must-have features (v1)
1. **Conversational search**
   - Natural language query parsing.
   - Filters: budget, condition, distance.

2. **Price guidance**
   - "Good deal / fair / overpriced" badge.
   - Estimated fair-price range using recent comps.

3. **Seller listing assistant**
   - Auto-generated title + description from prompts/photos (if photos are available).
   - Listing quality checklist (missing specs, blurry photos, etc.).

4. **Negotiation assistant**
   - Suggested opening offer.
   - Counter-offer suggestions with configurable floor/ceiling.

5. **Safety signals**
   - Basic scam heuristics (too-good-to-be-true pricing, suspicious wording patterns, repeated repost behavior where data exists).

6. **Alerts**
   - Saved search + price-drop notifications.

### Nice-to-have (post-MVP)
- Multi-category support.
- Reputation scoring and trusted-seller indicators.
- Auto-posting integrations for sellers.
- In-app escrow/payment partnerships.

---

## 3) 90-day build roadmap

## Days 1–30: Foundation + first working flow

### Product/UX
- Define 3 key user journeys (buyer search, seller listing creation, negotiation).
- Ship low-fidelity wireframes and a clickable prototype.

### Engineering
- Set up backend API (auth, user profile, saved searches, listing normalization).
- Build data ingestion pipeline for selected marketplaces (API-first; no ToS-violating scraping).
- Implement first AI orchestration:
  - intent extraction,
  - response formatting,
  - listing-summary generation.

### Data/ML
- Establish a canonical listing schema.
- Build baseline price model with heuristic + median comps.

### Milestone
- Internal demo: buyer can query and receive ranked listings with basic pricing labels.

---

## Days 31–60: MVP feature completion

### Product/UX
- Add seller listing assistant UI.
- Add negotiation suggestion interface and safety warnings.

### Engineering
- Add alerts/notifications service.
- Implement prompt/version management and observability (latency, token usage, failure rates).
- Add moderation pipeline for risky outputs.

### Data/ML
- Improve fair-price model using condition, storage size, age, and local demand.
- Add rule-based + model-based scam flagging.

### Milestone
- Private beta for 20–50 users with full MVP loop.

---

## Days 61–90: Beta hardening + launch prep

### Product/UX
- Tighten onboarding and trust messaging.
- Add transparent "why this recommendation" explanations.

### Engineering
- Performance optimization and caching for popular searches.
- Add rate limiting, abuse protection, and audit logging.
- Error budget + SLOs for core endpoints.

### Data/ML
- A/B test recommendation styles (brief vs detailed).
- Calibrate scam alerts to reduce false positives.

### Go-to-market
- Launch a focused beta community in one region.
- Build referral loop and feedback capture.

### Milestone
- Public beta launch with clear category/region limitations.

---

## Suggested technical stack
- **Frontend:** React (Next.js) or Flutter.
- **Backend:** Python (FastAPI) or Node.js (Nest/Express).
- **Database:** Postgres + Redis cache.
- **Search:** Postgres full-text or OpenSearch.
- **AI:** LLM for chat + structured tool calls; embeddings for semantic matching.
- **Analytics:** PostHog / Amplitude.
- **Infra:** Docker + managed cloud (AWS/GCP/Azure) with CI/CD.

---

## Risks and mitigation
- **Marketplace policy risk:** prioritize official APIs and partnerships.
- **Fraud risk:** start with conservative warnings + user reporting.
- **AI hallucinations:** constrain outputs, use retrieval + strict templates.
- **Legal/compliance:** clear disclaimers, moderation, and terms for advisory output.
