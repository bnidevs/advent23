with open('input', 'r') as f:
	d = [l.strip() for l in f.readlines()]

	d = [[int(i) for i in x.split(' ')[1:] if i != ''] for x in d]

	t = d[0]
	d = d[1]
	l = len(t)

	p = 1
	for i in range(l):
		ct, cd = t[i], d[i]

		nw = 0
		for g in range(ct):
			if (ct - g) * g > cd:
				nw += 1

		p *= nw

	print(p)

with open('input', 'r') as f:
	d = [l.strip() for l in f.readlines()]

	d = [[i for i in x.split(' ')[1:] if i != ''] for x in d]

	t = int(''.join(d[0]))
	d = int(''.join(d[1]))

	g = 1
	while (t - g) * g <= d:
		g += 1

	print(t - 2 * g + 1)
