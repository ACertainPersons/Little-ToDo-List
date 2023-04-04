import os

#first line is title, second is description
title = input("Title: ")
description = input("Description: ")

#writing time
f = open("/Users/Little-ToDo-List/data.txt", "a")
f.write(title + "\n")
f.write(description + "\n")
f.close()

#list out
os.system('/usr/bin/python3 /Users/Little-ToDo-List/todo-l.py')