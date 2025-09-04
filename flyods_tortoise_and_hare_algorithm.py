def findDuplicate():
    arr = [ 2, 6, 4, 1, 3, 1, 5 ]
    tortoise = arr[0]
    hare = arr[0]

    while True:
        tortoise = arr[tortoise]
        hare = arr[arr[hare]]
        if tortoise == hare:
            break
    
    tortoise = arr[0]
    while tortoise != hare:
        tortoise = arr[tortoise]
        hare = arr[hare]
        
    return hare

result = findDuplicate()
print(result)