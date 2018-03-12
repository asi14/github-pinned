import github
from pylatex import Document, Section, Subsection, Command,Itemize
from pylatex.utils import italic, NoEscape

#follow example and create latex document

def make_file():
	return github.pull_margin(30)

def github_generate(doc):
	output=make_file()
	print(output)
	with doc.create(Section('Github Projects')):
		with doc.create(Itemize()) as itemize:
			for key,values in output.items():
				print(key)
				itemize.add_item(key)	

if __name__ == '__main__':
	print('AAAAAAAAAA')
	doc=Document()
	github_generate(doc)
	doc.generate_pdf('lists',clean_tex=False)
