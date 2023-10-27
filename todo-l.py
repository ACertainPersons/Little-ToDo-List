import os.path

path = os.path.expanduser("~/Little-ToDo-List/data.txt")

#first line is title, second is description
n = 0
f = open(path, "r")
z = 1

#print the title
print (f.readline(n)) 
for line in f.readlines():
    if (n + 1) % 2 == 0 :
        t = (line)
        y = str(z)
        print("☐ " + y + ") " + t)
        z += 1
    elif n != 0: 
        print("      "  + line)#there should be 6 spaces within the bracket
    else :
        print(line)
    n += 1
print()