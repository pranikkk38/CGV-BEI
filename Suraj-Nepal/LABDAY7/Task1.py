import numpy as np

def transform_2d(points, matrix):
    transformed_points = []
    for point in points:
        x, y = point
        transformed_point = np.dot(matrix, [x, y, 1])
        transformed_points.append((transformed_point[0], transformed_point[1]))
    return transformed_points

points = [(1, 2), (3, 4), (5, 6)]
matrix = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
transformed_points = transform_2d(points, matrix)
print(transformed_points)                           