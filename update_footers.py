import os

new_footer = """    <!-- Footer -->
    <footer class="site-footer">
        <div class="container footer-grid" style="display: grid !important; grid-template-columns: 1.2fr 1fr 1fr 1fr !important; gap: 40px !important; align-items: start !important; overflow-x: auto !important;">
            <!-- Column 1: Company Profile -->
            <div class="footer-col">
                <h3>Company Profile</h3>
                <p>Welcome to GIRNARI EXPORT.<br>We feel proud to introduce ourselves as leading Manufacturer, supplier and exporter of dehydrated Onions, Garlic, Ginger, Fried onions, Fried garlic, Vegetables powder, fruits powder, Indian spices, seasoning masala and instant soup premix and many more.....</p>
                <div class="footer-socials">
                    <a href="#" aria-label="Facebook"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg></a>
                    <a href="#" aria-label="YouTube"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33 2.78 2.78 0 0 0 1.94 2c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.33 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02" fill="white"></polygon></svg></a>
                    <a href="#" aria-label="WhatsApp"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M20.5 3.5C18.2 1.2 15.2 0 12 0 5.4 0 0 5.4 0 12c0 2.1.5 4.1 1.5 6L0 24l6.1-1.6c1.9 1 3.9 1.5 6 1.5 6.6 0 12-5.4 12-12 0-3.2-1.2-6.2-3.6-8.4zm-8.5 18c-1.8 0-3.5-.5-5-1.4l-.4-.2-3.7 1 1-3.6-.3-.4C2.5 15.5 2 13.8 2 12 2 6.5 6.5 2 12 2s10 4.5 10 10-4.5 10-10 10zm5.5-7.5c-.3-.1-1.8-.9-2.1-1-.3-.1-.5-.1-.7.1-.2.3-.8 1-1 1.2-.2.2-.4.3-.7.1-1.1-.6-2.1-1.3-3-2.2-.7-.7-1.1-1.5-1.4-2.4-.1-.3 0-.4.2-.6.2-.1.3-.3.5-.5.1-.2.2-.3.4-.5.1-.2 0-.4 0-.5-.1-.3-.7-1.7-.9-2.3-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.1 1.1-1.1 2.7 0 1.6 1.1 3.1 1.3 3.3.2.2 2.3 3.5 5.5 4.9 2.2.9 3.1.9 4 1 .8.1 1.8-.4 2.1-.9.3-.5.3-1 .2-1.1-.1-.1-.3-.2-.6-.4z"></path></svg></a>
                    <a href="#" aria-label="Instagram"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg></a>
                </div>
            </div>
            
            <!-- Column 2: Explore -->
            <div class="footer-col">
                <h3>Explore</h3>
                <ul class="footer-list">
                    <li>Dehydrated White Onions</li>
                    <li>Dehydrated Pink Onions</li>
                    <li>Dehydrated Red Onions</li>
                    <li>Fried Onion</li>
                    <li>Dehydrated Garlic</li>
                    <li>Fried Garlic</li>
                    <li>Vegetables Powder</li>
                </ul>
            </div>
            
            <!-- Column 3: Quick Links -->
            <div class="footer-col">
                <h3>Quick Links</h3>
                <ul class="footer-list">
                    <li><a href="index.html">Home</a></li>
                    <li><a href="about.html">About Us</a></li>
                    <li><a href="products.html">Products</a></li>
                    <li><a href="certifications.html">Quality</a></li>
                    <li><a href="contact.html">Contact Us</a></li>
                </ul>
            </div>
            
            <!-- Column 4: Connect Now -->
            <div class="footer-col" style="min-width: 0;">
                <h3>Connect Now</h3>
                <p>Feel free to get in touch with us</p>
                <form class="footer-form">
                    <div style="display: flex; gap: 8px; margin-bottom: 10px;">
                        <select class="country-code" style="width: 38%; padding: 8px; border: 1px solid rgba(0,0,0,0.1); border-radius: 4px; font-size: 14px; background: #fff; color: #333; outline: none; cursor: pointer;">
                            <option value="+91" data-len="10">🇮🇳 +91</option>
                            <option value="+1" data-len="10">🇺🇸 +1</option>
                            <option value="+44" data-len="10">🇬🇧 +44</option>
                            <option value="+971" data-len="9">🇦🇪 +971</option>
                            <option value="+61" data-len="9">🇦🇺 +61</option>
                            <option value="" data-len="15">🌐 Other</option>
                        </select>
                        <input type="text" placeholder="Phone" class="phone-input" style="width: 62% !important; margin-bottom: 0 !important; box-sizing: border-box !important;">
                    </div>
                    <input type="email" placeholder="Email" class="email-input" style="width: 100% !important; box-sizing: border-box !important;">
                    <button type="submit" style="width: 100% !important; box-sizing: border-box !important;">Send message</button>
                </form>
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
