from periment import Periment
from fix_type import fix_type
from random import randint
from sys import argv

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
