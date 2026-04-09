import re

with open('ai-hardware-pm-course.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix total pages in header
content = content.replace('当前页 <span class="current">01</span> / 08', '当前页 <span class="current">01</span> / 09')

# Let's fix up JS totalSlides if needed
# The script currently likely checks for DOM elements dynamically, but let's make sure.
with open('ai-hardware-pm-course.html', 'w', encoding='utf-8') as f:
    f.write(content)
