import os

html_path = r'c:\Users\hitdb\Documents\Projects\girnariexportindia\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

replacements = {
    "<p>Three generations of agricultural expertise shape our onion sourcing—crafted with tradition, passion, and deep knowledge.</p>": "<p>Three generations of farming expertise behind every batch we source.</p>",
    "<p>Our skilled team handles every stage—from sourcing to market—with precision, care, and an unwavering focus on quality.</p>": "<p>Skilled hands, precise process, quality at every step.</p>",
    "<p>Equipped with advanced processing technology, our facility ensures maximum efficiency, consistency, and world-class production standards.</p>": "<p>Advanced equipment for consistent, world-class output.</p>",
    "<p>We deliver end-to-end services, from custom blends to global-ready packaging, tailored perfectly to international market needs.</p>": "<p>End-to-end service, from custom blends to global-ready packaging.</p>",
    "<p>Every single batch meets the highest global standards of quality, safety, and purity—independently verified and guaranteed.</p>": "<p>Every batch tested and verified to global standards.</p>",
    "<p>We support local farming communities across Gujarat, focusing on sustainable agricultural practices and impactful, long-term initiatives.</p>": "<p>Supporting Gujarat's farmers through sustainable practices.</p>"
}

for old, new in replacements.items():
    html = html.replace(old, new)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Copy updated successfully.")
