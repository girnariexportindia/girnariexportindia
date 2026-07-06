import os

html_path = r'c:\Users\hitdb\Documents\Projects\girnariexportindia\index.html'
js_path = r'c:\Users\hitdb\Documents\Projects\girnariexportindia\js\main.js'

# 1. Update HTML
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Add ID to the section
old_tag = '<section class="section" style="background-color: #FDF9F1; position: relative; overflow: hidden;">'
new_tag = '<section id="our-strengths-section" class="section" style="background-color: #FDF9F1; position: relative; overflow: hidden;">'
html = html.replace(old_tag, new_tag)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
# 2. Update JS
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace('trigger: ".strengths-pin-section",', 'trigger: "#our-strengths-section",')

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)

print("Floating issue fixed.")
