# Worker Profile Screen - State & Architecture

## 1. Visual Architecture & Layout
**Information Hierarchy:**
1. Global Navigation (App bar)
2. Worker Identity & Social Proof (Hero Card)
3. Primary Actions (Follow / Call)
4. Contextual Navigation (Tabs)
5. Dynamic Content Area (Tab specific)

### Structural Wireframe
```text
[ StatusBar ]
[ <   Worker Details   ⋮ ]
------------------------------------------------
[ [Avatar]  Prayag ahire               [IG] ]
[ [100x100] Plumber                         ]
[           ⭐⭐⭐⭐⭐ 3.5 (2 reviews)      [YT] ]
[           ⬈ 0.0 km away                   ]
------------------------------------------------
[ [   Follow   ]    [ 📞 Unavailable ]      ]
------------------------------------------------
[ Photos ] [ Reviews ] [ Availability ] [ About ]
------------------------------------------------
[[ DYNAMIC CONTENT AREA ]]
```

### Dynamic Content Layouts

**Photos Tab:**
- 2-Column Grid.
- 1:1 Aspect ratio images, ~8px gap between grid items.

**Reviews Tab:**
- **Write Review Block:** Surface container with `md` padding.
  - "Write a review" heading.
  - Row of 5 large outline stars.
  - Text input (pill shape, full width).
  - Submit Button (solid, full width).
- **Review List:** Vertical list, no borders, separated by whitespace or hairlines.
  - Layout: `[Avatar Circle]` `[Name]` `[⭐⭐⭐⭐⭐]`
                     `[Date]`
  - Review text below.

**Availability Tab:**
- Surface container with grouped sections:
  - **Hours:** `[Clock Icon]` "Working hours" -> text below.
  - **Days:** "Working days" -> Row of 7 compact pills.
  - **Calendar:** "Holidays" -> Header -> `[<]` "September 2026" `[>]` -> 7-column grid of dates.

**About Tab:**
- **Bio:** Full-width text block, 1.6 line height.
- **Products:** 
  - Heading: "Product details"
  - 2-Column Grid of Product Cards.
  - Card Layout: Image top (with 'For sale' overlay tag), Title centered, Price centered below.

## 2. Technical Decisions (Tokens & Styles - Stage 5)
### Color Palette
- **Background:** `#F9F9F9` (Very light grey for contrast against white cards).
- **Surface:** `#FFFFFF` (White cards).
- **Primary Accent (Blue):** `#2563EB` (Used for Active Tab, Submit Button, Blue Calendar Pills).
- **Secondary Accent (Outline/Text):** `#1D4ED8` (Slightly darker blue for Follow button outline and text).
- **Disabled/Inactive Fill:** `#F3F4F6` (Very light grey for Unavailable button, Inactive pills).
- **Disabled/Inactive Text:** `#9CA3AF` (Grey for Unavailable text).
- **Text Primary:** `#111827` (Dark Navy/Black for Name, Titles, Values).
- **Text Secondary:** `#6B7280` (Muted Grey for Profession, Dates, Helper text).
- **Warning/Star:** `#F59E0B` (Amber).

### Radii & Elevation
- **Large Surfaces (Hero Card, Calendar Card):** `20px` radius, flat or extremely soft `resting` shadow (`0 2px 10px rgba(0,0,0,0.03)`).
- **Buttons, Tabs & Pills:** `999px` (Full pill shape).
- **Avatar & Images:** `16px` radius (Avatar is a rounded square, not a circle).
- **Product Cards:** `12px` radius.

### Component Specs
- **Tab Bar:** Horizontal scroll row. Active tab = `#2563EB` fill, `#FFFFFF` text. Inactive = `#F9F9F9` fill (or no fill), `#6B7280` text.
- **Action Buttons (Follow / Unavailable):** `44px` height, full width of their grid column (gap `12px`).
- **Review Stars:** `24px` size icons, stroke width `1.5`, gap `8px`.
- **Calendar Pills (Sun-Sat):** ~`40x40px` rounded square/pill (`12px` radius), centered text.
- **Photo Grid:** `2-column`, `gap: 12px`, aspect ratio `1:1`.
## 3. SVG/Frontend State (Pending Stages 6 & 7)
*(To be filled when HTML is generated)*
