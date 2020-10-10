def largestRange(array):
    hash_table = {}

    prev_elem, next_elem = (None, None)
    max_len = float('-inf')
	for i in range(len(array)):
		hash_table[array[i]] = False
		
    for i in range(len(array)):
		if hash_table[array[i]] == True:
			continue
        length = 0
        hash_table[array[i]] = True
        prev_elem = array[i] - 1
        while prev_elem in hash_table:
            length += 1
            prev_elem -= 1
        
        next_elem = array[i] + 1
        while next_elem in hash_table:
            length += 1
            next_elem += 1
        # print(f'length = {length}, max_len = {max_len}')
        if length > max_len:
            best_range = [prev_elem + 1, next_elem - 1]
			max_len = length
        
    
    return best_range
