from theclass import Periment
from fix_type import fix_type
from sys import argv
command = argv
command.pop(0)
command = fix_type(command)

try:
    peri = Periment()  # Range 'til stop
    if command[0] in ('show', 'guess', 'returning'):
        command.pop(0)
        peri.returning(*command)
    else:
        raise ValueError('Invalid function.')

except Exception:
    peri = Periment()
    peri.ranger = 10
    peri.show(animation=True)
    peri.guess(random=True)

