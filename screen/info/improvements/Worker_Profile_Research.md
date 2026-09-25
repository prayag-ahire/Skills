# Industry UX Research: Worker Profile

## Benchmark Sources
- **Competitors Analyzed:** TaskRabbit, Urban Company, Thumbtack, Angi.
- **Key Resources:** Mobbin, Pinterest (Service Marketplace UI), UX Planet Case Studies.

## Core UX Principles (The "Trust Engine")
In a service marketplace where users invite strangers into their homes, the Worker Profile acts primarily as a **trust-optimization engine**, not just a static resume. The most successful apps prioritize:
1. **Humanizing the Provider:** Smiling, well-lit, professional headshots increase booking rates drastically.
2. **Instant Social Proof:** Highlighting total jobs completed alongside star ratings.
3. **Frictionless Conversion:** A permanent, sticky Call-to-Action (CTA) at the bottom of the screen so users can book from anywhere in the scroll.

## Proposed Improvements to Our Current Design

### 1. The Hero Card (Trust & Verification)
* **Current:** Shows Avatar, Name, Profession, Stars (3.5), Review Count (2), and Distance.
* **Industry Standard:** Top apps heavily emphasize safety.
* **Actionable Improvement:** 
  - Add a **"Background Checked"** or **"ID Verified"** badge with a green checkmark next to the worker's name.
  - Add **"Completed Tasks"** metric (e.g., "150+ Jobs") alongside the Star Rating. This provides significantly more trust than just "2 reviews".

### 2. The Conversion Flow (Sticky Footer)
* **Current:** The "Follow" and "Call (Unavailable)" buttons are placed immediately below the Hero Card. If a user scrolls down to read reviews, those buttons disappear off the top of the screen.
* **Industry Standard:** TaskRabbit and Urban Company use a **Sticky Footer CTA** (e.g., a massive "Book Now" or "Message" button permanently fixed to the bottom of the screen viewport).
* **Actionable Improvement:** 
  - Move the primary booking/contact action to a sticky bottom container (`position: fixed` or `transform` fixed in SVG) with a slight gradient overlay above it to indicate scrollable content beneath.

### 3. Clearer Pricing Transparency
* **Current:** Pricing is listed under "Product details" in the About tab (e.g., "Appqw ₹399").
* **Industry Standard:** Users need to understand base costs immediately to reduce anxiety.
* **Actionable Improvement:** 
  - Add a prominent "Starting at ₹X / hour" tag directly in the Hero Card or as a floating chip on the sticky footer.

### 4. Categorized Reviews (Cognitive Load Reduction)
* **Current:** A single vertical feed of reviews.
* **Industry Standard:** For workers with many reviews, platforms allow users to filter reviews by specific skills (e.g., "Plumbing", "Electrical").
* **Actionable Improvement:** 
  - Add quick-filter pill buttons above the Review feed (e.g., [All] [Punctuality] [Quality] [Value]).

## Next Steps for the AI Team
1. The `visual-architecture-designer` should update the structural wireframe to include a Sticky Bottom CTA.
2. The `svg-master` should add Trust Badges (Verified Icon) to the Hero Card component library.
