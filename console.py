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
    Classes = {"BaseModel": BaseModel}

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        pass

    def do_create(self, line=None):
        """ Create new instance of BaseModel"""

        if not line:
            print(f"** class name missing **")
        elif line in self.Classes:
            obj = self.Classes[line]()
            obj.save()
            print(obj.id)
        else:
            print(f"** class doesn't exist **")

    def do_show(self, line=None):
        """Prints the string representation of an instance """
        """based on the class name and id"""
        
        if line:
            classname, id = line.split()
        
            if not classname:
                print(f"** class name missing **")
            if not id:
                print(f"** instance id missing **")
            if classname not in self.Classes:
                print(f"** class doesn't exist **")
            else:
                key = classname + "." + id
                all_instance = storage.all()

                if key in all_instance.keys():
                    print(self.Classes[classname](all_instance[key]))
                else:
                    print(f"** no instance found **")
        else:
            print(f"Usage: show Classname Id")

    def do_destroy(self, line):
        pass


    do_quit = do_EOF
if __name__ == "__main__":
    HBNBCommand().cmdloop()
