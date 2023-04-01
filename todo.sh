#!/bin/bash

if [ "$1" == "-l" ] || [ -z "$1" ];
then
   /usr/bin/python3 /Users/amos/Shell/Little-ToDo-List/todo-l.py
fi

if [ "$1" == "-v" ];
then
   echo "v0.5"
fi

if [ "$1" == "-a" ];
then
   /usr/bin/python3 /Users/amos/Shell/Little-ToDo-List/todo-a.py
fi

if [ "$1" != "-v" ] && [ "$1" != "-l" ] && [ ! -z "$1" ] && [ "$1" == "-a" ];
then
   echo "invalid"
fi