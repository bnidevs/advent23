with open('input', 'r') as f:
	d = f.readlines()

	ct = {'red': 12, 'green': 13, 'blue': 14}

	s = 0

	i = 1
	for l in d:
		t = l[l.find(':')+2:].strip().split('; ')

		b = True

		for r in t:
			k = r.split(', ')

			for c in k:
				p = c.split(' ')

				if ct[p[1]] < int(p[0]):
					b = False
					break

			if not b:
				break

		if b:
			s += i

		i += 1

	print(s)

from functools import reduce

with open('input', 'r') as f:
	d = f.readlines()

	s = 0

	i = 1
	for l in d:
		ct = {'red': 0, 'green': 0, 'blue': 0}

		t = l[l.find(':')+2:].strip().split('; ')

		b = True

		for r in t:
			k = r.split(', ')

			for c in k:
				p = c.split(' ')

				ct[p[1]] = max(ct[p[1]], int(p[0]))

		s += reduce(lambda x, y: x * y, ct.values())

		i += 1

	print(s)