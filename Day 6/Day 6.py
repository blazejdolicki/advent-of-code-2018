import numpy as np

def manhattan_distance(x,y,coord):
    distance = abs(x-int(coord[0]))+abs(y-int(coord[1]))
    return distance


coordinates = open("input.txt").read().split("\n")
# coordinates = ["1, 1",
# "1, 6",
# "8, 3",
# "3, 4",
# "5, 5",
# "8, 9"]
print(len(coordinates))
# Remove empty strings from coordinates
coordinates = list(filter(None, coordinates))
maxX = 0
maxY = 0
for coord in coordinates:
    coord = coord.split(", ")
    print(coord)
    coord[0] = int(coord[0])
    coord[1] = int(coord[1])
    if coord[0] > maxX:
        maxX = coord[0]
    if coord[1] > maxY:
        maxY = coord[1]

points = np.zeros((maxY+1, maxX+1), dtype=int)
ex_aequo = np.zeros((maxY+1, maxX+1), dtype=int)
infinite_areas =[]
areas = np.zeros(len(coordinates)+1)
for i in range(points.shape[0]):
    for j in range(points.shape[1]):
        dist = maxY*maxX
        closest_coord = -1
        print("point ",i,j)
        for coord in coordinates:
            coord_index = coordinates.index(coord)+1

            man_dist = manhattan_distance(j, i, coord.split(", "))
            if dist==man_dist:
                ex_aequo[i][j] = 1
            if dist>man_dist:
                dist = man_dist
                closest_coord = coord_index
                ex_aequo[i][j] = 0

        if ex_aequo[i][j]==1:
            points[i][j] = 0
        else:
            points[i][j] = closest_coord
            areas[closest_coord] += 1
        if i==0 or j==0 or i==maxY or j==maxX:
            infinite_areas.append(points[i][j])


def print_table():
    for i in range(points.shape[0]):
        for j in range(points.shape[1]):
            print(points[i][j],end=' ')
        print()


print_table()
maxArea = 0
for i in range(len(areas)):
    if areas[i]>maxArea and i not in infinite_areas:
        maxArea = areas[i]
print("The max area is",maxArea)

# Part 2
region_size = 0
for i in range(points.shape[0]):
    for j in range(points.shape[1]):
        distance_to_all_coords = 0
        print("point ",i,j)
        for coord in coordinates:
            man_dist = manhattan_distance(j, i, coord.split(", "))
            distance_to_all_coords += man_dist
        if distance_to_all_coords<10000:
            region_size += 1
print("The region size",region_size)