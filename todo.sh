#!/bin/bash

if [ "$1" == "-l" ] || [ -z "$1" ];
then
   /usr/bin/python3 /Users/Little-ToDo-List/todo-l.py
fi

if [ "$1" == "-v" ];
then
   echo "v0.2"
fi

if [ "$1" == "help" ];
then
   echo "Available Commands:"
   echo ""
   echo "help   Display the available commands"
   echo "-l     Lists out the things on your to-do list"
   echo "-v     Displays the version"
   echo "-a     Add a new item"
   echo "-c     Delete (cancel) an item"
fi

if [ "$1" == "-a" ];
then
   /usr/bin/python3 /Users/Little-ToDo-List/todo-a.py
fi

if [ "$1" == "-c" ];
then
   /usr/bin/python3 /Users/Little-ToDo-List/todo-c.py
fi

if [ "$1" != "-v" ] && [ "$1" != "-l" ] && [ ! -z "$1" ] && [ "$1" != "-a" ] && [ "$1" != "-c" ] && [ "$1" != "help" ];
then
   echo "invalid"
fi