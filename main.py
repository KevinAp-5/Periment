from periment import Periment
from random import randint
from sys import argv

def fix_type(argv):  # Fix TypeError caused by argv, agrv returns str
    """ Get a list and fix the type errors"""
    for x in range(len(argv)):
        if isinstance(argv[x], str):
            if argv[x].isnumeric() is True:
                argv[x] = int(argv[x])
            elif '.' in argv[x]:
                argv[x] = float(argv[x])
            elif argv[x] == 'True' or argv[x] == 'False':
                argv[x] = bool(argv[x])

    return argv

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
