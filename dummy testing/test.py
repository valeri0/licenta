import subprocess


def run_in_docker(source_code):
    with open("script.py","w") as write_file:
        for line in source_code.strip():
            write_file.write(line)


run_in_docker(
    "def myfunc(x,y):\
    if x > y:\
        return x+y\
    elif: x < y:\
        return x-y\
    else:\
        return x*y\
# Test cases\
print myfunc(2,3)\
print myfunc(10,2)")
