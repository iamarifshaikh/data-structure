from math import inf

def numberOfPairs():
    points = [[6,2],[4,4],[2,6]]
    points = [[1,1],[2,2],[3,3]]
    points = [[3,1],[1,3],[1,1]]
    points.sort(key=lambda point: (point[0], -point[1]))
    print(points)
    ans = 0
      
    for i, (x1, y1) in enumerate(points):
        max_y = -inf 
        for x2, y2 in points[i + 1:]:
                # If the y-value of the current point is greater than max_y
                # and not greater than y1, this is a valid pair
            if max_y < y2 <= y1:
                print(max_y,y2,y1)
                max_y = y2  # Update max_y to the current y-value
                ans += 1  # Increment the count of valid pairs

    return ans

print(numberOfPairs())