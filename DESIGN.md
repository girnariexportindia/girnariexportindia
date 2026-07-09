# Girnari Export - Design System

## 1. Brand Guidelines
Girnari Export uses a premium, natural, and highly professional aesthetic. The theme is built around earthy greens and creams to signify agriculture and purity, sharply contrasted with a vibrant neon green for primary calls to action. The interface relies on soft shadows, rounded corners, and smooth micro-interactions (like hover lifts) to feel modern and dynamic.

## 2. Color Palette
- **Primary Color:** `#2E4A35` (Deep Forest Green) - Used for primary headings, footer background, and strong contrast elements.
- **Secondary Color:** `#FDFBF7` (Soft Cream) - Used for section backgrounds to provide a warm, earthy feel.
- **Accent Color:** `#39FF14` (Neon Green) - **STRICTLY RESERVED** for primary Call-To-Action (CTA) buttons, important links, and active states.
- **Text Primary:** `#333333` - Main body text.
- **Text Secondary:** `#4B5563` - Subtitles, descriptions, and less emphasized text.
- **Surface / Card Background:** `#FFFFFF` (Pure White) - Used for cards and floating elements to stand out against the cream background.

## 3. Typography
- **Heading Font:** `Syne`, sans-serif
  - H1: 2.5rem (40px), Bold (700)
  - H2: 2rem (32px), Semi-Bold (600)
  - H3: 1.5rem (24px), Medium (500)
- **Body Font:** `Inter`, sans-serif
  - Body Large: 1.1rem (18px), Regular (400)
  - Body Default: 1rem (16px), Regular (400)
  - Body Small: 0.875rem (14px), Regular (400)

## 4. Shadows & Elevation
- **Card Shadow (Default):** `0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)`
- **Card Shadow (Hover/Lift):** `0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)`

## 5. Spacing & Layout
- **Container Max-Width:** 1200px
- **Section Padding:** 50px vertical (`pt-50`, `pb-50`), with 150px top padding for Hero sections (`pt-150`).
- **Grid Gap:** 30px (used heavily in 3-column product/certification grids)
- **Border Radius:** `12px` for all cards and images; `8px` for buttons.

## 6. Components

### Buttons
- **Primary CTA:** 
  - Background: `#39FF14`
  - Text Color: `#000000` (for contrast)
  - Border Radius: `8px`
  - Padding: `12px 24px`
  - Font Weight: 600 (Semi-bold)
  - Hover: Slight scale up (`transform: scale(1.05)`) or brightness increase.
- **Secondary Links:**
  - Color: `#2E4A35` with an underline or arrow icon (`&rarr;`)
  - Font Weight: 600
  - Hover: Color shifts to `#39FF14`

### Product & Certification Cards
- Background: `#FFFFFF`
- Border: `1px solid rgba(0,0,0,0.05)`
- Top Accent Border (Optional for emphasis): `4px solid #39FF14`
- Border Radius: `12px`
- Padding: `30px` (internal content padding)
- **Interaction (Hover Lift):** On hover, the card should translate up by 8px (`transform: translateY(-8px)`) and the shadow should expand to the "Hover/Lift" Shadow defined above. Transition duration should be `0.3s ease`.

### Animations
- **Entrance:** Elements should use a `fade-in-up` animation when scrolling into view. (Opacity transitions from 0 to 1, TranslateY transitions from 20px to 0px).
