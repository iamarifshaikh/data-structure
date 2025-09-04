def findClosest():
    x = 2
    y = 7
    z = 4

    if abs(x - z) == abs(y - z): return 0
    if abs(x - z) < abs(y - z): return 1
    else: return 2


findClosest()