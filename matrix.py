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
        s += "*\n"

        return s
