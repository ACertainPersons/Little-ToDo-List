import os

#first line is title, second is description
title = input("Title: ")
description = input("Description: ")

#writing time
f = open("data.txt", "a")
f.write(title + "\n")
f.write(description + "\n")
f.close()

#list out
os.system('/usr/bin/python3 /Users/amos/Shell/Little-ToDo-List/todo-l.py')