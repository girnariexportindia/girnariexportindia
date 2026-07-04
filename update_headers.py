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
            <a href="index.html" class="logo-container flex-center-gap-15" aria-label="Home">
                <img src="images/logo.png" alt="Girnari Export Logo" style="height: 85px; width: auto; transform: scale(1.5); transform-origin: left center;">
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
                        <a href="#" aria-label="YouTube"><svg><use href="#icon-youtube"></use></svg></a>
                        <a href="#" aria-label="LinkedIn"><svg><use href="#icon-linkedin"></use></svg></a>
                    </div>
                </div>
                <nav class="main-nav" id="main-nav">
                    <ul class="nav-links">
                        <li><a href="index.html">HOME</a></li>
                        <li><a href="about.html">ABOUT</a></li>
                        <li class="dropdown">
                            <a href="#">SERVICES <svg width="10" height="6" viewBox="0 0 10 6" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-left: 4px; display: inline-block; vertical-align: middle; transform: translateY(-1px);"><path d="M1 1L5 5L9 1" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
                            <ul class="dropdown-menu">
                                <li><a href="#">Service 1</a></li>
                                <li><a href="#">Service 2</a></li>
                            </ul>
                        </li>
                        <li><a href="certifications.html">CERTIFICATIONS</a></li>
                        <li><a href="#">CAREERS</a></li>
                        <li><a href="#">NEWS & EVENTS</a></li>
                        <li><a href="#">FAQ</a></li>
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
