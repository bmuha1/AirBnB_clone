#!/usr/bin/python3
""" the entry point of the command interpreter """
import cmd, sys
from models.base_model import BaseModel
import models
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = "(hbnb) "

    def do_all(self, line):
        """Print all instances."""
        if not line or line == 'BaseModel':
            print([str(value) for key, value in storage.all().items()])
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """Delete an instance based on class name and id."""
        if not line:
            print('** class name missing **')
            return

        args = line.split()
        if args[0] != 'BaseModel':
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
        if args[0] != 'BaseModel':
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

if __name__ == "__main__":
    HBNBCommand().cmdloop()
