import os
import git 

git_url = "https://github.com/Gustavo-Miguel/teste.git"
repo_dir = "C://Users//Gustavo//Desktop//teste"

def get_description():
    f = open("C://Users//Gustavo//Desktop//description.txt", "r")
    description = f.read()
    return description

if os.path.exists(repo_dir):
    cloned_repo = git.Repo.init(repo_dir)
    #os.remove(repo_dir)
    print("Directory already exist!")
else:
    cloned_repo = git.Repo.clone_from(git_url, repo_dir)
    print("Directory don't exist!")

desc = get_description()

f = open("C://Users//Gustavo//Desktop//teste//CHANGELOG.md", "a")
f.write(desc)
f.close()

cloned_repo.index.add("*")
cloned_repo.index.commit("Changelog commit")
origin = cloned_repo.remote(name='origin')
origin.push()

