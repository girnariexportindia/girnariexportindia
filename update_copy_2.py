import os

html_path = r'c:\Users\hitdb\Documents\Projects\girnariexportindia\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

replacements = {
    "<p>Three generations of farming expertise behind every batch we source.</p>": "<p>Three generations of agricultural expertise shape our onion sourcing.</p>",
    "<p>Skilled hands, precise process, quality at every step.</p>": "<p>Our team handles every stage, from sourcing to market, with care and precision.</p>",
    "<p>Advanced equipment for consistent, world-class output.</p>": "<p>Advanced processing technology for efficient, consistent production.</p>",
    "<p>End-to-end service, from custom blends to global-ready packaging.</p>": "<p>End-to-end services, from custom blends to global-ready packaging.</p>",
    "<p>Every batch tested and verified to global standards.</p>": "<p>Every batch meets global standards of quality, safety, and purity.</p>",
    "<p>Supporting Gujarat's farmers through sustainable practices.</p>": "<p>Supporting local farming communities across Gujarat through sustainable practices.</p>"
}

for old, new in replacements.items():
    html = html.replace(old, new)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Copy updated successfully again.")
