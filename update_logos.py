import os
import re

html_dir = '/Users/sudhiryadav/Downloads/harmony-replica'
files = [f for f in os.listdir(html_dir) if f.endswith('.html')]

# The footer logo block has an SVG of width="40" and height="28" followed by a div with the text harmony TMS & MENTAL WELLNESS CENTER
footer_regex = re.compile(
    r'<svg width="40" height="28".*?</svg>\s*<div class="d-flex flex-column align-items-start[^>]*>.*?</div>',
    re.DOTALL
)

# Wait we must also replace the header logo if it was missed in contact.html or referring-providers.html etc.
header_regex = re.compile(
    r'<svg width="60" height="42".*?</svg>\s*<div class="d-flex flex-column align-items-start[^>]*>.*?</div>',
    re.DOTALL
)

replacement = '<img src="images/icons/image.png" alt="Harmony Neurocare" class="logo-img" style="height: 40px; width: auto;">'

for f in files:
    filepath = os.path.join(html_dir, f)
    with open(filepath, 'r') as file:
        content = file.read()
    
    new_content = header_regex.sub(replacement, content)
    
    # for footer, we might want a slightly different class or style, but the prompt says "use this logo in every section".
    # We will use logo-footer-img or just logo-img.
    footer_replacement = '<img src="images/icons/image.png" alt="Harmony Neurocare" class="logo-footer-img" style="height: 50px; width: auto;">'
    new_content = footer_regex.sub(footer_replacement, new_content)
    
    if new_content != content:
        with open(filepath, 'w') as file:
            file.write(new_content)
        print(f"Updated {f}")

