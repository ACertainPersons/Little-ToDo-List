import os

try :
    n = int(input("Item Number to be deleted: "))

    #the part where it closes the task
    # list to store file lines
    lines = []
    # read file
    with open(r"~/Little-ToDo-List/data.txt", 'r') as fp:
        # read and store all lines into list
        lines = fp.readlines()

    m = (n*2)-1
    p = m + 1
    # Write file
    with open(r"~/Little-ToDo-List/data.txt", 'w') as fp:
        # iterate each line
        for number, line in enumerate(lines):
            # note list index starts from 0
            if number not in [m, p]:
                fp.write(line)
                # iterate each line
    fp.close()
    
    #list out
    os.system('/usr/bin/python3 ~/Little-ToDo-List/todo-l.py')
except ValueError: 
    print()
    print("Only integers are supported")
    print("Please try again")
    os.system('/usr/bin/python3 ~/Little-ToDo-List/todo-c.py')