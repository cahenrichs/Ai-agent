from functions.run_python_file import run_python_file

f = run_python_file("calculator", "main.py") 
print(f)
g = run_python_file("calculator", "main.py")
print(g)
h = run_python_file("calculator", "tests.py")
print(h)
j = run_python_file("calculator", "../main.py")
print(j)
k = run_python_file("calculator", "nonexistent.py")
print(k)