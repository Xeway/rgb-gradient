import math

def get_linear_gradient(colors, nb_points):
    def distance_3d(point1, point2):
        x1, y1, z1 = point1
        x2, y2, z2 = point2

        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

    gradient = []
    new_points = nb_points - len(colors)

    distances = [distance_3d(colors[i], colors[i]+1) for i in range(len(colors)-1)]
    global_distance = sum(distances)
    part_size = global_distance / (new_points+1)

    cum_distance = 0
    cum_part_size = part_size

    for i in range(len(colors)-1):
        a = colors[i]
        b = colors[i]+1

        l = b[0] - a[0]
        m = b[1] - a[1]
        n = b[2] - a[2]

        gradient.append(a)

        cum_distance += distances[i]

        while cum_distance >= cum_part_size:
            # gradient.append()
            cum_part_size += part_size

    gradient.append(colors[-1])