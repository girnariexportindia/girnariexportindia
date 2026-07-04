import os

new_footer = """    <!-- Footer -->
    <footer class="site-footer">
        <div class="container footer-grid">
            <div class="footer-col contact-col">
                <img src="images/logo.png" alt="Girnari Export Logo" style="height: 180px; width: auto; margin-bottom: 20px; transform: scale(1.2); transform-origin: left center;">
                <h3>CONTACT</h3>
                <p>Girnari Export,<br>
                Ahmedabad,<br>
                Gujarat, India.</p>
                <a href="#" class="get-directions"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 8px; vertical-align: text-bottom;"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>Get Directions</a>
                
                <div class="contact-details mt-20">
                    <p>PHONE : (+91) 98765 43210</p>
                    <p>EMAIL : info@girnariexport.com</p>
                </div>
            </div>
            
            <div class="footer-col business-col">
                <h3>BUSINESS HOURS</h3>
                <div class="business-hours mb-30">
                    <p>09:00 A.M. TO 5:00 P.M<br><span>Monday to Friday</span></p>
                    <p class="mt-15">09:00 A.M. TO 2:00 P.M<br><span>Alternate Saturdays</span></p>
                </div>
                
                <h3>FOLLOW US</h3>
                <div class="social-links">
                    <a href="#" aria-label="Facebook"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg></a>
                    <a href="#" aria-label="Instagram"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg></a>
                    <a href="#" aria-label="YouTube"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33 2.78 2.78 0 0 0 1.94 2c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.33 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02" fill="white"></polygon></svg></a>
                    <a href="#" aria-label="LinkedIn"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg></a>
                </div>
                
                <div class="footer-bottom-links mt-20">
                    <a href="#">Sitemap</a> | <a href="#">Privacy Policy</a>
                </div>
            </div>
            
            <div class="footer-col links-col">
                <h3>QUICK LINKS</h3>
                <ul>
                    <li><a href="index.html">Home</a></li>
                    <li><a href="about.html">About</a></li>
                    <li><a href="#">Services</a></li>
                    <li><a href="certifications.html">Certifications</a></li>
                    <li><a href="#">Careers</a></li>
                    <li><a href="#">FAQ</a></li>
                    <li><a href="#">News & Events</a></li>
                    <li><a href="#">Blog</a></li>
                    <li><a href="contact.html">Contact</a></li>
                </ul>
            </div>
        </div>
    </footer>"""

def update_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        import re
        # Find everything from <!-- Footer --> to </footer>
        pattern = re.compile(r'<!-- Footer -->.*?</footer>', re.DOTALL)
        
        if not pattern.search(content):
            print(f"Footer block not found in {filepath}")
            return
            
        new_content = pattern.sub(new_footer, content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print(f"Successfully updated {filepath}")
        
    except Exception as e:
        print(f"Error updating {filepath}: {e}")

if __name__ == "__main__":
    directory = "."
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            filepath = os.path.join(directory, filename)
            update_file(filepath)
