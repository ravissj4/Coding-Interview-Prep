def isValidSubsequence(array, sequence):
	i,j=0,0
	matched_elements = 0
	while i != len(sequence):
        if j == len(array):
            break
        if sequence[i] == array[j]:
            i += 1
            j += 1
			matched_elements += 1
        else:
            j += 1
	# print(matched_elements)
	# print(len(sequence))
	return matched_elements == len(sequence)
    