#!/usr/bin/env python3
"""Replace all footers across every HTML page with the canonical footer."""

import re
import os
import glob

# The canonical footer HTML (from the reference screenshot / referring-providers.html)
CANONICAL_FOOTER = '''    <!-- Footer -->
    <footer class="py-5 small" style="background-color: #2A371E !important; color: #f0ebd8;">
        <div class="container pt-5">
            <div class="row g-4 mb-2">
                <!-- Column 1: Logo & Text -->
                <div class="col-lg-4 pe-lg-4 d-flex flex-column justify-content-between">
                    <div>
                        <a href="index.html" class="d-flex flex-column align-items-start text-decoration-none mb-4"
                            style="margin-left: -5px;">
                            <img src="images/icons/footer-logo-transparent.png" alt="Harmony Neurocare Logo"
                                class="img-fluid"
                                style="height: auto; width: 100%; max-width: 280px; object-fit: contain;">
                        </a>
                        <p class="small mb-5 fst-italic"
                            style="font-size: 0.8rem; line-height: 1.6; max-width: 450px; color: #d0cbb8; font-weight: 300;">
                            Harmony Neurocare provides hope-inspired mental health care in Castle Rock, CO, offering
                            FDA-cleared TMS therapy, ketamine &amp; SPRAVATO&reg; treatments, and psychiatric support.
                            With evidence-backed therapies, a judgment-free environment, and compassionate expertise, we
                            help patients reclaim balance and find real transformation.
                        </p>
                    </div>
                    <div
                        style="font-size: 0.7rem; color: #9f9b8c; font-weight: 300; line-height: 1.8; margin-top: auto; white-space: nowrap;">
                        &copy; 2026 Harmony Neurocare in Castle Rock, CO | All Rights Reserved<br>
                        <a href="#" class="text-reset text-decoration-none hover-white">Privacy Policy</a> | <a href="#"
                            class="text-reset text-decoration-none hover-white">Terms & Conditions</a> | <a href="#"
                            class="text-reset text-decoration-none hover-white">Disclaimers</a>
                    </div>
                </div>

                <!-- Column 2: Quicklinks -->
                <div class="col-lg-2 offset-lg-1">
                    <h6 class="mb-4 text-uppercase"
                        style="color: #606C39; font-size: 0.7rem; letter-spacing: 1px; font-weight: 600;">QUICKLINKS
                    </h6>
                    <ul class="list-unstyled small d-flex flex-column gap-3"
                        style="font-size: 0.85rem; font-weight: 300; color: #e5e1d0;">
                        <li><a href="tms.html" class="text-reset text-decoration-none hover-white">What is TMS
                                Therapy?</a></li>
                        <li><a href="ketamine.html" class="text-reset text-decoration-none hover-white">How Ketamine
                                &amp; SPRAVATO&reg; Works</a></li>
                        <li><a href="#" class="text-reset text-decoration-none hover-white">Patient Portal</a></li>
                        <li><a href="referring-providers.html"
                                class="text-reset text-decoration-none hover-white">Referring Providers</a></li>
                        <li><a href="#" class="text-reset text-decoration-none hover-white">Careers</a></li>
                    </ul>
                </div>

                <!-- Column 3: Contact -->
                <div class="col-lg-2">
                    <h6 class="mb-4 text-uppercase"
                        style="color: #606C39; font-size: 0.7rem; letter-spacing: 1px; font-weight: 600;">CONTACT</h6>
                    <ul class="list-unstyled small d-flex flex-column gap-3"
                        style="font-size: 0.85rem; font-weight: 300; color: #e5e1d0;">
                        <li class="d-flex gap-2 align-items-start">
                            <i class="fa-solid fa-location-dot mt-1"
                                style="font-size: 0.8rem; color: #FFF; width: 14px; text-align: center;"></i>
                            <span style="line-height: 1.6;">757 Maleta Lane, Suite 201<br>Castle Rock, CO 80108</span>
                        </li>
                        <li class="d-flex gap-2 align-items-center mt-2">
                            <i class="fa-solid fa-phone"
                                style="font-size: 0.8rem; color: #FFF; width: 14px; text-align: center;"></i>
                            <span>Phone: 303-409-7446</span>
                        </li>
                        <li class="d-flex gap-2 align-items-center" style="margin-top: -8px;">
                            <span style="margin-left: 22px;">Fax: 303-409-7443</span>
                        </li>

                        <li class="d-flex gap-2 align-items-center mt-2">
                            <i class="fa-solid fa-envelope"
                                style="font-size: 0.8rem; color: #FFF; width: 14px; text-align: center;"></i>
                            <span>info@harmonyneurocare.com</span>
                        </li>
                    </ul>
                </div>

                <!-- Column 4: Clinic Hours -->
                <div class="col-lg-3 ps-lg-4">
                    <h6 class="mb-4 text-uppercase"
                        style="color: #606C39; font-size: 0.7rem; letter-spacing: 1px; font-weight: 600;">CLINIC HOURS
                    </h6>
                    <ul class="list-unstyled small d-flex flex-column gap-2"
                        style="font-size: 0.85rem; font-weight: 300; color: #e5e1d0;">
                        <li class="d-flex justify-content-between align-items-center mb-1">
                            <span>Mon</span>
                            <span class="flex-grow-1 mx-2" style="border-bottom: 1px dashed rgba(229, 225, 208, 0.5); height: 1px; align-self: center;"></span>
                            <span class="text-end" style="min-width: 120px; white-space: nowrap;">8:00AM - 6:00PM</span>
                        </li>
                        <li class="d-flex justify-content-between align-items-center mb-1">
                            <span>Tues</span>
                            <span class="flex-grow-1 mx-2" style="border-bottom: 1px dashed rgba(229, 225, 208, 0.5); height: 1px; align-self: center;"></span>
                            <span class="text-end" style="min-width: 120px; white-space: nowrap;">8:00AM - 6:00PM</span>
                        </li>
                        <li class="d-flex justify-content-between align-items-center mb-1">
                            <span>Wed</span>
                            <span class="flex-grow-1 mx-2" style="border-bottom: 1px dashed rgba(229, 225, 208, 0.5); height: 1px; align-self: center;"></span>
                            <span class="text-end" style="min-width: 120px; white-space: nowrap;">8:00AM - 6:00PM</span>
                        </li>
                        <li class="d-flex justify-content-between align-items-center mb-1">
                            <span>Thu</span>
                            <span class="flex-grow-1 mx-2" style="border-bottom: 1px dashed rgba(229, 225, 208, 0.5); height: 1px; align-self: center;"></span>
                            <span class="text-end" style="min-width: 120px; white-space: nowrap;">8:00AM - 6:00PM</span>
                        </li>
                        <li class="d-flex justify-content-between align-items-center mb-1">
                            <span>Fri</span>
                            <span class="flex-grow-1 mx-2" style="border-bottom: 1px dashed rgba(229, 225, 208, 0.5); height: 1px; align-self: center;"></span>
                            <span class="text-end" style="min-width: 120px; white-space: nowrap;">8:00AM - 6:00PM</span>
                        </li>
                        <li class="d-flex justify-content-between align-items-center mb-1">
                            <span>Sat</span>
                            <span class="flex-grow-1 mx-2" style="border-bottom: 1px dashed rgba(229, 225, 208, 0.5); height: 1px; align-self: center;"></span>
                            <span class="text-end" style="min-width: 120px; white-space: nowrap;">Closed</span>
                        </li>
                        <li class="d-flex justify-content-between align-items-center mb-1">
                            <span>Sun</span>
                            <span class="flex-grow-1 mx-2" style="border-bottom: 1px dashed rgba(229, 225, 208, 0.5); height: 1px; align-self: center;"></span>
                            <span class="text-end" style="min-width: 120px; white-space: nowrap;">Closed</span>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </footer>'''

def replace_footer(filepath):
    """Replace the footer in an HTML file with the canonical footer."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Match from <footer to </footer> with various possible indentation
    # Also try to capture the <!-- Footer --> comment if present
    pattern = r'(\s*<!--\s*Footer\s*-->\s*)?\s*<footer[^>]*>.*?</footer>'
    
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        print(f"  WARNING: No footer found in {filepath}")
        return False
    
    # Replace the matched footer with the canonical one
    new_content = content[:match.start()] + '\n' + CANONICAL_FOOTER + content[match.end():]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  ✓ Updated: {os.path.basename(filepath)}")
    return True

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    html_files = sorted(glob.glob(os.path.join(base_dir, '*.html')))
    
    print(f"Found {len(html_files)} HTML files")
    print("=" * 50)
    
    updated = 0
    for filepath in html_files:
        if replace_footer(filepath):
            updated += 1
    
    print("=" * 50)
    print(f"Updated {updated}/{len(html_files)} files")

if __name__ == '__main__':
    main()
