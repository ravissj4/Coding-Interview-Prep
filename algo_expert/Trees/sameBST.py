def sameBsts(arrayOne, arrayTwo):
    # Write your code here.
	
    if len(arrayOne) != len(arrayTwo):
        return False
    if len(arrayOne) == 0:
        return True
    rootElem1 = arrayOne[0]
    rootElem2 = arrayTwo[0]
    if rootElem1 != rootElem2:
        return False
    smallerOne = [arrayOne[i] for i in range(1, len(arrayOne)) if arrayOne[i] < rootElem1]
    smallerTwo = [arrayTwo[i] for i in range(1, len(arrayTwo)) if arrayTwo[i] < rootElem2]
    greaterOne = [arrayOne[i] for i in range(1, len(arrayOne)) if arrayOne[i] >= rootElem1]
    greaterTwo = [arrayTwo[i] for i in range(1, len(arrayTwo)) if arrayTwo[i] >= rootElem2]

    return sameBsts(smallerOne, smallerTwo) and sameBsts(greaterOne, greaterTwo)
        
    
     
	
