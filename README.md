# Little-ToDo-List
A command line based ToDo list. Written mostly in Python with some shell script.

## Preview
<img src="https://acertainpersons.github.io/omg_its_img!/sample1.png">

<br>

## Installation

**DO NOT USE THE ZIP FILES INCLUDED WITH THE RELEASE. FOLLOW THE FOLLOWING INSTRUCTIONS INSTEAD**\
\
Run the following in your terminal:  
```zsh
cd ~/ && git clone https://github.com/ACertainPersons/Little-ToDo-List.git && sudo touch ~/.zshenv && echo "alias todo=~/Little-ToDo-List/todo.sh" >> ~/.zshenv && cd Little-ToDo-List && touch data.txt && echo "Use todo -a to write in a new item" >> data.txt 
```

If it doesn't execute due to a permissions issue, you may need to run the following command:
```zsh
cd ~/Little-ToDo-List
chmod 777 todo.sh
```

<br>

## Available Commands

Just run todo in your terminal!

```zsh
User@ComputerName Little-ToDo-List % todo help  
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

To use the development branch(Just remove the part inside of <>):
```zsh
git checkout -b development-<your_username>
```


