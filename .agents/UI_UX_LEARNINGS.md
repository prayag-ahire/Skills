# Central AI UI/UX Knowledge Base

This document serves as a persistent, global memory bank for the AI. Whenever the AI discovers a new design pattern, interaction flow, or technical SVG/HTML trick that improves the quality of the UI/UX, it MUST be logged here.

## 1. Icon Library (Lucide SVG Paths)
*Store newly discovered, high-quality SVG paths here so they can be reused across all future screens without bloating the HTML or fetching external libraries.*

- `#icon-home`: `<path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>`
- `#icon-user`: `<path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>`
- `#icon-check-circle`: `<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/>`

## 2. Interaction Flows & A/B Testing
*Document proven workflows for handling user interactions and testing new ideas.*

- **Non-Destructive Versioning:** When testing a new UI idea, always keep the original screen intact. Duplicate the original flow into a new `.flow-row` directly underneath it (V1 at the top, V2 below). Ensure Javascript IDs are suffixed (e.g., `-old`) to prevent cross-scope collision.
- **Async State Simulation:** For network requests (e.g., booking, searching), physically build all 3 states (Form, Loading, Success) in the SVG. Use `display="none"` and `setTimeout` to swap them in sequence to create a high-fidelity prototype feel.

## 3. Technical SVG & Layout Patterns
*Document rendering tricks, clipping rules, and layout constraints.*

- **Hardware Clipping (The Apple Bezel Rule):** Sticky CTA footers and bottom navigation bars MUST either be placed inside the global screen `clip-path` (to inherit the phone's border radius) OR must be drawn using a custom `<path>` with bottom arcs (`a40 40 0 0 1 -40 40`) to flawlessly trace the phone bezel. Square corners bleeding out of rounded bezels instantly destroy prototype authenticity.
- **Form Affordance in Empty States:** Never hide primary text inputs or buttons inside empty state cards unless the card physically collapses. If the card is sized to fit the input, the input must always be visible by default to establish clear affordance.

*(Note for AI: Continuously append to this file as you learn new tricks or refine your design system!)*

## 4. Figma Play & Dual-Flow Architecture
*The system uses two separate HTML environments to showcase the design: Canvas and Play Mode.*

- **Canvas (`proworker.html` / `build.py`):** Displays all screens simultaneously in a horizontal/vertical layout. Both V1 (Old Flow - literal screenshots) and V2 (New Flow - premium designs) must be injected here side-by-side so the user can see all screens at once. JS interactivity here is limited to internal component logic (like tabs or lightboxes).
- **Play Mode (`app.html` / `build_app.py`):** A single-device interactive prototype that acts like Figma Play. It starts with a black screen, transitions to a splash screen, and then routes to the selected flow (V1 or V2).
- **Navigation Routing:** In Play Mode, screens are stacked on top of each other using `opacity: 0; pointer-events: none` and `opacity: 1; pointer-events: auto`. We use a global `window.navigateTo('screen-id')` function to handle transitions between screens (e.g., clicking the Plumber icon routes from Home to Worker List).

## 5. Global JS Bundle Safety
*When injecting multiple JS files (`v1.js`, `v2.js`) into a single global prototype like Play Mode, strict safety measures are required.*

- **IIFE Isolation:** Every single JS file MUST be wrapped in an IIFE `(() => { ... })();`. A missing opening or closing bracket in one file will throw a Syntax Error that completely crashes the global bundle, breaking all interactive flows.
- **Null-Check Everything:** Because Play Mode dynamically shows/hides SVGs, `document.getElementById` might return `null` if a screen hasn't loaded or isn't part of the current flow. ALL event listeners (e.g., `workerSvg.addEventListener`) MUST be wrapped in `if (workerSvg)` to prevent fatal `TypeError`s.
- **Variable Collisions:** Be extremely careful when copy-pasting interaction logic between V1 and V2. Ensure variables (like `workerSvg`) are consistent and explicitly scoped within their respective IIFEs, or suffix IDs/variables (e.g., `workerProfileSvgOld`) to prevent cross-contamination.
