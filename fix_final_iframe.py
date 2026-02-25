import re

html_file = "index.html"

with open(html_file, "r") as f:
    content = f.read()

# Iframe code using Bootstrap ratio component
old_container_pattern = re.compile(
    r'<div class="position-relative w-100 mb-5 rounded-4 overflow-hidden"[\s]*style="[^"]*">[\s]*<iframe[^>]*></iframe>[\s]*</div>'
)

# And fallback for the user's manual ratio container if it exists
old_ratio_pattern = re.compile(
    r'<div class="ratio ratio-16x9 w-100 mb-5 rounded-4 overflow-hidden"[\s]*style="[^"]*">[\s]*<iframe[^>]*></iframe>[\s]*</div>'
)

new_container = '''<div class="ratio ratio-16x9 w-100 mb-5 rounded-4 overflow-hidden" style="max-width: 480px; margin: 0 auto; background-color: #000;">
                            <iframe src="https://www.youtube.com/embed/io_ganJ0Za0?rel=0"
                                title="YouTube video player" frameborder="0"
                                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                                allowfullscreen></iframe>
                        </div>'''

content = old_container_pattern.sub(new_container, content)
content = old_ratio_pattern.sub(new_container, content)

with open(html_file, "w") as f:
    f.write(content)

print("Video iframes reset!")
