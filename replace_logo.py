#!/usr/bin/env python3
"""Replace old SVG navbar logo with new image logo across all HTML pages."""
import glob, re

old_logo = """<a class="navbar-brand d-flex align-items-center gap-2 text-decoration-none" href="index.html">
                <svg width="40" height="28" viewBox="0 0 70 42" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M8 12 Q 5 21 8 30" stroke="#c25e28" stroke-width="3" stroke-linecap="round" />
                    <path d="M16 8 Q 10 21 16 34" stroke="#c25e28" stroke-width="6" stroke-linecap="round" />
                    <ellipse cx="35" cy="21" rx="11" ry="16" fill="#c25e28" />
                    <path d="M54 8 Q 60 21 54 34" stroke="#c25e28" stroke-width="6" stroke-linecap="round" />
                    <path d="M62 12 Q 65 21 62 30" stroke="#c25e28" stroke-width="3" stroke-linecap="round" />
                </svg>
                <div class="d-flex flex-column align-items-start lh-1 ps-1">
                    <span class="brand-top text-white"
                        style="font-family: 'Cormorant Garamond', serif; font-weight: 600; font-size: 1.8rem; letter-spacing: -0.5px; line-height: 0.9;">harmony</span>
                    <span class="brand-bottom text-white text-uppercase"
                        style="font-family: 'Lato', sans-serif; font-size: 0.65rem; letter-spacing: 3px; font-weight: 500; margin-left: 2px;">NEUROCARE</span>
                </div>
            </a>"""

new_logo = """<a class="navbar-brand d-flex align-items-center gap-2 text-decoration-none" href="index.html">
                <div class="d-flex flex-column align-items-start lh-1 ps-1">
                    <a href="index.html" class="d-flex flex-column align-items-start text-decoration-none mb-4"
                        style="margin-left: -5px;">
                        <img src="images/logo-full1.png" alt="Harmony Neurocare Logo" class="img-fluid"
                            style="height: auto; width: 100%; max-width: 220px; object-fit: contain;">
                    </a>
                </div>
            </a>"""

files = glob.glob("/Users/sudhiryadav/Downloads/harmony-replica/*.html")
for f in sorted(files):
    with open(f, "r") as fh:
        content = fh.read()
    if old_logo in content:
        content = content.replace(old_logo, new_logo)
        with open(f, "w") as fh:
            fh.write(content)
        print(f"✅ {f.split('/')[-1]}")
    else:
        print(f"⏭️  {f.split('/')[-1]} (already updated or different format)")

print("\nDone!")
