'''
Easy
Linear Algebra

Write a Python function that calculates the mean of a matrix either by row or by column, based on a given mode. The function should take a matrix (list of lists) and a mode ('row' or 'column') as input and return a list of means according to the specified mode.
'''
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if mode == 'row':
		
		return [sum(row)/len(row) for row in matrix]

	elif mode == 'column':
	
		return [sum(col)/len(col) for col in zip(*matrix)]
	
	else:
		raise ValueError("Mode must be 'row' or 'column'")
	
