import os

#first line is title, second is description
title = input("Title: ")
description = input("Description: ")

#writing time
r = open("data.txt", "r")
d = open("data.txt", "w")
f = open("data.txt", "a")
if 'Nothing to do ;) Use ./todo.sh -a to write in a new item' in r.read():  
    d.write("")
f.write(title + "\n")
f.write(description + "\n")
f.close()

#list out
os.system('/usr/bin/python3 /Users/amos/Shell/Little-ToDo-List/todo-l.py')