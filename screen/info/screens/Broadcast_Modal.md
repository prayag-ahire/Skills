# Broadcast Request Modal - State & Architecture

## 1. Visual Architecture & Layout
**Information Hierarchy:**
1. Global Context (Sticky Header with Drag Handle)
2. Step 1: Service Selection (Grid of Pills)
3. Step 2: Time Selection (Horizontal Scroll of Pills)
4. Step 3: Context Inputs (Text Area + Photo Upload)
5. Primary Action (Sticky Footer CTA)

### Structural Wireframe
```text
================================================
[             [ Drag Handle ]                  ]
[ X           Broadcast Request                ]
[      Pings all verified workers within 5km   ]
================================================
[               (Scrollable Area)              ]
[                                              ]
[ What do you need help with?                  ]
[ [ Plumbing ] [ Electrical ] [ AC Repair ]    ]
[ [ Cleaning ] [ Carpentry ] [ Other ]         ]
[                                              ]
[ When do you need them?                       ]
[ [ Today ] [ Tomorrow ] [ Pick Date ]         ]
[ [ Right Now ] [ Morning ] [ Afternoon ]      ]
[                                              ]
[ Any details? (Optional)                      ]
[ +------------------------------------------+ ]
[ | Describe the issue...                    | ]
[ +------------------------------------------+ ]
[ [ 📷 Add photos ]                            ]
[                                              ]
================================================
[       [ BROADCAST REQUEST BUTTON ]           ]
================================================
```

### Loading State Wireframe (Scanning Radar)
```text
================================================
[                                              ]
[             [ Radar Animation ]              ]
[                                              ]
[         Finding available workers...         ]
[        Pinging 14 plumbers in your area      ]
[                                              ]
[             [ Cancel Search ]                ]
================================================
```

### Success State Wireframe
```text
================================================
[             [ Success Checkmark ]            ]
[                                              ]
[                 Job Accepted!                ]
[ Prayag Ahire has accepted your request and   ]
[ is reviewing the details.                    ]
[                                              ]
[          [ View Worker Profile ]             ]
================================================
```

## 2. Layout & Spacing Rules (Visual Architecture)
- **Modal Container:** Slides up from the bottom, covering 90% of the screen height. Top corners should be heavily rounded (e.g., 24px or 32px radius).
- **Header:** Fixed at the top of the modal. Contains a pill-shaped drag handle at the very top center, an `X` close button on the top left, and centered title/subtitle text.
- **Body Padding:** The scrollable content area should have generous padding (e.g., `24px` left/right).
- **Section Spacing:** Each step (What, When, Details) must be separated by substantial vertical white space (e.g., `32px` margin-bottom) to prevent visual crowding.
- **Pill Grids:** 
  - Service Selection: Flex-wrap layout with `12px` gap.
  - Time Selection: Two separate rows (Dates, then Times), each horizontally scrollable with `12px` gap.
## 3. Technical Decisions (Tokens & Styles - Stage 5)

### Color Palette (Inheriting from ProWorker System)
- **Modal Background:** `#FFFFFF` (Solid white for maximum contrast against the grey Home Screen).
- **Dimmer Overlay:** `#000000` with `0.6` opacity.
- **Primary Accent (Blue):** `#2563EB` (Used for Active selected pills, the massive Broadcast CTA, and loading radar pulses).
- **Secondary Accent:** `#EFF6FF` (Very light blue background for the selected pills to give a soft highlight).
- **Interactive Surface (Unselected):** `#F3F4F6` (Light grey for unselected pills, input backgrounds, and photo upload box).
- **Text Primary:** `#111827` (Dark Navy for headings and active pill text).
- **Text Secondary:** `#6B7280` (Muted grey for subtitles and unselected pill text).
- **Success Accent:** `#10B981` (Emerald Green for the Job Accepted checkmark).

### Radii & Elevation
- **Modal Top Corners:** `32px` radius.
- **Selection Pills:** `999px` (Full pill shape) for single-select items.
- **Input Areas:** `16px` radius (Matching the softness of the ProWorker brand).
- **Photo Upload Box:** `16px` radius, with a `2px dashed #D1D5DB` border.
- **Sticky Footer:** `0px` bottom radius, `24px` top radius, with a strong upward drop shadow: `0 -4px 20px rgba(0,0,0,0.08)`.

### Component Specs
- **Drag Handle:** `#E5E7EB`, `48px` wide, `4px` tall, `999px` radius.
- **Selection Pills:** `36px` height, `16px` horizontal padding. Font: `14px`, `500` weight.
- **Primary Broadcast CTA:** `56px` height (taller than standard buttons to emphasize the final commitment action), full width, `16px` radius. Font: `16px`, `700` weight.
- **Radar Animation Core:** A central circle (`40px` radius) with `2-3` expanding, fading concentric SVG `<circle>` rings scaling outward infinitely to simulate searching.
