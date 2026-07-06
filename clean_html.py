import os

html_path = r'c:\Users\hitdb\Documents\Projects\girnariexportindia\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()
    
# We want to properly close `.strengths-grid` before `.strengths-pin-section`
# Looking at the file, the last card in `.strengths-grid` is "Empowering Communities"
# Let's find "Empowering Communities" and the closing tags of that card.
# Then we can replace the malformed section.

# To be completely safe, let's just find the entire section from 
# `<!-- Our Strengths Section -->` to `<!-- Stats Section -->` 
# and replace it with a clean version.

clean_section = """    <!-- Our Strengths Section -->
    <section class="section" style="background-color: #FDF9F1; position: relative; overflow: hidden;">
        <!-- Abstract background shapes -->
        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 0; pointer-events: none;">
            <svg viewBox="0 0 100 100" preserveAspectRatio="none" style="position:absolute; top:-20%; left:-10%; width:40%; height:80%; fill:none; stroke:#EAE0D5; stroke-width:0.5;"><path d="M0,50 Q25,20 50,50 T100,50" /></svg>
            <svg viewBox="0 0 100 100" preserveAspectRatio="none" style="position:absolute; top:20%; right:-10%; width:30%; height:60%; fill:#E9F0E6; opacity:0.7;"><path d="M10,0 Q50,20 80,60 T100,100 L100,0 Z" /></svg>
        </div>
        
        <div class="container" style="position: relative; z-index: 1;">
            <div class="text-center fade-in-up">
                <svg style="width:24px; height:24px; color:#5D9530; margin-bottom:15px;"><use href="#icon-leaf"></use></svg>
                <p style="text-transform:uppercase; font-size:0.8rem; font-weight:600; color:#8A6C58; letter-spacing:1px; margin-bottom:10px;">DISCOVER GIRNARI EXPORT</p>
                <h2 style="font-size:2.5rem; margin-bottom:50px; font-weight:400;">OUR STRENGTHS</h2>
            </div>
            
            <div class="strengths-grid fade-in-up delay-1 strengths-grid-mobile-fallback">
                <div class="strength-card">
                    <div class="strength-header">
                        <div class="strength-icon"><svg><use href="#icon-leaf"></use></svg></div>
                        <h3>Deep Agricultural Roots</h3>
                    </div>
                    <div class="strength-content">
                        <p>Three generations of agricultural expertise shape our onion sourcing—crafted with tradition, passion, and deep knowledge.</p>
                    </div>
                </div>
                <div class="strength-card">
                    <div class="strength-header">
                        <div class="strength-icon"><svg><use href="#icon-star"></use></svg></div>
                        <h3>Expert Processing Team</h3>
                    </div>
                    <div class="strength-content">
                        <p>Our skilled team handles every stage—from sourcing to market—with precision, care, and an unwavering focus on quality.</p>
                    </div>
                </div>
                <div class="strength-card">
                    <div class="strength-header">
                        <div class="strength-icon"><svg><use href="#icon-cog"></use></svg></div>
                        <h3>Modern Infrastructure</h3>
                    </div>
                    <div class="strength-content">
                        <p>Equipped with advanced processing technology, our facility ensures maximum efficiency, consistency, and world-class production standards.</p>
                    </div>
                </div>
                <div class="strength-card">
                    <div class="strength-header">
                        <div class="strength-icon"><svg><use href="#icon-truck"></use></svg></div>
                        <h3>Comprehensive Export Solutions</h3>
                    </div>
                    <div class="strength-content">
                        <p>We deliver end-to-end services, from custom blends to global-ready packaging, tailored perfectly to international market needs.</p>
                    </div>
                </div>
                <div class="strength-card">
                    <div class="strength-header">
                        <div class="strength-icon"><svg><use href="#icon-shield"></use></svg></div>
                        <h3>Quality Assurance</h3>
                    </div>
                    <div class="strength-content">
                        <p>Every single batch meets the highest global standards of quality, safety, and purity—independently verified and guaranteed.</p>
                    </div>
                </div>
                <div class="strength-card">
                    <div class="strength-header">
                        <div class="strength-icon"><svg><use href="#icon-price"></use></svg></div>
                        <h3>Empowering Communities</h3>
                    </div>
                    <div class="strength-content">
                        <p>We support local farming communities across Gujarat, focusing on sustainable agricultural practices and impactful, long-term initiatives.</p>
                    </div>
                </div>
            </div>

            <!-- Desktop Pinned Strengths -->
            <div class="strengths-pin-section fade-in-up delay-1">
                <div class="strengths-content">
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
                </div>
            </div>
        </div>
    </section>"""

import re
pattern = r'<!-- Our Strengths Section -->.*?<!-- Stats Section -->'
# Replace everything between those two comments
new_html = re.sub(pattern, clean_section + '\n\n    <!-- Stats Section -->', html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_html)
print("HTML successfully fixed.")
