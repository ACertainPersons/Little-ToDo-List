#!/bin/bash

valid="-l"
if [ "$1" == "-l" ];
then
   /usr/bin/python3 /Users/amos/Shell/ToDo/todo-l.py #runs the list command
fi

if [ "$1" != $valid ];
then
   echo "invalid!"w
fi