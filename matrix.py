class Matrix:
	def __init__(self, values):
		self.values = values
		self.rows, self.cols = Matrix.check_matrix(values)
	
	@staticmethod
	def check_matrix(values):
		if len(values) == 0:
			raise Exception("Matrix does not contain any rows.")
		
		m = len(values)
		n = len(values[0])
		
		# Check if it is square
		for i in range(m):
			if len(values[i]) != n:
				raise Exception("Matrix does not have equal amount of columns in every row.")
		
		# Return size of matrix
		return m, n
