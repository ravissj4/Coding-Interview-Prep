def isMonotonic(array):
    # Write your code here.
    isPositiveMonotonic = True
	isNegativeMonotonic = True
	
	for i in range(1, len(array)):
		
		curr = array[i]
		prev = array[i-1]
		
		# let's say our array is +ve monotonic
		if prev > curr: 
			# +ve monotonicity broken
			isPositiveMonotonic = False
			# break
		
		# let's say our array is -ve monotonic
		if prev < curr:
			isNegativeMonotonic = False
			# break
		
	return isPositiveMonotonic or isNegativeMonotonic
		
		
		
		
		