# Girnari Export - Project Context & Documentation

This file serves as a persistent context guide for future AI agents and developers working on this repository. It tracks how the codebase is structured, how it works, and the historical optimizations that have been applied.

## 1. Project Architecture

This is a **pure static website** built with HTML, CSS, and JavaScript. 
- **No Templating Engine:** There is no build step for the HTML (like Next.js, Hugo, or PHP). This means that common UI elements like the Navigation Header, Footer, and Floating Action Button (FAB) are hardcoded into every individual `.html` file. Any structural changes to these components must be manually duplicated across all HTML files.
- **Hosting:** The site is designed to be hosted on static platforms like GitHub Pages.

## 2. Asset Pipeline & Guidelines

**CSS & JavaScript:**
- **Development Files:** `css/styles.dev.css` and `js/main.dev.js` are the source of truth for development. Edit these files when making changes.
- **Production Files:** `css/styles.min.css` and `js/main.min.js` are the files actually referenced by the HTML. 
- *Rule:* If you modify a `.dev.` file, you **must** re-minify it to update the `.min.` version so the changes reflect on the site.

**Images:**
- Avoid raw PNGs/JPEGs if possible. The site uses heavily optimized `WebP` images to maintain fast load times.
- All decorative/layout images below the fold must have `loading="lazy"` attributes.
- Always include explicit `width` and `height` attributes (representing the aspect ratio/display size) to prevent Cumulative Layout Shift (CLS).

## 3. Caching Rules

- **Do NOT use query strings for cache busting** (e.g., `css/styles.min.css?v=1.1`). 
- GitHub Pages automatically handles caching via ETags. Adding query strings can break the CDN caching behavior.

## 4. History of Changes & Optimizations

*July 2026 - Major Performance & Cleanup Pass*

1. **Payload Reduction:** Discovered six 5MB+ PNG files being used in the "Our Strengths" section, scaled down via HTML. Converted all to highly optimized WebP format (saving ~29MB of payload) and added explicit width/height matching their CSS max-height constraints (250px-300px).
2. **Lazy Loading:** Enforced `loading="lazy"` on all below-the-fold images across the site.
3. **Asset Minification:** Implemented the `.dev.` vs `.min.` separation for CSS and JS to significantly reduce file sizes on production while keeping code editable.
4. **Caching Fix:** Stripped `?v=1.1` from all asset references across HTML files to allow GitHub Pages ETags to function correctly.
5. **404 Page:** Created a custom `404.html` that inherits the main site's header and footer.
6. **Repository Cleanup:** Deleted 15+ one-off python development scripts (`update_headers.py`, `add_images.py`, etc.) and `.patch` files that were cluttering the root.
7. **Gitignore:** Added a strict `.gitignore` to prevent future python cache files, scratch scripts, or diffs from being committed.
