with open('ai-hardware-pm-course.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('<span>/ 08</span>', '<span>/ 09</span>')

with open('ai-hardware-pm-course.html', 'w', encoding='utf-8') as f:
    f.write(content)
