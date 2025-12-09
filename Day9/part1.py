def part1(points):
    area = 0
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i+1, n):
            x2, y2 = points[j]
            # must be opposite corners (different x and different y)
            if x1 == x2 or y1 == y2:
                continue
            width = abs(x2 - x1) + 1
            height = abs(y2 - y1) + 1
            a = width * height
            if a > area:
                area = a
    
    return area