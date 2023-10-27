import os
import os.path

#first line is title, second is description
title = input("Title: ")
description = input("Description: ")
path = os.path.expanduser("~/Little-ToDo-List/data.txt")

#writing time
f = open(path, "a")
f.write(title + '\n')
f.write(description + '\n')
f.close()

#list out
os.system('/usr/bin/python3 ~/Little-ToDo-List/todo-l.py')