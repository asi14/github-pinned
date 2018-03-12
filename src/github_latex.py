'''
TODO: make into class
A sample implementation of PyLaTeX with Github-Pinned to generate resumes

'''
import github
from pylatex import Document, Section, Subsection, Command,Itemize
from pylatex.utils import italic, NoEscape

#follow example and create latex document
def make_repos():
	return github.pull_margin(30)

def preamble_modify(doc): #add packages this way doc.packages.append(Package('tikz'))
	print('AAAA')	
def github_generate(doc):
	output=make_repos()
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
	doc=Document(documentclass='article')#modify document classes here, as necessary
	preamble_modify(doc)
	github_generate(doc)
	doc.generate_pdf(filepath='../bin/lists',clean_tex=False)
