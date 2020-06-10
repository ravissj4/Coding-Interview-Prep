def minRewards(array):
    rewards = [1 for i in range(len(array))]
    for i in range(1, len(rewards)):
        if array[i] > array[i-1]:
            rewards[i] = rewards[i-1] + 1
    
    for i in reversed(range(len(rewards) - 1)):
        if array[i] > array[i+1]:
            rewards[i] = max(rewards[i], rewards[i+1] + 1)
        
    return sum(rewards)
        

