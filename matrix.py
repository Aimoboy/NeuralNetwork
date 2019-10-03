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
    
    @staticmethod
    def zero_matrix(rows, cols):
        if rows == 0 or cols == 0:
            raise Exception("Rows and columns have to be larger than zero.")

        values = []
        for i in range(rows):
            temp = []
            for j in range(cols):
                temp.append(0)
            values.append(temp)
        
        return Matrix(values)
    
    def __str__(self):
        # Settings
        space_between_elems = 1

        s = ""

        # Find the longest element
        longest_elem = 0
        for i in range(self.rows):
            for j in range(self.cols):
                l = len(str(self.values[i][j]))
                if l > longest_elem:
                    longest_elem = l
        
        # Draw top of box
        s += "*"
        s += "-" * (self.cols * longest_elem + (self.cols - 1) * space_between_elems)
        s += "*\n"

        # Draw middle of box
        for i in range(self.rows):
            s += "|"

            for j in range(self.cols):
                s += str(self.values[i][j])
                space_num = longest_elem - len(str(self.values[i][j]))
                s += " " * space_num
                if j != self.cols - 1:
                    s += " " * space_between_elems
                    

            s += "|\n"
        
        # Draw bottom of box
        s += "*"
        s += "-" * (self.cols * longest_elem + (self.cols - 1) * space_between_elems)
        s += "*"

        return s
    
    def __mul__(self, other):
        # If matrix
        if type(other) is Matrix:
            return self.multiply_matrix(other)
        
        # If scalar
        if type(other) is int or type(other) is float:
            return self.multiply_scalar(other)
    
    def __rmul__(self, other):
        # If scalar
        if type(other) is int or type(other) is float:
            return self.multiply_scalar(other)
    
    def multiply_matrix(self, m):
        # Check dimensions
        if self.cols != m.rows:
            raise Exception("Matrices have the wrong dimensions for multiplication.")

        # Calculate new matrix
        new_matrix = Matrix.zero_matrix(self.rows, m.cols)
        for i in range(new_matrix.rows):
            for j in range(new_matrix.cols):
                for k in range(self.cols):
                    new_matrix.values[i][j] += self.values[i][k] * m.values[k][j]
        
        # Return result
        return new_matrix
    
    def multiply_scalar(self, s):
        new_matrix = self.copy()

        # Multiply scalar
        for i in range(self.rows):
            for j in range(self.cols):
                new_matrix.values[i][j] *= s
        
        return new_matrix
    
    def copy(self):
        new_matrix = Matrix.zero_matrix(self.rows, self.cols)

        for i in range(self.rows):
            for j in range(self.cols):
                new_matrix.values[i][j] = self.values[i][j]
        
        return new_matrix

    def apply_function(self, f):
        new_matrix = self.copy()

        # Apply function
        for i in range(self.rows):
            for j in range(self.cols):
                new_matrix.values[i][j] = f(new_matrix.values[i][j])
        
        return new_matrix
