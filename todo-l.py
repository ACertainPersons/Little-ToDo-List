#The first character is the order, after : is title, after a new line is description
n = 0
f = open("data.txt", "r")

print("#:TITLE")
print("____________")

#print the title
print(f.readline(n)) 
for line in f.readlines():
    if n % 3 == 0 :
        print(line)
    n += 1