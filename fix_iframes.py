import re

html_file = "index.html"

with open(html_file, "r") as f:
    content = f.read()

# Replace all youtube domains in the iframes
old_iframe = '''<iframe class="w-100 h-100" src="https://www.youtube.com/embed/WGqTDxMjtN0"
                                title="YouTube video player" frameborder="0"
                                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                                allowfullscreen></iframe>'''

new_iframe = '''<iframe class="w-100 h-100" src="https://www.youtube-nocookie.com/embed/WGqTDxMjtN0?rel=0&amp;modestbranding=1"
                                title="YouTube video player" frameborder="0"
                                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                                referrerpolicy="strict-origin-when-cross-origin"
                                allowfullscreen></iframe>'''

content = content.replace(old_iframe, new_iframe)

with open(html_file, "w") as f:
    f.write(content)

print("All iframes fixed!")
