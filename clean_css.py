import os

css_path = r'c:\Users\hitdb\Documents\Projects\girnariexportindia\css\styles.css'

with open(css_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    
# Find the line index for "/* ==========================================================================\n" that proceeds "   Strengths Pinned Section\n"
start_idx = -1
for i, line in enumerate(lines):
    if '   Strengths Pinned Section' in line:
        start_idx = i - 1
        break

if start_idx != -1:
    lines = lines[:start_idx]
    
    clean_css = """/* ==========================================================================
   Strengths Pinned Section
   ========================================================================== */
@media (min-width: 900px) {
  .strengths-pin-section {
    border-top: none;
    margin-top: 30px;
    min-height: 450px;
  }
  .strengths-content {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    padding: 0 20px;
    position: relative;
  }
  .strengths-list-wrapper {
    position: relative;
    flex-grow: 0;
    width: 40%;
  }
  .strengths-list {
    font-size: 22px;
    font-family: var(--font-heading);
    font-weight: 600;
    margin: 0;
    padding: 0 20px 0 30px;
    list-style: none;
    color: #8A6C58;
    position: relative;
    cursor: default;
  }
  .strengths-list li {
    padding: 20px 0;
    transition: color 0.3s;
  }
  .strengths-fill {
    position: absolute;
    top: 0;
    left: 0;
    width: 4px;
    height: 100%;
    background-color: #C46C49;
    border-radius: 4px;
  }
  .strengths-detail {
    flex-grow: 1;
    position: relative;
    min-height: 300px;
    width: 60%;
  }
  .strength-slide {
    position: absolute;
    top: 50%;
    left: 0;
    transform: translateY(-50%);
    opacity: 0;
    visibility: hidden;
    text-align: left;
    max-width: 500px;
  }
  .strength-slide svg {
    width: 48px;
    height: 48px;
    color: #C46C49;
    margin-bottom: 16px;
  }
  .strength-slide p {
    font-size: 18px;
    line-height: 1.6;
    color: var(--color-text);
  }
  .strengths-grid-mobile-fallback {
    display: none !important;
  }
}
@media (max-width: 899px) {
  .strengths-pin-section {
    display: none !important;
  }
}
"""
    lines.append(clean_css)
    with open(css_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print("CSS Cleaned")
else:
    print("Not found")
