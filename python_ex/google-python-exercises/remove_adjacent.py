def remove_adjancent(nums):
	if not nums: return []
	l=[nums[0]]

	for n in nums[1:]:
		if n != l[-1]:
			l.append(n)

	return l

# zip(n[:-1],n[1:])

