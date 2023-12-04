with open('input', 'r') as f:
	d = f.readlines()

	t = 0

	s = set([str(x) for x in range(10)])
	for l in d:
		c = 0
		while l[c] not in s:
			c += 1

		t += 10 * int(l[c])

		c = -1
		while l[c] not in s:
			c -= 1

		t += int(l[c])

	print(t)

with open('input', 'r') as f:
	d = f.readlines()

	t = 0

	s = set([str(x) for x in range(10)])
	w = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
	for l in d:
		c = 0
		while l[c] not in s:
			c += 1

		cv = int(l[c])

		wf = [l.find(x) for x in w]
		for i,k in enumerate(wf):
			if -1 < k < c:
				c = k
				cv = i + 1

		t += 10 * cv

		c = -1
		while l[c] not in s:
			c -= 1

		cv = int(l[c])
		c += len(l)

		wf = [l.rfind(x) for x in w]
		for i,k in enumerate(wf):
			if k != -1 and k > c:
				c = k
				cv = i + 1

		t += cv

	print(t)
