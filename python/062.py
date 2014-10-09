#!/usr/bin/env python3

from collections import defaultdict

def largest_perm(n):
	"""return largest possible permutation"""
	# p = sorted(set(int(''.join(x)) for x in permutations(str(n))))
	return int(''.join(sorted(str(n), reverse=True)))

if __name__ == '__main__':
	count_dict = defaultdict(list)
	for n in [x**3 for x in range(345, 10000)]:
		key = largest_perm(n)
		count_dict[key].append(n)
		if len(count_dict[key]) == 5:
			print(count_dict[key])
			break
