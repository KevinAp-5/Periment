def fix_type(a):
	for x in range(len(a)):
		if a[x] == 'True':
			a[x] = True
		if a[x] == 'False':
			a[x] = False
		try:
			if a[x].isdigit() is True:
				a[x] = float(a[x])
		except Exception:
			pass
	return a