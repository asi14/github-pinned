import github

#follow example and create latex document

def make_file():
	repo_output = github.pull_margin(30)
	print(repo_output)
make_file()
