import math
def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

#Manhattan is the combination of Edge value(distance) from vertex A to vertex B

def manhattan():
    distance = manhattan_distance(1, 1, 5, 4)
    print(distance)

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def euclidean():
    distance = euclidean_distance(1,1,5,4)
    print(distance)


def run():
    #manhattan()
    euclidean()