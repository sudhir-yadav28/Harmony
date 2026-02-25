#!/usr/bin/env python3
"""Fix navbar logo alignment on mobile - remove mb-4 from inner <a> tag."""
import glob

old = """<a class="navbar-brand d-flex align-items-center gap-2 text-decoration-none" href="index.html">
                <div class="d-flex flex-column align-items-start lh-1 ps-1">
                    <a href="index.html" class="d-flex flex-column align-items-start text-decoration-none mb-4"
                        style="margin-left: -5px;">
                        <img src="images/logo-full1.png" alt="Harmony Neurocare Logo" class="img-fluid"
                            style="height: auto; width: 100%; max-width: 220px; object-fit: contain;">
                    </a>
                </div>
            </a>"""

new = """<a class="navbar-brand d-flex align-items-center text-decoration-none" href="index.html">
                <img src="images/logo-full1.png" alt="Harmony Neurocare Logo" class="img-fluid"
                    style="height: auto; max-width: 220px; object-fit: contain;">
            </a>"""

files = glob.glob("/Users/sudhiryadav/Downloads/harmony-replica/*.html")
for f in sorted(files):
    with open(f, "r") as fh:
        content = fh.read()
    if old in content:
        content = content.replace(old, new)
        with open(f, "w") as fh:
            fh.write(content)
        print(f"✅ {f.split('/')[-1]}")
    else:
        print(f"⏭️  {f.split('/')[-1]}")

print("\nDone!")
