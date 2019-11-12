#!/usr/bin/python3
""" the entry point of the command interpreter """
import traceback
import cmd
import sys
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = "(hbnb) "

    classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
    functions = ["all", "destroy", "update", "show", "create"]

    def do_update(self, line):
        """Update an instance based on class name and id."""
        if not line:
            print('** class name missing **')
            return

        args = shlex.split(line, posix=False)
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print('** instance id missing **')
            return
        else:
            try:
                key = args[0] + '.' + args[1]
                storage.all()[key]
            except:
                print('**no instance found **')
                return

        if len(args) == 2:
            print('** attribute name missing **')
        elif len(args) == 3:
            print('** value missing **')
        else:
            key = args[0] + '.' + args[1]
            try:
                if '.' in args[3]:
                    value = float(args[3])
                else:
                    value = int(args[3])
            except ValueError:
                value = str(args[3]).strip('\"')
                value = value.strip("\'")
                value = str(value)
            setattr(storage.all()[key], args[2], value)
            storage.save()

    def do_all(self, line):
        """Print all instances."""
        if not line:
            print([str(value) for key, value in storage.all().items()])
        elif line in self.classes:
            my_list = []
            for key, value in storage.all().items():
                if str(key.split('.')[0]) == line:
                    my_list.append(str(value))
            print(my_list)
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """Delete an instance based on class name and id."""
        if not line:
            print('** class name missing **')
            return

        args = line.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            try:
                key = args[0] + '.' + args[1]
                del storage.all()[key]
                storage.save()
            except:
                print('** no instance found **')

    def do_show(self, line):
        """Print an instance based on class name and id."""
        if not line:
            print('** class name missing **')
            return

        args = line.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            try:
                key = args[0] + '.' + args[1]
                print(storage.all()[key])
            except KeyError:
                print('** no instance found **')

    def do_create(self, line):
        """Create a new instance of BaseModel."""
        if not line:
            print('** class name missing **')
            return

        try:
            new = eval(line + '()')
            print(new.id)
            new.save()
        except:
            print("** class doesn't exist **")

    def do_quit(self, line):
        """Quit to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing"""
        pass
    
    def precmd(self, line):
        """ Parses the input string. """       
        for c in self.classes:
            for f in self.functions:
                prefix = "{}.{}".format(c, f)
                if line.startswith(prefix):
                    remain = line[len(prefix) + 1:-1].replace(",", "")
                    remain2 = remain.split()
                    if (len(remain2) == 1):
                        id_attr = remain2[0].replace("\"", "")
                        return "{} {} {}".format(f, c, id_attr)
                    elif (len(remain2) == 2):
                        id_attr = remain2[0].replace("\"", "")
                        attr_name = remain2[1].replace("\"", "")
                        return "{} {} {} {}".format(f, c, id_attr, attr_name)
                    elif (len(remain2) >= 3):
                        id_attr = remain2[0].replace("\"", "")
                        attr_name = remain2[1].replace("\"", "")
                        attr_val = remain2[2]
                        return "{} {} {} {} {}".format(f, c, id_attr, attr_name, attr_val)
                    new_line = "{} {} {}".format(f, c, remain)
                    return new_line
        return line


if __name__ == "__main__":
    HBNBCommand().cmdloop()
