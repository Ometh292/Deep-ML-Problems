'''
Easy
Linear Algebra

Write a Python function that reshapes a given matrix into a specified shape. if it cant be reshaped return back an empty list []
'''

import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	# Write your code here and return a python list after reshaping by using numpy's tolist() method

	a_array = np.array(a)
	reshaped_matrix = a_array.reshape(new_shape)
	reshaped_matrix_list = reshaped_matrix.tolist()

	return reshaped_matrix_list
