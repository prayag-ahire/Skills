# ProWorker - Technical & Design Decisions

## 1. Technology Stack
- **Customer App:** Flutter
- **Worker App:** React Native (without Expo)
- **Backend Runtime:** Node.js (TypeScript)
- **Framework & ORM:** Express + Prisma
- **Database & Cache:** PostgreSQL + Redis
- **Auth:** JWT
- **Realtime & Calling:** WebSocket + WebRTC
- **Storage:** S3 / R2
- **Web/SEO Pages:** Astro (Static generation / SSR)

## 2. WebRTC Architecture
- **Optimization:** To save bandwidth, ringback tones are NOT transmitted over WebRTC. The calling device plays a local custom tone until connected.
- **Incoming Calls:** Trigger the native phone ringtone.
- **Future:** Push notifications to wake the app; foreground service only active during the call.

## 3. UI/UX Design System (AI Decisions)
- **Grid System:** Strict 8pt spacing grid.
- **Safe Area:** 80-100px top margin reserved for the Dynamic Island to prevent overlap.
- **Typography:** Modern Sans-serif.
- **Corners & Radii:** 
  - App interface wrapper: 40px radius.
  - Cards: 20px radius (`md`/`lg`).
  - Buttons/Icons: Full rounding (`rx=50%`) for avatars and pills.
- **Device Frame (For Mockups):** 
  - Color: `#111111` (Black)
  - Hardware Buttons: `#333333`
  - Bezel thickness: 8-10px gap between outer frame and inner screen.
  - Shadow: SVG native `feDropShadow` applied directly to the device frame.
  - Notch: Modern floating Dynamic Island (`y=11`, `width=123`, `height=35`, `rx=17.5`).

## 4. Layout Architecture Decisions
- **Hero Sections:** Large edge-to-edge images taking up ~35% of the screen height.
- **Metadata Compression:** Instead of multiple floating pills, metadata is merged into single readable strings (e.g., `Plumber • 4.8 ★ • 0.8 km`) to reduce cognitive overload.
- **Text & Icon Alignment:** SVG icons (`<use>`) placed next to text are given negative `y` coordinates (e.g., `y="-22"`) to align perfectly with the SVG text baseline.
