#!/usr/bin/python3
""" This is the entry point to the command prompt """
import cmd
from models.base_model import BaseModel
from models import storage


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

    def do_create(self, arg):
        """Create Command to create a new instance of BaseModel"""
        if not arg:
            print("** Class Name Missing **")
        elif arg not in storage.CLASSES:
            print("** Class doesn't exist **")
        else:
            new_instance = storage.CLASSES[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Show command to print the string representation of an instance"""
        args = arg.split()
        if not arg:
            print("** Class name missing **")
        elif args[0] not in storage.CLASSES:
            print("** Class doesn't exist **")
        elif len(args) == 1:
            print("** Instance ID missing **")
        else:
            obj_key = args[0] + "." + args[1]
            objs = storage.all()
            if obj_key not in objs:
                print("** No instance found **")
            else:
                print(objs[obj_key])

    def do_destroy(self, arg):
        """Destroy command to delete an instance"""
        args = arg.split()
        if not arg:
            print("** Class Name missing **")
        elif args[0] not in storage.CLASSES:
            print("** Class doesn't exist **")
        elif len(args) == 1:
            print("** Instance ID missing **")
        else:
            obj_key = args[0] + "." + args[1]
            objs = storage.all()
            if obj_key not in objs:
                print("** No instance found **")
            else:
                del objs[obj_key]
                storage.save()

    def do_all(self, arg):
        """All command to print All instances"""
        objs = storage.all()
        if not arg:
            print([str(objs[obj]) for obj in objs.values()])
        elif arg not in storage.CLASSES:
            print("** Class doesn't exist **")
        else:
            result = []
            for key in objs.keys():
                if key.split('.')[0] == arg:
                    result.append(str(objs[key]))
            print(result)

    def do_update(self, arg):
        """Update command to update an instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in storage.CLASSES:
            print("** Class doesn't exist **")
        elif len(args) == 1:
            print("** Instance Id missing **")
        elif len(args) == 2:
            print("** Attribute name missing **")
        elif len(args) == 3:
            print("** Value missing **")
        else:
            obj_key = args[0] + "." + args[1]
            objs = storage.all()
            if obj_key not in objs:
                print("** No Instance Found **")
            else:
                obj = objs[obj_key]
                attr = args[2]
                value = args[3]
                if hasattr(obj, attr):
                    value_type = type(getattr(obj, attr))
                    try:
                        value = value_type(value)
                    except ValueError:
                        pass
                    setattr(obj, attr, value)
                    obj.save()
                else:
                    print("** Attribute doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
