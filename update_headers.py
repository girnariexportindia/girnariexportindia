import os
import re

html_files = [
    'index.html',
    'products.html',
    'about.html',
    'certifications.html',
    'contact.html'
]

new_header = """    <!-- Navigation Bar -->
    <header class="site-header" id="header">
        <div class="container nav-container">
            <!-- Left: Logo Badge -->
            <a href="index.html" class="logo-badge-container" aria-label="Home">
                <div class="logo-badge">
                    <span class="logo-letter">G</span>
                </div>
            </a>
            
            <!-- Center/Right: Two tiers -->
            <div class="nav-content">
                <div class="nav-top">
                    <ul class="secondary-links">
                        <li><a href="#">CSR</a></li>
                        <li><a href="#">Blog</a></li>
                    </ul>
                    <div class="social-links-nav">
                        <a href="#" aria-label="Facebook"><svg><use href="#icon-facebook"></use></svg></a>
                        <a href="#" aria-label="Instagram"><svg><use href="#icon-instagram"></use></svg></a>
                        <a href="#" aria-label="LinkedIn"><svg><use href="#icon-linkedin"></use></svg></a>
                    </div>
                </div>
                <nav class="main-nav" id="main-nav">
                    <ul class="nav-links">
                        <li><a href="index.html">HOME</a></li>
                        <li><a href="about.html">ABOUT</a></li>
                        <li><a href="products.html">PRODUCTS</a></li>
                        <li><a href="certifications.html">CERTIFICATIONS</a></li>
                        <li><a href="contact.html">CONTACT</a></li>
                    </ul>
                </nav>
            </div>

            <!-- Far Right: Button -->
            <div class="nav-action">
                <a href="contact.html" class="btn nav-btn">INQUIRE NOW</a>
                <button class="menu-toggle" id="menu-toggle" aria-label="Toggle Menu">
                    <svg width="24" height="24"><use href="#icon-menu"></use></svg>
                </button>
            </div>
        </div>
    </header>"""

for file in html_files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Use regex to find and replace the entire header block
        pattern = re.compile(r'<!-- Navigation Bar -->.*?</header>', re.DOTALL)
        new_content = pattern.sub(new_header, content)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
