#!/usr/bin/python3
""" This is the entry point to the command prompt """
import cmd
import json
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Command Interpreter Class """

    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Command to exit program """
        return True

    def do_EOF(self, arg):
        """Command to exit program """
        print("")
        return True

    def emptyLine(self):
        """When an empty line is entered """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
