from periment import Periment
from fix_type import fix_type
from random import randint
from sys import argv

command = fix_type(argv[1:])

periment = Periment()
# periment.set_filter('name', 'number', 'symbol', 'summary')  # Custom filter

try:
    if command[0] == 'show':
        periment.show(*command[1:])
    elif command[0] == 'returning':
        periment.returning(*command[1:])
    else:
        print('Invalid command.\ncommands: returning, show')
except IndexError:
    command.append('show')
    command.append(randint(1, 119))
    periment.show(*command[1:])
