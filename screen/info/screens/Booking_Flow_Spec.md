# Product Spec: Booking Request Flow (Future Feature)

## 1. Product Overview
- **Purpose:** To allow customers to officially request and book a service from a worker directly within the ProWorker app, moving beyond the current "Call Only" model.
- **Goal:** Increase trust by capturing service details upfront, giving workers context before they arrive, and tracking jobs digitally.

## 2. Feature Inventory: The Booking Flow
When a user taps "Book Now" on a Worker's Profile, they enter a multi-step booking request flow.

### Step 1: Service Selection
- **Objective:** Determine what the customer needs.
- **Inputs:** 
  - List of the worker's standard services (e.g., for a Plumber: "Leak Repair", "Pipe Installation", "General Inspection").
  - "Other / Custom Request" option.
- **Validation:** Must select at least one service.

### Step 2: Date & Time Preferences
- **Objective:** Find a mutually agreeable time based on the worker's Availability Calendar.
- **Inputs:**
  - Date Picker (blocks out dates the worker marked as Holidays).
  - Time Slot Selector (e.g., Morning, Afternoon, Evening) bounded by the worker's "Working Hours" (e.g., 9:00 AM - 3:00 PM).

### Step 3: Issue Description & Media
- **Objective:** Give the worker context so they bring the right tools.
- **Inputs:**
  - Text area: "Describe the issue (Optional)".
  - Media Upload: "Add photos of the problem" (up to 3 images).

### Step 4: Location & Confirmation
- **Objective:** Finalize the address and broadcast the request to the network.
- **Inputs:**
  - Map snippet showing the customer's location.
  - "Broadcast Request" sticky bottom CTA.
- **Outputs:** Shows a scanning radar or loading state "Finding plumbers within 3km..."

## 3. Business Rules (Constraints)
- **Broadcast Model (Uber-style):** When a request is sent, it is pinged to ALL available plumbers within the selected radius (3-5-8 km).
- **First-to-Claim:** The first worker to accept the request wins the job.
- **Instant Lockout:** As soon as one worker accepts, the job is immediately assigned to them and is no longer available for other workers to accept.
- **No Immediate Payments:** The booking is a *request*. No money changes hands through the app yet (respecting the "No middleman" core philosophy).

## 4. Proposed Screen Inventory
For the prototype, we will design **The Broadcast Booking Screen (Screen 3)**.
- Since this request goes to *all* nearby plumbers, this screen should probably be accessed from the Home/Search screen (e.g., "I need a Plumber"), rather than from a specific Worker's Profile.
- It compresses the 4 steps above into a single, scrollable, highly-visual form (Service Select pills -> Date Scroller -> Photo Upload -> Confirm Button).
