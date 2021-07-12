import markdown

with open('README.md', 'r') as f:
	text = f.read()
	html = markdown.markdown(text)

with open('index.html', 'w') as f:
	f.write(html)