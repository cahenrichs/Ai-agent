from functions.write_file import write_file


g = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
print(g)

q = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
print(q)

r = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
print(r)