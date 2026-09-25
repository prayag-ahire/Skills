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

## Home Screen (Broadcast Flow Entry)

### 1. Broadcast Request FAB
- **Floating Action Button (FAB):** Positioned at the bottom right (above the tab bar) or as a sticky banner. Text: "Quick Request" or a lightning bolt icon.
- *On Click:* Opens the **Broadcast Request Sheet** (Screen 3) as a modal overlay sliding up from the bottom.

## Broadcast Request Sheet (Screen 3)

### 1. Step 1: Service Selection
- **UI:** A grid of pills (e.g., Plumber, Electrician, AC Tech).
- *Interaction:* Single-select. Clicking a pill highlights it in blue.

### 2. Step 2: Date & Time
- **UI:** Horizontal scroll of dates (Today, Tomorrow) and time slots (Morning, Afternoon, Evening).
- *Interaction:* Single-select for date, single-select for time.

### 3. Step 3: Issue Description
- **UI:** Text area and "Upload Photo" dotted box.
- *Interaction:* Typing expands the text area. Clicking "Upload" opens native file picker.

### 4. Step 4: Broadcast CTA
- **Button:** Giant sticky button at the bottom of the sheet: "Broadcast to Plumbers within 5km".
- *On Click:* 
  - Validates that a service is selected.
  - Hides the form.
  - Displays a "Scanning Radar" loading state ("Pinging 14 plumbers nearby...").
  - (Mock response): After 3 seconds, shows a success state: "Job Claimed! Prayag Ahire is on the way." and displays a "View Details" button linking to the Worker Profile.
