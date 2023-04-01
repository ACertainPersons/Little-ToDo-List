#first line is title, second is description
n = 0
f = open("data.txt", "r")

#print the title
print (f.readline(n)) 
for line in f.readlines():
    if n % 2 == 0 :
        t = (line)
        print("☐ " + t)
    else : 
        print("    "  + line)#there should be 4 spaces within the bracket
    n += 1