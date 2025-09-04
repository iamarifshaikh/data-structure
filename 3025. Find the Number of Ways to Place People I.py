def numberOfPairs():
    points = [[1,1],[2,2],[3,3]]
    # points.sort()
    print(points)
    count = 0

    for i in range(len(points)):
        for j in range(len(points)):
            if i == j: continue
            A = points[i]
            B = points[j]
            
            if A[0] <= B[0] and A[1] >= B[1] and (A[0] < B[0] or A[1] > B[1]):
                valid = True

                for k in range(len(points)):
                    if k == i or k == j:
                        continue

                    C = points[k]
                    
                    if  A[0] <= C[0] <= B[0] and B[1] <= C[1] <= A[1]:
                        valid = False
                        break

                if valid:
                    print(A,B)
                    count += 1
    return count

print(numberOfPairs())