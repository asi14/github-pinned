import github
from pylatex import Document, Section, Subsection, Command,Itemize
from pylatex.utils import italic, NoEscape

#follow example and create latex document

def make_file():
	return github.pull_margin(30)

def github_generate(doc):
	output=make_file()
	with doc.create(Section('Github Projects')):
		with doc.create(Itemize()) as itemize:
			for i in range(len(output)):
				print(output[i])
				itemize.add_item(output[i])	

if __name__ == '__main__':
	print('AAAAAAAAAA')
	doc=Document()
	github_generate(doc)
	doc.generate_pdf('lists',clean_tex=False)
