#!/usr/bin/python3
"""This module supplies a console that interracts with the airbnb system"""

from models.base_model import BaseModel
from models import storage
import cmd
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    defines a class that inherits from cmd with its attributes and methods
    """

    prompt = "(hbnb) "
    Classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
            }

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    do_quit = do_EOF
    
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
            if " " in line:
                classname, id = line.split()
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
                print(f"** instance id missing **")
        else:
            print(f"** class name missing **")

    def do_destroy(self, line=None):
        """Deletes an instance based on the class name and id"""
        if line:
            if " " in line:
                classname, id = line.split()
                key = classname + "." + id
                all_instance = storage.all()
                if classname not in self.Classes:
                    print(f"** class doesn't exist **")
                elif key not in all_instance.keys():
                    print(f"** no instance found **")
                else:
                    all_instance.pop(key)
                    storage.save()
            else:
                print(f"** instance id missing **")
        else:
            print(f"** class name missing **")

    def do_all(self, line=None):
        """Prints all string representation of all instances based or not on the class name"""
        all_instance = storage.all()
        if line:
            if line in self.Classes:
                for key, value in all_instance.items():
                    name, id = key.split(".")
                    if line == name:
                        print(value)
            else:
                print(f"** class doesn't exist **")
        else:
            for key, value in all_instance.items():
                print(value)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        space_count = 0
        if line:
            for i in line:
                if i == " ":
                    space_count += 1
            if space_count == 0:
                print(f"** instance id missing **")
            elif space_count == 1:
                print(f"** attribute name missing **")
            elif space_count == 2:
                print(f"** value missing **")
            elif space_count == 3:
                all_instance = storage.all()
                classname, id, attr_name, attr_value = line.split()
                key = classname + "." + id
                if key in all_instance.keys():
                    instance = self.Classes[classname](all_instance[key])
                    setattr(instance, attr_name, attr_value)
                    instance.save()

                


























if __name__ == "__main__":
    HBNBCommand().cmdloop()
