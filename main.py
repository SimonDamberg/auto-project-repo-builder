import string, os
from jinja2 import Template

def validName(project_name):
    special_chars = string.punctuation
    special_chars = special_chars.replace('_', '')
    special_chars= special_chars.replace('-', '')
    hasSpecial = list(map(lambda char: char in special_chars, project_name))
    if(len(project_name.split(" ")) > 1 or any(hasSpecial)):
        return False
    else:
        if len(project_name) >= 1 and len(project_name) <= 40:
            return True
        else:
            return False

def validLanguage(project_language):
    validLanguages = ["python", "java"]
    return project_language.lower() in validLanguages


def getInput():
    project_name = input("What is the name of your project? \n\n")
    while True:
        if validName(project_name):
            break
        else:
            project_name = input("Invalid project name! Please try again.\n\n")

    project_author = input("\n\nWho is the author of this project? \n\n")
    while True:
        if len(project_author) >= 1 and len(project_author) <= 40:
            break
        else:
            project_author = input("Invalid author name! Please try again.\n\n")

    project_language = input("\n\nWhat is your desired programming language for the project? \n\n")
    while True:
        if validLanguage(project_language):
            break
        else:
            project_language = input("Invalid programming language! Please try again.\n\n")

    print("\n====== PROJECT DETAILS ======\n")
    print("Project name: " + project_name)
    print("Author: " + project_author)
    print("Programming language: " + project_language)

    return project_name, project_author, project_language

def createRepository(project_name):
    path = "../" + project_name
    os.mkdir(path)
    print("\nCreated directory at " + os.path.abspath("../" + project_name))
    return

def createReadMe(project_name, project_author):
    readme_template = open("templates/README.md.template").read()
    string = Template(readme_template).render(project_name=project_name, project_author=project_author)
    path = "../" + project_name + "/README.md"
    file = open(path, 'x')
    file.write(string)
    print("Created file at " + os.path.abspath(path))
    return

def createTODO(project_name):
    readme_template = open("templates/TODO.md.template").read()
    string = Template(readme_template).render(project_name=project_name)
    path = "../" + project_name + "/TODO.md"
    file = open(path, 'x')
    file.write(string)
    print("Created file at " + os.path.abspath(path))
    return

def createFile(project_name, project_language):
    if(project_language.lower() == "python"):
        readme_template = open("templates/main.py.template").read()
        string = Template(readme_template).render(project_name=project_name)
        path = "../" + project_name + "/main.py"
    elif(project_language.lower() == "java"):
        readme_template = open("templates/main.java.template").read()
        string = Template(readme_template).render(project_name=project_name)
        path = "../" + project_name + "/main.java"
    else:
        return
    file = open(path, 'x')
    file.write(string)
    print("Created file at " + os.path.abspath(path))
    return

if __name__ == "__main__":
    print("\n====== Welcome to the Automatic Project Builder by @SimonDamberg! ====== \n\n")
    project_name, project_author, project_language = getInput()
    print("\n====== Creating files ======")
    createRepository(project_name)
    createReadMe(project_name, project_author)
    createTODO(project_name)
    createFile(project_name, project_language)
    print("\n====== Successfully created project files!  ======\n")
    print("Happy coding!\n")
