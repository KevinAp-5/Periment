from periment import Periment
from fix_type import fix_type
from sys import argv

command = fix_type(argv[1:])

periment = Periment()
if command[0] == 'show':
    periment.show(*command[1:])
elif command[0] == 'returning':
    periment.returning(*command[1:])
else:
    print('Invalid command.\ncommands: returning, show')
