with open('input', 'r') as f:
	d = f.readlines()

	n = 0
	for l in d:
		t = l[l.find(':')+2:].strip().split(' | ')
		w = t[0].split(' ')
		h = t[1].split(' ')

		w = set([int(x) for x in w if len(x) > 0])
		h = set([int(x) for x in h if len(x) > 0])

		c = -1
		for i in h:
			if i in w:
				c += 1

		n += int(2 ** c)

	print(n)

with open('input', 'r') as f:
	d = f.readlines()

	n = 0
	m = [1] * len(d)
	p = 0
	for l in d:
		t = l[l.find(':')+2:].strip().split(' | ')
		w = t[0].split(' ')
		h = t[1].split(' ')

		w = set([int(x) for x in w if len(x) > 0])
		h = set([int(x) for x in h if len(x) > 0])

		c = 0
		for i in h:
			if i in w:
				c += 1
				m[p + c] += m[p]

		p += 1

	print(sum(m))