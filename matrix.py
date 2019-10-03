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

	def draw(self):
		# Settings
		space_between_elems = 1

		# Find the longest element
		longest_elem = 0
		for i in range(self.rows):
			for j in range(self.cols):
				l = len(str(self.values[i][j]))
				if l > longest_elem:
					longest_elem = l
		
		# Draw top of box
		print("*", end="")
		print("-" * (self.cols * longest_elem + (self.cols - 1) * space_between_elems), end="")
		print("*")

		# Draw middle of box
		for i in range(self.rows):
			print("|", end="")

			for j in range(self.cols):
				print(self.values[i][j], end="")
				space_num = longest_elem - len(str(self.values[i][j]))
				print(" " * space_num, end="")
				if j != self.cols - 1:
					print(" " * space_between_elems, end="")
					

			print("|")
		
		# Draw bottom of box
		print("*", end="")
		print("-" * (self.cols * longest_elem + (self.cols - 1) * space_between_elems), end="")
		print("*")
