#!/usr/bin/python3
""" This is the entry point to the command prompt """
import cmd


class HBNBCommand(cmd.Cmd):
    """ Command Interpreter Class """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyLine(self):
        """An empty line is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
