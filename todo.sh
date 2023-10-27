#!/bin/bash

if [ "$1" == "-l" ] || [ -z "$1" ];
then
   /usr/bin/python3 ~/Little-ToDo-List/todo-l.py
fi

if [ "$1" == "-v" ];
then
   echo ""
   echo "v0.3"
   echo ""
fi

if [ "$1" == "help" ] || [ "$1" == "-h" ];
then
   echo "Available Commands:"
   echo ""
   echo "help, -h       Display the available commands"
   echo "<blank>, -l    Lists out the things on your to-do list"
   echo "-v             Displays the version"
   echo "-a             Add a new item"
   echo "-c             Delete (cancel) an item"
   echo "-t             Change the title for an item"
   echo "-d             Change the description for an item"
fi

if [ "$1" == "-a" ];
then
   /usr/bin/python3 ~/Little-ToDo-List/todo-a.py
fi

if [ "$1" == "-c" ];
then
   /usr/bin/python3 ~/Little-ToDo-List/todo-c.py
fi

if [ "$1" == "-t" ];
then
   /usr/bin/python3 ~/Little-ToDo-List/todo-t.py
fi

if [ "$1" == "-d" ];
then
   /usr/bin/python3 ~/Little-ToDo-List/todo-d.py
fi

if [ "$1" != "-v" ] && [ "$1" != "-l" ] && [ ! -z "$1" ] && [ "$1" != "-a" ] && [ "$1" != "-c" ] && [ "$1" != "help" ] && [ "$1" != "-h" ] && [ "$1" != "-t" ] && [ "$1" != "-d" ];
then
   echo "invalid"
   echo "Use -h to list out the Available Commands"
fi