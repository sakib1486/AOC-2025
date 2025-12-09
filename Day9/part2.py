from shapely.geometry import box, Polygon
from itertools import combinations

def part2(points):
    area = -1
    coords = [tuple(x) for x in points]

    poly = Polygon(coords)

    for a, b in combinations(coords, 2):
        min_x, max_x = min(a[0], b[0]), max(a[0], b[0])
        min_y, max_y = min(a[1], b[1]), max(a[1], b[1])

        a = (max_x - min_x + 1) * (max_y - min_y + 1)

        if a < area or not poly.covers(box(min_x, min_y, max_x, max_y)):
            continue

        area = a

    return area