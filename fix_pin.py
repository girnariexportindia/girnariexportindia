import os
import re

html_path = r'c:\Users\hitdb\Documents\Projects\girnariexportindia\index.html'
css_path = r'c:\Users\hitdb\Documents\Projects\girnariexportindia\css\styles.css'
js_path = r'c:\Users\hitdb\Documents\Projects\girnariexportindia\js\main.js'

# 1. Update HTML
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the pinned section content
new_html_content = """                <div class="strengths-content">
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
                    
                    <div class="strengths-list-wrapper">
                        <div class="strengths-fill"></div>
                        <ul class="strengths-list">
                            <li data-icon="leaf">Deep Agricultural Roots</li>
                            <li data-icon="star">Expert Processing Team</li>
                            <li data-icon="cog">Modern Infrastructure</li>
                            <li data-icon="truck">Comprehensive Export Solutions</li>
                            <li data-icon="shield">Quality Assurance</li>
                            <li data-icon="price">Empowering Communities</li>
                        </ul>
                    </div>
                </div>"""

pattern = r'<div class="strengths-content">.*?</div>\s*</div>\s*</div>'
html = re.sub(pattern, new_html_content + '\n            </div>\n        </div>', html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
# 2. Update JS
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace('start: "center center",', 'start: "top top",')

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)
    
# 3. Update CSS
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('.strengths-fill {\n    position: absolute;\n    top: 0;\n    left: 0;\n    width: 4px;\n    height: 100%;\n    background-color: #C46C49;\n    border-radius: 4px;\n  }',
                  '.strengths-fill {\n    position: absolute;\n    top: 0;\n    left: 0;\n    width: 4px;\n    height: 100%;\n    background-color: #C46C49;\n    border-radius: 4px;\n  }')

# Add new wrapper css and fix positions
css_patch = """
  .strengths-list-wrapper {
    position: relative;
    flex-grow: 0;
    width: 40%;
  }
  .strengths-list {
    padding: 0 20px 0 30px;
  }
"""

if '.strengths-list-wrapper {' not in css:
    css = css.replace('.strengths-list {', css_patch + '\n  .strengths-list {')
    
# Fix detail width and slide left
css = css.replace('.strengths-detail {\n    flex-grow: 1;\n    position: relative;\n    min-height: 300px;\n  }',
                  '.strengths-detail {\n    flex-grow: 1;\n    position: relative;\n    min-height: 300px;\n    width: 60%;\n  }')
css = css.replace('left: 2rem;', 'left: 0;')

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Updates applied.")
