import os
import os.path

path = os.path.expanduser("~/Little-ToDo-List/data.txt")

try :
    n = int(input("Item Number to be edited: "))
    d = input("What do you want to change the description to (If left blank, nothing will change): ")

    #the part where it closes the task
    # list to store file lines
    lines = []
    # read file
    with open(path, 'r') as fp:
        # read and store all lines into list
        lines = fp.readlines()

    if d :
        m = n*2
        # Write file
        with open(path, 'w') as fp:
            # iterate each line
            for number, line in enumerate(lines):
                # note list index starts from 0
                if number not in [m]:
                     fp.write(line)
                    # iterate each line
                else:
                     fp.write(d + '\n')
    
    #list out
    os.system('/usr/bin/python3 ~/Little-ToDo-List/todo-l.py')
    fp.close()
except ValueError: 
    print()
    print("Only integers are supported")
    print("Please try again")
    os.system('/usr/bin/python3 ~/Little-ToDo-List/todo-t.py')