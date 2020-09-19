from theclass import Periment
from fix_type import fix_type
from sys import argv
command = argv
command.pop(0)
command = fix_type(command)

try:
    peri = Periment()  # Range 'til stop
    if command[0] == 'show':
        peri.show(*command[1:])
    elif command[0] == 'guess':
        peri.guess(*command[1:])
    elif command[0] == 'returning':
        peri.returning(*command[1:])
    else:
        raise ValueError('Invalid function.')

except Exception:
    peri = Periment(rang=10)
    peri.show(animation=True)
    peri.guess(random=True)

