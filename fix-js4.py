import re

with open('ai-hardware-pm-course.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the total page number span format so that it uses the correct 09
content = content.replace('<span>/ 08</span>', '<span>/ 09</span>')

# Let's save and test again
with open('ai-hardware-pm-course.html', 'w', encoding='utf-8') as f:
    f.write(content)
