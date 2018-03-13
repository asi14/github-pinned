'''
TODO: make into class
A sample implementation of PyLaTeX with Github-Pinned to generate resumes
take note with how the method github_generate(doc) ieterates through the outputed dictionary to extract the repo
details as necessary
for PyLaTeX-specific questions, please visit its documentation.
'''
import github
from pylatex import Document, Section, Subsection, Command,Itemize,Package
from pylatex.utils import italic, NoEscape

#follow example and create latex document

def make_repos(): #generate github dictionary here
	return github.pull_margin(30)
def preamble_modify(doc): #add LaTeX packages here. Ex: doc.packages.append(Package('tikz'))
	doc.packages.append(Package('myresume'))#sample package
def github_generate(doc): #parses the file and generates the according LaTeX
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
