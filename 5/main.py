with open('input', 'r') as f:
	d = f.read()

	maps = d.split('\n\n')

	seeds = [int(x) for x in maps[0][maps[0].find(':')+2:].strip().split(' ')]

	maps = [x.strip().split('\n')[1:] for x in maps[1:]]

	for m in maps:
		mp = [[int(y) for y in x.split(' ')] for x in m]

		for i in range(len(seeds)):
			for c in mp:
				if c[1] <= seeds[i] < c[1] + c[2]:
					seeds[i] += c[0] - c[1]
					break

	print(sorted(seeds)[0])