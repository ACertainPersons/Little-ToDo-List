# Little-ToDo-List
A command line based ToDo list. Written mostly in Python with some shell script.

## Preview
<img src="https://acertainpersons.github.io/omg_its_img!/sample.png">

<br>

## Installation

**DO NOT USE THE ZIP FILES INCLUDED WITH THE RELEASE. FOLLOW THE FOLLOWING INSTRUCTIONS INSTEAD**\
\
Run the following in your terminal:  
```zsh
cd /Users/ && sudo git clone https://github.com/ACertainPersons/Little-ToDo-List.git && sudo chmod 777 little-todo-list && cd little-todo-list && sudo touch data.txt && sudo chmod 777 data.txt && sudo echo "Use ./todo.sh -a to write in a new item" >> data.txt
```

<br>

## Available Commands

```zsh
User@ComputerName Little-ToDo-List % ./todo.sh help  
Available Commands:

help, -h       Display the available commands
<blank>, -l    Lists out the things on your to-do list
-v             Displays the version
-a             Add a new item
-c             Delete (cancel) an item
-t             Change the title for an item
-d             Change the description for an item

```

## Contributing

You are welcome to fork it and add your own things to it. If you want your version to be integrated into here, feel free to send a pull request.
