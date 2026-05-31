import numpy as np

def svd_2x2_singular_values(A: np.ndarray) -> tuple:
	
	a, b, c, d = A[0][0], A[0][1], A[1][0], A[1][1]

	A_T_A = A.T @ A # A transpose x A
	
	theta = 0.5 * np.arctan2(2 * A_T_A[0, 1], A_T_A[0, 0] - A_T_A[1, 1])
	J = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
	A_prime = J.T @ A_T_A @ J 
	# Calculate singular values from the diagonalized A^TA (approximation for 2x2 case)
	singular_values = np.sqrt(np.diag(A_prime))

	return J, singular_values, J.T
