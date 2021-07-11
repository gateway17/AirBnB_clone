#!/usr/bin/python3

"""Entry piont of AirBnB console """
import cmd
from models.base_model import BaseModel
from shlex import split as parse


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb)'
    clases = ["BaseModel"]

    def do_quit(self, arg):
        """ quit and EOF to exit the program.\n """
        return True

    def do_EOF(self,arg):
        """ quit and EOF to exit the program.\n """
        return True


    def do_create(self, arg):
        """ Creates intances of given argument """

        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in self.clases:
            print("** class doesn't exist **")
        else:
            instance = eval(arg[0])()
            BaseModel.storage.save(instance)
            print(instance.id)

    def do_show(self, arg):
        """ Prints the string representation of an instance\
        based on the class name and id """
        args = parse(arg)
        objects = models.storage.all()
        data = args[0] + '.' + args[1]

        if args == []:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")

        if data in objects.keys():
            print(objects[data])

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id"""
        args = parse(arg)
        if arg == []:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")

        else:
            data = args[0] + '.' + args[1]
            if data in objects.keys():
                objects.pop(data, None)
                objects.storage.save()
            else:
                print('** no instance found **')

    def do_all(self, arg):
        """ """
        args = parse(arg)
        data = args[0] + '.' + args[1]
        if data not in objects.keys:
            print("** class doesn't exist **")
        elif data in objects.keys:
            return list(str(data))
        else:
            return list(str(objects))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
