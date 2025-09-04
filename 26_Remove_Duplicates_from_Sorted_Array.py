def removeDuplicates():
    array = [1,1,1,2,2,3]
    j = 0

    for i in range(len(array)):
        if array[i] != array[j]:
            j += 1
            array[j] = array[i]
    return j + 1


result = removeDuplicates()
print(result)