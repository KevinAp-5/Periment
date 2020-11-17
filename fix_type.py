def fix_type(argv):  # Fix TypeError caused by argv, agrv returns str
    for x in range(len(argv)):
        """ Get a list and fix the type errors"""
        if type(argv[x]) == str:
            try:
                argv[x] = bool(argv[x])
            except Exception:
                raise

        try:
            if argv[x].isdigit() is True:
                argv[x] = float(argv[x])
        except Exception:
            raise
        return argv
