def largestRange(array):
    hash_table = {}

    prev_elem, next_elem = (None, None)
    max_len = float('-inf')

    for i in range(len(array)):
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

"""
algorithm : 
1. iterate over the array elements
2. everytime store the current element in a hash table 
3. keep on expanding towards the left and right of the current element 
    by subtracting 1 (prev element) and adding 1 (next element) and searching
    in the hash table and also incrementing the length meanwhile
4. if length > max_len 
    then make max_len = length 
    and best_range = prev and next elemns but 1 position shrinked since 
    they would have gone 1 step forward in order to break their respective loops
    
"""