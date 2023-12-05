with open('input', 'r') as f:
	d = [x.strip() for x in f.readlines()]

	r = 0
	cl = {}
	for l in d:

		i = 0

		cc = ''
		s = set([str(x) for x in range(10)])
		while i < len(l):
			if l[i] in s:
				cc += l[i]
			elif len(cc) > 0:
				cl[(r, i - len(cc))] = cc
				cc = ''

			i += 1

		if len(cc) > 0:
			cl[(r, i - len(cc))] = cc
			cc = ''

		r += 1

	tt = 0

	for k in cl:
		au = [(k[0] - 1, k[1] + x) for x in range(-1, len(cl[k]) + 1)]
		ab = [(k[0] + 1, k[1] + x) for x in range(-1, len(cl[k]) + 1)]

		sr = au + ab + [( k[0], k[1] - 1 ), ( k[0], k[1] + len(cl[k]) )]

		sr = [p for p in sr if 0 <= p[0] < len(d) and 0 <= p[1] < len(d[0])]

		sr = set([d[p[0]][p[1]] for p in sr])

		s = set([str(x) for x in range(10)])
		for sn in s:
			sr.discard(sn)

		sr.discard('.')

		if len(sr) > 0:
			tt += int(cl[k])

	print(tt)

with open('input', 'r') as f:
	d = [x.strip() for x in f.readlines()]

	r = 0
	cl = {}
	for l in d:

		i = 0

		cc = ''
		s = set([str(x) for x in range(10)])
		while i < len(l):
			if l[i] in s:
				cc += l[i]
			elif len(cc) > 0:
				cl[(r, i - len(cc))] = cc
				cc = ''

			i += 1

		if len(cc) > 0:
			cl[(r, i - len(cc))] = cc
			cc = ''

		r += 1

	tt = 0

	ng = {}

	for k in cl:
		au = [(k[0] - 1, k[1] + x) for x in range(-1, len(cl[k]) + 1)]
		ab = [(k[0] + 1, k[1] + x) for x in range(-1, len(cl[k]) + 1)]

		sr = au + ab + [( k[0], k[1] - 1 ), ( k[0], k[1] + len(cl[k]) )]

		sr = [p for p in sr if 0 <= p[0] < len(d) and 0 <= p[1] < len(d[0])]


		for p in sr:
			if d[p[0]][p[1]] == '*':
				if (p[0], p[1]) in ng:
					tt += int(cl[k]) * ng[(p[0], p[1])]
					del ng[(p[0], p[1])]
				else:
					ng[(p[0], p[1])] = int(cl[k])

	print(tt)
