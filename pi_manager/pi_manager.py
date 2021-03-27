"""Raspberry pi managing tool.

Usage:
    pi_manager.py (-h | --help)
    pi_manager.py set_color <COLOR>
    pi_manager.py set_aliases [PATH]
    pi_manager.py listos
    pi_manager.py install <PROJECT>
    pi_manager.py remove <PROJECT>

Arguments:
    PATH    system path
    COLOR   yellow, green, blue ,red
    PROJECT raspberry pi project name

Options:
  -h --help
  set_color     set the pi identification color
  set_aliases   set the terminal aliases
  listos        list all available OS's for the raspberry
  install       install a new project for the raspberry
  remove        remove an existing project from the raspberry

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
    print(arguments)
