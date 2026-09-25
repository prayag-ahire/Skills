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
