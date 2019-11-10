#!/usr/bin/python3
""" the entry point of the command interpreter """
import cmd
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF to exit the program"""
        print()
        return True

    def emptyline(self):
        """If this method is not overridden, repeats the last
            nonempty command entered"""

if __name__ == "__main__":
    HBNBCommand().cmdloop()
