#!bin/bash

# to make the file excecutable, add the following line somewhere
# chmod +x .my_custom_commands.sh

# to add all the commands to any terminal session, i need add the following line to the
# .bashrc
# source <path to file>/.commands.sh

# prints the input
function () {
  echo 'Your input: ' $1
}