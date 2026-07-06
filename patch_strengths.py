import os
import re

html_path = r'c:\Users\hitdb\Documents\Projects\girnariexportindia\index.html'
css_path = r'c:\Users\hitdb\Documents\Projects\girnariexportindia\css\styles.css'
js_path = r'c:\Users\hitdb\Documents\Projects\girnariexportindia\js\main.js'

# 1. Update HTML
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Add the fallback class to the existing grid
html_content = html_content.replace(
    '<div class="strengths-grid fade-in-up delay-1">',
    '<div class="strengths-grid fade-in-up delay-1 strengths-grid-mobile-fallback">'
)

new_html = """
            <!-- Desktop Pinned Strengths -->
            <div class="strengths-pin-section fade-in-up delay-1">
                <div class="strengths-content">
                    <ul class="strengths-list">
                        <li data-icon="leaf">Deep Agricultural Roots</li>
                        <li data-icon="star">Expert Processing Team</li>
                        <li data-icon="cog">Modern Infrastructure</li>
                        <li data-icon="truck">Comprehensive Export Solutions</li>
                        <li data-icon="shield">Quality Assurance</li>
                        <li data-icon="price">Empowering Communities</li>
                    </ul>
                    <div class="strengths-fill"></div>
                    <div class="strengths-detail">
                        <div class="strength-slide active" data-index="0">
                            <svg><use href="#icon-leaf"></use></svg>
                            <p>Three generations of agricultural expertise shape our onion sourcing—crafted with tradition, passion, and deep knowledge.</p>
                        </div>
                        <div class="strength-slide" data-index="1">
                            <svg><use href="#icon-star"></use></svg>
                            <p>Our skilled team handles every stage—from sourcing to market—with precision, care, and an unwavering focus on quality.</p>
                        </div>
                        <div class="strength-slide" data-index="2">
                            <svg><use href="#icon-cog"></use></svg>
                            <p>Equipped with advanced processing technology, our facility ensures maximum efficiency, consistency, and world-class production standards.</p>
                        </div>
                        <div class="strength-slide" data-index="3">
                            <svg><use href="#icon-truck"></use></svg>
                            <p>We deliver end-to-end services, from custom blends to global-ready packaging, tailored perfectly to international market needs.</p>
                        </div>
                        <div class="strength-slide" data-index="4">
                            <svg><use href="#icon-shield"></use></svg>
                            <p>Every single batch meets the highest global standards of quality, safety, and purity—independently verified and guaranteed.</p>
                        </div>
                        <div class="strength-slide" data-index="5">
                            <svg><use href="#icon-price"></use></svg>
                            <p>We support local farming communities across Gujarat, focusing on sustainable agricultural practices and impactful, long-term initiatives.</p>
                        </div>
                    </div>
                </div>
            </div>
"""

# Find the end of the strengths grid and insert the new_html
# It is right after the 6th card which ends with:
#                     </div>
#                 </div>
#             </div>
#         </div>
#     </section>
# Using regex to find the end of the grid (closing div of strengths-grid)
# Wait, let's just find "<!-- Stats Section -->" and insert before it, but inside the section?
# No, it should be in the same container.
pattern = r'(<div class="strength-card">.*?<h3>Empowering Communities</h3>.*?</div>.*?</div>\s*</div>)'
match = re.search(pattern, html_content, re.DOTALL)
if match:
    html_content = html_content[:match.end()] + "\n" + new_html + html_content[match.end():]
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("HTML updated")
else:
    print("Could not find the insertion point in HTML")

# 2. Update CSS
with open(css_path, 'a', encoding='utf-8') as f:
    f.write("""
/* ==========================================================================
   Strengths Pinned Section
   ========================================================================== */
@media (min-width: 900px) {
  .strengths-pin-section {
    border-top: none;
    margin-top: 30px;
    min-height: 450px;
  }
  .strengths-content {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    padding: 0 20px;
    position: relative;
  }
  .strengths-list {
    font-size: 22px;
    font-family: var(--font-heading);
    font-weight: 600;
    margin: 0;
    padding: 0 40px 0 20px;
    list-style: none;
    flex-grow: 0;
    color: #8A6C58;
    position: relative;
    cursor: default;
  }
  .strengths-list li {
    padding: 20px 0;
    transition: color 0.3s;
  }
  .strengths-fill {
    position: absolute;
    top: 0;
    left: 0;
    width: 4px;
    height: 100%;
    background-color: #C46C49;
    border-radius: 4px;
  }
  .strengths-detail {
    flex-grow: 1;
    position: relative;
    min-height: 300px;
  }
  .strength-slide {
    position: absolute;
    top: 50%;
    left: 2rem;
    transform: translateY(-50%);
    opacity: 0;
    visibility: hidden;
    text-align: left;
    max-width: 500px;
  }
  .strength-slide svg {
    width: 48px;
    height: 48px;
    color: #C46C49;
    margin-bottom: 16px;
  }
  .strength-slide p {
    font-size: 18px;
    line-height: 1.6;
    color: var(--color-text);
  }
  .strengths-grid-mobile-fallback {
    display: none !important;
  }
}
@media (max-width: 899px) {
  .strengths-pin-section {
    display: none !important;
  }
}
""")
print("CSS updated")

# 3. Update JS
js_code = """

// --- Pinned Strengths Animation ---
if (window.innerWidth >= 900) {
  if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
      gsap.registerPlugin(ScrollTrigger);

      const list = document.querySelector(".strengths-list");
      const fill = document.querySelector(".strengths-fill");
      if (list && fill) {
          const listItems = gsap.utils.toArray("li", list);
          const slides = gsap.utils.toArray(".strength-slide");

          const tl = gsap.timeline({
            scrollTrigger: {
              trigger: ".strengths-pin-section",
              start: "center center",
              end: "+=" + listItems.length * 50 + "%",
              pin: true,
              scrub: true
            }
          });

          gsap.set(fill, { scaleY: 1 / listItems.length, transformOrigin: "top left" });

          listItems.forEach((item, i) => {
            const previousItem = listItems[i - 1];
            if (previousItem) {
              tl.set(item, { color: "#C46C49" }, 0.5 * i)
                .to(slides[i], { autoAlpha: 1, duration: 0.2 }, "<")
                .set(previousItem, { color: "#8A6C58" }, "<")
                .to(slides[i - 1], { autoAlpha: 0, duration: 0.2 }, "<");
            } else {
              gsap.set(item, { color: "#C46C49" });
              gsap.set(slides[i], { autoAlpha: 1 });
            }
          });

          tl.to(fill, { scaleY: 1, transformOrigin: "top left", ease: "none", duration: tl.duration() }, 0)
            .to({}, {});
      }
  }
}
"""

with open(js_path, 'a', encoding='utf-8') as f:
    f.write(js_code)

print("JS updated")
