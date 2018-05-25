import re


def generalize_function(content, general_name):
    x = re.search("def .+\(", content).group()
    content = content.replace(x, "def {}(".format(general_name))
    return content

with open("C:\\Users\\Lenovo\\Documents\\GitHub\\licenta\\Business\\Repositories\\CompilerAuxFiles\\script.py",
          "r") as fl:
    print(generalize_function(fl.read(),"func_submitted"))