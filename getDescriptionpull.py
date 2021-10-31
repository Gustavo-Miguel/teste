import os
import git 
import requests

git_url = "  https://api.github.com/repos/Gustavo-Miguel/teste/pulls/1"

def get_description():
    description = requests.get(git_url)
    return description

desc = get_description()

print("---DESCRIPTION---")
print(desc.json().get('body'))
