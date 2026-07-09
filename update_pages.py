import re
import os

files = ['products.html', 'white-onion-powder.html', 'pink-onion-powder.html', 'red-onion-powder.html']

with open('extracted_header.html', 'r', encoding='utf-8') as f:
    header_html = f.read()

with open('extracted_footer.html', 'r', encoding='utf-8') as f:
    footer_html = f.read()

css_tags = '''
<link rel="stylesheet" href="css/styles.min.css">
<link rel="stylesheet" href="css/responsive.css">
'''

js_tags = '''
<div id="svg-sprite-container" style="display: none;"></div>
<script>
    fetch('assets/icons.svg')
        .then(response => response.text())
        .then(svg => document.getElementById('svg-sprite-container').innerHTML = svg);
</script>
<script defer src="js/main.min.js"></script>
'''

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace nav
    content = re.sub(r'<nav.*?</nav>', header_html, content, flags=re.DOTALL)
    
    # Replace footer
    content = re.sub(r'<footer.*?</footer>', footer_html, content, flags=re.DOTALL)
    
    # Inject CSS
    if 'css/styles.min.css' not in content:
        content = content.replace('</head>', css_tags + '\n</head>')
        
    # Inject JS
    if 'svg-sprite-container' not in content:
        content = content.replace('</body>', js_tags + '\n</body>')
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated {file}')

