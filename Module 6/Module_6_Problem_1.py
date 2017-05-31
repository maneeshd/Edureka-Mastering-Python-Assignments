"""
@author: Maneesh D
@date: 29-May-17
@intepreter: Python 3.6

Consider a random 10 x 2 matrix representing Cartesian coordinates, convert them to Polar coordinates.
"""
import math

import numpy

numpy.set_printoptions(precision=2)
cartesian_matrix = numpy.random.randint(0, 9, size=(10, 2))

print(cartesian_matrix.shape)
print("Cartesian Co-ordinate matrix:")
print(cartesian_matrix)

# Converting to polar co-ordinates
polar_matrix = numpy.empty(shape=cartesian_matrix.shape, dtype=float)
for i in range(cartesian_matrix.shape[0]):
    row_data = cartesian_matrix[i]
    r = ((row_data[0] ** 2) + (row_data[1] ** 2)) ** 0.5
    phi = math.atan2(row_data[1], row_data[0])
    polar_matrix[i] = [r, phi]


print("Polar co-ordinate matrix:")
print(polar_matrix)
