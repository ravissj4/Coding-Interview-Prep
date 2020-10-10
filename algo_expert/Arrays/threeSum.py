def threeNumberSum(array, targetSum):
    # Write your code here.
	answer = []
    array.sort()
    for i in range(len(array) - 2):
		current_no = array[i]
		new_target_sum = targetSum - current_no
		left_ptr = i+1
		right_ptr = len(array) - 1
		
		while left_ptr < right_ptr:
			left_no = array[left_ptr]
			right_no = array[right_ptr]
			
			if left_no + right_no > new_target_sum:
				right_ptr -= 1
			elif left_no + right_no < new_target_sum:
				left_ptr += 1
			else:
                ans = []
				ans.append(current_no)
				ans.append(left_no)
				ans.append(right_no)
				ans.sort()
                left_ptr += 1
                right_ptr -= 1
		        answer.append(ans)
	
	return answer
		
			
				