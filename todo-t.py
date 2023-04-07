import os

try :
    n = int(input("Item Number to be edited: "))
    t = input("What do you want to change the title to (If left blank, nothing will change): ")

    #the part where it closes the task
    # list to store file lines
    lines = []
    # read file
    with open(r"/Users/Little-ToDo-List/data.txt", 'r') as fp:
        # read and store all lines into list
        lines = fp.readlines()

    if t :
        m = (n*2)-1
        # Write file
        with open(r"/Users/Little-ToDo-List/data.txt", 'w') as fp:
            # iterate each line
            for number, line in enumerate(lines):
                # note list index starts from 0
                if number not in [m]:
                     fp.write(line)
                    # iterate each line
                else:
                     fp.write(t + '\n')
    
    #list out
    os.system('/usr/bin/python3 /Users/Little-ToDo-List/todo-l.py')
    fp.close()
except ValueError: 
    print()
    print("Only integers are supported")
    print("Please try again")
    os.system('/usr/bin/python3 /Users/Little-ToDo-List/todo-t.py')