with open('ai-hardware-pm-course.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('当前页 <span class="current">01</span> / 08', '当前页 <span class="current">01</span> / 09')
content = content.replace('<span class="total">08</span>', '<span class="total">09</span>')

# Fix totalSlides variable logic if hardcoded
if 'const totalSlides = 8;' in content:
    content = content.replace('const totalSlides = 8;', 'const totalSlides = 9;')

with open('ai-hardware-pm-course.html', 'w', encoding='utf-8') as f:
    f.write(content)
