import os

file_path = r'c:\Users\hitdb\Documents\Projects\girnariexportindia\css\styles.css'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    new_lines.append(line)
    if '.cta-btn:hover {' in line:
        # The next line is '    background-color: #26130b;\n'
        # Then there's an empty line and then '.site-footer a:hover {'
        pass

# Since the file has been messed up, let's just find the exact index of '.cta-btn:hover {'
idx = -1
for i, line in enumerate(lines):
    if '.cta-btn:hover {' in line:
        idx = i
        break

if idx != -1:
    # Delete from idx+1 to the line before '.site-footer a:hover {'
    end_idx = -1
    for i in range(idx+1, len(lines)):
        if '.site-footer a:hover {' in lines[i]:
            end_idx = i
            break
    
    if end_idx != -1:
        del lines[idx:end_idx]
        
        insert_text = """.cta-btn:hover {
    background-color: #26130b;
    color: var(--color-white);
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(44, 24, 16, 0.3);
}

@media (max-width: 991px) {
    .contact-cta-card {
        flex-direction: column;
    }
    
    .contact-cta-image {
        min-height: 300px;
    }
    
    .contact-cta-content {
        padding: 50px 30px;
    }
}

/* ==========================================================================
   Footer Section
   ========================================================================== */
.site-footer {
    background-color: #EBE3D5; /* Light beige from image */
    padding: 70px 0 0px;
    color: var(--color-text-light);
    font-size: 0.95rem;
    line-height: 1.8;
    overflow: hidden;
}

.site-footer .footer-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 40px;
    padding-bottom: 0px;
}

.site-footer h3 {
    font-size: 0.95rem;
    font-weight: 500;
    color: #4A2B1D;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 25px;
}

.site-footer p {
    color: #7A6355;
    margin-bottom: 15px;
}

.site-footer a {
    color: #7A6355;
    text-decoration: none;
    transition: var(--transition);
}

"""
        lines.insert(idx, insert_text)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        print("Fixed styles.css")
    else:
        print("Could not find end index")
else:
    print("Could not find start index")
