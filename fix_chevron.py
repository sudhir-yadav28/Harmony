import re

html_file = "tms.html"

with open(html_file, "r") as f:
    content = f.read()

# Replace all variants of the FontAwesome chevron with the SVG
replacements = [
    ('<i class="fa-solid fa-chevron-down text-muted" style="font-size: 0.7rem; font-weight: 900;"></i>', 
     '''<svg width="10" height="6" viewBox="0 0 10 6" fill="none" xmlns="http://www.w3.org/2000/svg">
                                            <path d="M1 1L5 5L9 1" stroke="#6c757d" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                        </svg>'''),
    ('<i class="fas fa-chevron-down text-muted"></i>',
     '''<svg width="10" height="6" viewBox="0 0 10 6" fill="none" xmlns="http://www.w3.org/2000/svg">
                                            <path d="M1 1L5 5L9 1" stroke="#6c757d" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                        </svg>''')
]

for old, new in replacements:
    content = content.replace(old, new)

# Ensure all rounding circles have flex-shrink-0 so they don't squish
content = content.replace('<span class="bg-white rounded-circle d-flex', '<span class="bg-white rounded-circle flex-shrink-0 d-flex')

with open(html_file, "w") as f:
    f.write(content)

print("Icons fixed successfully!")
