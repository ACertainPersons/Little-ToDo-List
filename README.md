# Little-ToDo-List
A command line based ToDo list. Written mostly in Python with some shell script.

## Preview
<img src="https://acertainpersons.github.io/omg_its_img!/sample.png">

<br>

## Installation

**DO NOT USE THE ZIP FILES INCLUDED WITH THE RELEASE. FOLLOW THE FOLLOWING INSTRUCTIONS INSTEAD**\
\
First make sure that you have python3 installed by using  `python3 --version`. If you don't have python3, use DuckDuckGo to find out how to get it installed on your system. Then run the following in your terminal:
```
cd /Users && git clone https://github.com/ACertainPersons/Little-ToDo-List.git && cd little-todo-list && touch data.txt && echo "Use ./todo.sh -a to write in a new item" >> data.txt
```
Note: Due to the current folder set up, this tool will only run on macOS.

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
-t         Change the title for an item
-d         Change the description for an item
```