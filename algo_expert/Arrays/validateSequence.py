def isValidSubsequence(array, sequence):
    j = 0
    for i in range(len(sequence)):
        if j == len(array):
            break
        if sequence[i] == array[j]:
            i += 1
            j += 1
        else:
            j += 1
    if j == len(array):
        return False
    else:
        return True