import glob
import re

new_fab_html = """<div class="fab-wrap" id="fabWrap">
  <a href="https://wa.me/919876543210" target="_blank" class="fab-item" aria-label="WhatsApp">
    <svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.6 6.32A8.86 8.86 0 0 0 12.05 4a8.94 8.94 0 0 0-7.72 13.44L4 20l2.65-.7a8.9 8.9 0 0 0 5.4 1.82h.01A8.94 8.94 0 0 0 20 12.14a8.86 8.86 0 0 0-2.4-5.82Zm-5.55 13.7h-.01a7.4 7.4 0 0 1-3.78-1.04l-.27-.16-2.8.74.75-2.73-.18-.28a7.44 7.44 0 0 1 11.65-9.2 7.36 7.36 0 0 1 2 5.06 7.44 7.44 0 0 1-7.36 7.6Zm4.08-5.55c-.22-.11-1.32-.65-1.53-.73-.2-.08-.35-.11-.5.11-.15.22-.58.73-.71.88-.13.15-.26.16-.48.05a6.1 6.1 0 0 1-1.8-1.1 6.7 6.7 0 0 1-1.24-1.54c-.13-.22 0-.34.1-.45.1-.1.22-.26.33-.4.11-.13.15-.22.22-.37.07-.15.04-.28-.02-.4-.06-.11-.5-1.2-.68-1.65-.18-.43-.36-.37-.5-.38h-.43a.82.82 0 0 0-.6.28 2.5 2.5 0 0 0-.78 1.86c0 1.1.8 2.16.91 2.31.11.15 1.57 2.4 3.8 3.36.53.23.94.37 1.27.47.53.17 1.01.14 1.4.09.43-.06 1.32-.54 1.5-1.06.19-.52.19-.96.13-1.06-.05-.09-.2-.15-.42-.26Z"/></svg>
  </a>
  <a href="tel:+919876543210" class="fab-item" aria-label="Call">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.362 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.338 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
  </a>
  <a href="https://maps.google.com/" target="_blank" class="fab-item" aria-label="Location">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
  </a>
  <a href="contact.html" class="fab-item" aria-label="Enquiry Form">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4Z"/></svg>
  </a>
  <button class="fab" id="fabBtn" aria-label="Toggle quick actions" aria-expanded="false">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
      <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2Z"/>
      <path d="m22 6-10 7L2 6"/>
    </svg>
  </button>
</div>"""

for file in glob.glob("*.html"):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace old fab-wrap div with new one
    new_content = re.sub(r'<div class="fab-wrap" id="fabWrap">.*?</div>', new_fab_html, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {file}")
