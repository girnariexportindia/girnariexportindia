import os
import urllib.parse

html_path = r'c:\Users\hitdb\Documents\Projects\girnariexportindia\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

def get_img_tag(filename, alt_text):
    encoded_url = "assets/" + urllib.parse.quote(filename)
    return f'<img src="{encoded_url}" alt="{alt_text}" style="width: 100%; border-radius: 8px; margin-bottom: 20px; display: block; object-fit: cover; max-height: 200px;">'

replacements = {
    # data-index="1"
    '<div class="strength-slide" data-index="1">\n                            <svg><use href="#icon-star"></use></svg>': 
    f'<div class="strength-slide" data-index="1">\n                            {get_img_tag("ours professional.png", "Professional Team")}\n                            <svg><use href="#icon-star"></use></svg>',
    
    # data-index="2"
    '<div class="strength-slide" data-index="2">\n                            <svg><use href="#icon-cog"></use></svg>': 
    f'<div class="strength-slide" data-index="2">\n                            {get_img_tag("ours modern machinary.png", "Modern Machinery")}\n                            <svg><use href="#icon-cog"></use></svg>',
    
    # data-index="3"
    '<div class="strength-slide" data-index="3">\n                            <svg><use href="#icon-truck"></use></svg>': 
    f'<div class="strength-slide" data-index="3">\n                            {get_img_tag("ours comprehensive solution.png", "Comprehensive Solutions")}\n                            <svg><use href="#icon-truck"></use></svg>',
    
    # data-index="4"
    '<div class="strength-slide" data-index="4">\n                            <svg><use href="#icon-shield"></use></svg>': 
    f'<div class="strength-slide" data-index="4">\n                            {get_img_tag("ours quality check.png", "Quality Check")}\n                            <svg><use href="#icon-shield"></use></svg>',
    
    # data-index="5"
    '<div class="strength-slide" data-index="5">\n                            <svg><use href="#icon-price"></use></svg>': 
    f'<div class="strength-slide" data-index="5">\n                            {get_img_tag("ours community.png", "Community")}\n                            <svg><use href="#icon-price"></use></svg>'
}

for old, new in replacements.items():
    html = html.replace(old, new)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Images added to slides.")
