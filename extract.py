import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

header_match = re.search(r'<header class=\"site-header\" id=\"header\">.*?</header>', content, re.DOTALL)
footer_match = re.search(r'<footer class=\"site-footer\">.*?</footer>', content, re.DOTALL)

with open('extracted_header.html', 'w', encoding='utf-8') as f:
    f.write(header_match.group(0))

with open('extracted_footer.html', 'w', encoding='utf-8') as f:
    f.write(footer_match.group(0))

print('Extracted')
