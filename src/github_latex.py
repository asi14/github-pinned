import github
from pylatex import Document, Section, Subsection, Command,Itemize
from pylatex.utils import italic, NoEscape

#follow example and create latex document

def make_file():
	return github.pull_margin(30)

def github_generate(doc):
	output=make_file()
	with doc.create(Section('Github Projects')):
		for key,values in output.items():
			with doc.create(Itemize()) as itemize:
				itemize.add_item(key)	
				print(key)
				with doc.create(Itemize()) as itemize:
					print(output[key]['description'])
					itemize.add_item('Description:' + output[key]['description'])
					language = 'Languages: '
					for lang in output[key]['languages']:
						language+=lang + ', '
					itemize.add_item(language)


if __name__ == '__main__':
	print('AAAAAAAAAA')
	doc=Document()
	github_generate(doc)
	doc.generate_pdf('lists',clean_tex=False)
