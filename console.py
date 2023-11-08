#!/usr/bin/python3
"""This module supplies a console that interracts with the airbnb system"""

from models.base_model import BaseModel
from models import storage
import cmd

class HBNBCommand(cmd.Cmd):
    """
    defines a class that inherits from cmd with its attributes and methods
    """

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        pass

    do_quit = do_EOF
if __name__ == "__main__":
    HBNBCommand().cmdloop()
