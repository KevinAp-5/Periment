from periment import Periment
from random import randint
from sys import argv

def fix_type(argv):  # Fix TypeError caused by argv, agrv returns str
    """ Get a list and fix the type errors"""

    new_argv = []
    for index, item in enumerate(argv):
        if index == 1:
            new_argv.append(int(item))
        elif index == 2:
            new_argv.append(True if item.lower() == 'true' else False)
        else:
            new_argv.append(item)
    return new_argv

command = fix_type(argv[1:])

periment = Periment()
# periment.set_filter('name', 'number', 'symbol', 'summary')  # Custom filter

try:
    if command[0] == 'show':
        command.pop(0)
        periment.show(*command)
    elif command[0] == 'return':
        command.pop(0)
        periment.returning(*command)
    else:
        print('Invalid command.\ncommands: return, show')
except IndexError:
    periment.show(random=True, animation=True)
