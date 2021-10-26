
import os
from git import Repo

git_url = "https://github.com/Gustavo-Miguel/teste.git"
repo_dir = "C://Users//Gustavo//Desktop//teste"

if os.path.exists(repo_dir):
    os.remove(repo_dir)
    print("Directory already exist!")
else:
    print("Directory don't exist!")

cloned_repo = Repo.clone_from(git_url, repo_dir)

f = open("C://Users//Gustavo//Desktop//teste//README.md", "a")
f.write("\n\nNow the file has more content!\n\n")
f.close()

cloned_repo.index.add("README.md")
cloned_repo.index.commit("Append Readme")
origin = cloned_repo.remote(name='origin')
origin.push()

