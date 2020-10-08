def InSort(ar):
    #Assuming first element is sorted
    #start on second element
    for i in range(1, len(ar)):
        ins = ar[i]
        #Save the previous value
        j = i-1
        #Move all the sorted larger elements ahead
        while j>=0 and ar[j] > ins:
            ar[j+1] = ar[j]
            j = j-1
        #Make insertion XD
        ar[j+1] = ins

    return ar

#Print
print(InSort([5,6,8,9,2,3,66,45,1,25,00,-1]))

