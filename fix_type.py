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
