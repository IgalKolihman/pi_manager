"""Raspberry pi managing tool.

Usage:
    pi_manager.py (-h | --help)
    pi_manager.py set_color <TYPE>
    pi_manager.py set_aliases [PATH]

Arguments:
    COLOR   yellow, green, blue ,red

Options:
  -h --help
  set_color     set the pi identification color
  set_aliases    set the terminal aliases

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
    print(arguments)
