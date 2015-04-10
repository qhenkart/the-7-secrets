def isSubsetOf(list1, list2):
	exists = True
	for elem in list1:
		if elem not in list2:
			exists = False
	return exists








arr = ["is", "here"]
arr2 = ["something", "whatever", "happening", "here"]

print isSubsetOf(arr, arr2)
