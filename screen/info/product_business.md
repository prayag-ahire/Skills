# ProWorker - Product & Business Context

## 1. Product Vision
- **Product Name:** ProWorker
- **Core Concept:** Google Maps for finding people/workers. Connects customers directly with verified nearby workers.
- **Philosophy:** The platform intentionally avoids becoming a middleman. No booking system, no commission on jobs, worker controls pricing.
- **Target Audience:** Millions of independent workers (not agencies) and local customers in India.

## 2. User Roles
### Customer
- **App:** Consumer App (Flutter)
- **Actions:** Search for workers, filter by distance (2km, 5km, 8km default), browse portfolios/products, leave reviews, and contact workers via direct internet calling.
- **Restrictions:** Cannot create a profile, cannot book jobs or pay in-app.

### Independent Worker
- **App:** Worker App (React Native)
- **Actions:** Create a business profile, set schedule, set pricing (visit/service charges), upload portfolios (images/videos), sell products.
- **Restrictions:** Cannot act as an agency. 

## 3. Business Model
- **Primary:** Banner Ads (home, categories) and Native Ads (in product store and worker lists).
- **Future:** Premium worker subscriptions, local delivery integration, digital invoices, premium verification (identity badges).
- **Current Verification:** Free via OTP, funded by rewarded ads.

## 4. Key Constraints
- **What is NOT supported:** 
  - No middleman booking or payments.
  - No agencies allowed.
  - No Lawyers (due to Indian advertising laws).
  - No return policies yet for the product store.

## 5. SEO Strategy
- Every worker gets a public, static SEO page (e.g., `proworker.in/plumber/@rahul`) to ensure visibility on Google search.

## 6. Worker Profile Screen - Business Requirements
Based on reference screenshots:
- **Core Purpose:** The ultimate digital business card. Displays everything a customer needs to make a hiring or purchasing decision.
- **Identity Block:** Must include Avatar, Name, Profession, Rating (with count), Distance (km), and social links (Instagram/YouTube).
- **Primary Actions:** "Follow" (to subscribe to updates) and "Call" (WebRTC internet calling, which changes to "Unavailable" if outside working hours).
- **Tabbed Content (4 Sections):**
  1. **Photos:** A grid of the worker's portfolio images.
  2. **Reviews:** Allows users to leave a star rating and comment, and displays a feed of past customer reviews.
  3. **Availability:** Displays explicit working hours, days of the week (with active/inactive states), and a calendar showing specific holiday/unavailability dates.
  4. **About:** A text bio describing the worker's expertise, followed by a "Product details" grid where the worker sells inventory (e.g., pipes, shoes).

## 7. UX Copy & Text Content (Worker Profile Screen)
**Header & Core Identity:**
- Name: `Prayag ahire`
- Profession: `Plumber`
- Rating string: `3.5 (2 reviews)`
- Distance string: `0.0 km away`
- Primary CTAs: `Follow` and `Unavailable` (with phone icon)

**Navigation Tabs:**
- `Photos` | `Reviews` | `Availability` | `About`

**Reviews Tab Microcopy:**
- Section Title: `Write a review`
- Input Placeholder: `Share your experience (optional)`
- Submit Button: `Submit review`
- Mock Review 1: `Darshan` | `18 Sep 2026` | `Excellent service! Highly recommended`
- Mock Review 2: `prayag ahire` | `14 Sep 2026` | `Would recommend to others`

**Availability Tab Microcopy:**
- Time header: `Working hours` -> `9:00 AM – 3:00 PM`
- Days header: `Working days` -> `Sun`, `Mon`, `Tue`, `Wed`, `Thu`, `Fri`, `Sat`
- Holidays header: `Holidays`
- Helper text: `Marked days are when this worker is not available.`
- Calendar header: `September 2026`

**About Tab Microcopy:**
- Bio Text: `Reliable plumber with experience in pipe fitting, leak repairs, bathroom and kitchen installations, water tank connections, tap and shower fittings, and drainage maintenance. I provide quality workmanship, fair pricing, and on-time service for both residential and commercial jobs.`
- Store Header: `Product details`
- Product 1: `For sale` | `Appqw` | `₹399`
- Product 2: `For sale` | `Shoes` | `₹199`
