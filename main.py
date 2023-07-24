from periment import Periment
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


periment = Periment()
periment.set_filter('name', 'number', 'symbol', 'summary')  # Custom filter

argv = fix_type(argv[1:])
if len(argv) == 0:
    argv.append('show')

command = argv.pop(0)
if command == 'show':
    periment.show(*argv)
elif command == 'return':
    periment.returning(*argv)
else:
    periment.show(random=True, animation=True)
