def subarraySort(array):
    # Write your code here.
	min_out_of_order = float("inf")
	max_out_of_order = float("-inf")
	
	for i in range(len(array)):
		num = array[i]
		if(out_of_order(num, array, i)):
			# update
			max_out_of_order = max(max_out_of_order, num)
			min_out_of_order = min(min_out_of_order, num)
		
	
	# check boundary condition -> array already sorted
	if max_out_of_order == float("-inf") and min_out_of_order == float("inf"):
		return [-1,-1]
	# check the left boundary of unsorted
	left_idx = 0
	while(min_out_of_order >= array[left_idx]):
		left_idx += 1
	# check the right boundary of the unsorted
	right_idx = len(array) - 1
	while max_out_of_order <= array[right_idx]:
		right_idx -= 1
	
	return [left_idx, right_idx]
	
def out_of_order(num, array, i):
	if i == 0:
		return num > array[i+1]
	if i == len(array) - 1:
		return num < array[i-1]
	return num < array[i-1] or num > array[i+1]
    
