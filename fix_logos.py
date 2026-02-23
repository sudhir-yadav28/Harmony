import os
import glob
import re

html_files = glob.glob('*.html')

header_svg = """<svg width="60" height="42" viewBox="0 0 70 42" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M8 12 Q 5 21 8 30" stroke="#c25e28" stroke-width="3" stroke-linecap="round" />
                    <path d="M16 8 Q 10 21 16 34" stroke="#c25e28" stroke-width="6" stroke-linecap="round" />
                    <ellipse cx="35" cy="21" rx="11" ry="16" fill="#c25e28" />
                    <path d="M54 8 Q 60 21 54 34" stroke="#c25e28" stroke-width="6" stroke-linecap="round" />
                    <path d="M62 12 Q 65 21 62 30" stroke="#c25e28" stroke-width="3" stroke-linecap="round" />
                </svg>
                <div class="d-flex flex-column align-items-start lh-1 ps-1">
                    <span class="brand-top text-white" style="font-family: 'Cormorant Garamond', serif; font-weight: 600; font-size: 2.2rem; letter-spacing: -1px; line-height: 0.9;">harmony</span>
                    <span class="brand-bottom text-white text-uppercase" style="font-family: 'Lato', sans-serif; font-size: 0.75rem; letter-spacing: 4px; font-weight: 500; margin-left: 2px;">NEUROCARE</span>
                </div>"""

footer_svg = """<svg width="40" height="28" viewBox="0 0 70 42" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M8 12 Q 5 21 8 30" stroke="#c25e28" stroke-width="3" stroke-linecap="round" />
                            <path d="M16 8 Q 10 21 16 34" stroke="#c25e28" stroke-width="6" stroke-linecap="round" />
                            <ellipse cx="35" cy="21" rx="11" ry="16" fill="#c25e28" />
                            <path d="M54 8 Q 60 21 54 34" stroke="#c25e28" stroke-width="6" stroke-linecap="round" />
                            <path d="M62 12 Q 65 21 62 30" stroke="#c25e28" stroke-width="3" stroke-linecap="round" />
                        </svg>
                        <div class="d-flex flex-column align-items-start lh-1 ps-1">
                            <span class="brand-top text-white" style="font-family: 'Cormorant Garamond', serif; font-weight: 600; font-size: 1.8rem; letter-spacing: -0.5px; line-height: 0.9;">harmony</span>
                            <span class="brand-bottom text-white text-uppercase" style="font-family: 'Lato', sans-serif; font-size: 0.65rem; letter-spacing: 3px; font-weight: 500; margin-left: 2px;">NEUROCARE</span>
                        </div>"""

for filepath in html_files:
    with open(filepath, 'r') as f:
        content = f.read()

    # Replace header logo
    content = re.sub(
        r'<img\s+src="images/icons/image.png"[^>]*class="logo-img"[^>]*>',
        header_svg,
        content,
        flags=re.IGNORECASE | re.DOTALL
    )

    # Replace footer logo
    content = re.sub(
        r'<img\s+src="images/icons/image.png"[^>]*class="logo-footer-img"[^>]*>',
        footer_svg,
        content,
        flags=re.IGNORECASE | re.DOTALL
    )

    with open(filepath, 'w') as f:
        f.write(content)

print(f"Updated {len(html_files)} HTML files.")
