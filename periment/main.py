from theclass import Periment
from fix_type import fix_type
from sys import argv
command = argv
command.pop(0)
command = fix_type(command)

try:
	peri = Periment()  # Range 'til stop
	if command[0] == 'show':
		command.pop(0)
		peri.show(*command)
	elif command[0] == 'guess':
		command.pop(0)
		peri.guess(*command)
	elif command[0] == 'returning':
		command.pop(0)
		peri.returning(*command)

except Exception:
	peri = Periment(rang=10)
	peri.show(animation=True)
	peri.guess()
