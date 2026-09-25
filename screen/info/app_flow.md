# ProWorker - App Flow & Interaction Logic

## Worker Profile Screen

### 1. Navigation & Header
- **Back Arrow (`<`):** Navigates the user back to the previous screen (Home/Search).
- **Three Dots Menu (`⋮`):** Opens a bottom sheet with options: "Share Profile" and "Report Worker".
- **Social Icons (Instagram / YouTube):** Opens the respective external app or browser to the worker's linked profile.

### 2. Primary Action Buttons
- **Follow Button:**
  - *Default State:* Outlined blue pill, text "Follow".
  - *On Click:* Slight scale animation (`0.95`), changes to solid grey pill, text "Following".
- **Call Button:**
  - *Active State (Within Working Hours):* Solid blue pill with phone icon, text "Call". On click, initiates WebRTC call sequence.
  - *Inactive State (Outside Working Hours/Days):* Solid light grey pill, grey text "Unavailable", disabled pointer events. (As seen in the screenshot).

### 3. Tab Navigation (Photos, Reviews, Availability, About)
- *Interaction:* Horizontal scrollable tab row. Clicking a tab changes the active state to a solid blue pill (e.g., "Photos" in screenshot 1).
- *Action:* Replaces the content in the lower half of the screen below the tabs. Does not navigate to a new page (SPA behavior).

### 4. Tab Content Logic
#### A. Photos Tab
- Displays a 2-column grid of portfolio images.
- *On Click (Image):* Opens a full-screen lightbox modal. User can swipe horizontally to view the next/previous photo. Tap `X` or swipe down to close.

#### B. Reviews Tab
- **Write a Review Section:**
  - *Default:* Shows 5 empty stars.
  - *Interaction:* Tapping a star fills the stars up to that point (e.g., tapping the 4th star fills stars 1-4). 
  - *On Star Tap:* Reveals the "Share your experience" text input and the "Submit review" button.
  - *Submit:* Validates if a star rating exists. On success, clears the form and prepends the new review to the list below with a toast "Review submitted".
- **Review Feed:** Static vertical list of past reviews.

#### C. Availability Tab
- **Working Days Pills:** Static display. Blue pills (e.g., Tue-Sat) represent active working days. White/Grey pills (e.g., Sun, Mon) represent days off. Not clickable by the customer.
- **Calendar:** 
  - *Interaction:* Tapping `<` or `>` arrows switches the month view. 
  - *State:* Holidays/unavailable dates are visually distinct (e.g., greyed out or strike-through). Not selectable.

#### D. About Tab
- **Bio Text:** Static text description. If longer than 4 lines, truncates with a "Read more" inline button.
- **Product Details Grid:** 
  - *Interaction:* Tapping a product card navigates the user to a dedicated "Product Detail" screen or opens a bottom sheet with purchase info.
