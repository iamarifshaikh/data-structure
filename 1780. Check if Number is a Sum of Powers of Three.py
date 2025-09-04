def checkPowersOfThree(n, x=0, sumOf=0):
    if sumOf == n:
        return True
    
    if sumOf > n:
        return False
    
    if 3 ** x > n:
        return False

    if checkPowersOfThree(n, x+1, sumOf + (3 ** x)):
        return True
    
    if checkPowersOfThree(n, x+1, sumOf):
        return True
    
    return False

result = checkPowersOfThree(91,0,0)
print(result)