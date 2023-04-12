# Little-ToDo-List
A command line based ToDo list. Written mostly in Python with some shell script.

## Preview
<img src="https://acertainpersons.github.io/omg_its_img!/sample.png">

<br>

## Installation

**DO NOT USE THE ZIP FILES INCLUDED WITH THE RELEASE. FOLLOW THE FOLLOWING INSTRUCTIONS INSTEAD**\
\
Run the following in your terminal:  
```
git clone https://github.com/ACertainPersons/Little-ToDo-List.git && cd little-todo-list && touch data.txt && echo "Use ./todo.sh -a to write in a new item" >> data.txt
```
Then copy the Little-ToDo-List folder into your /Users directory.
### Reasons and Explanations

The reason why I didn't `cd` into your /Users directory is because on macOS, it doesn't grant you the permission necessary to `git clone` stuff. I don't know if this works on Linux. Please check and if it doesn't work, send me an issue.

<br>

## Available Commands

```
User@ComputerName Little-ToDo-List % ./todo.sh help  
Available Commands:

help, -h   Display the available commands
-l         Lists out the things on your to-do list
-v         Displays the version
-a         Add a new item
-c         Delete (cancel) an item
```