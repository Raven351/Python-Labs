class Matrix:
    def __init__ (self, x, y): #init matrix
        self.x = x #rows number
        self.y = y #column number
        self.rows = [] #rows array
        self.createRows(x,y) #creates rows and columns
        print("Created ",x,"x",y," matrix.")

    def createRows(self, x, y): #creates rows and columns, fills them with word "empty"
        i = 0
        j = 0
        values = [] #temp array to copy values from
        for i in range(x): #for every row
            for j in range (y): #for every column in row
                values.append("empty")
                j += 1
            self.rows.append(values.copy()) #add values to self.rows array
            values.clear()   #clear values array for next loop (i)
            i += 1

    def printMatrix(self): #to do
        for i in self.rows:
            print(" | ".join(map(str,i)))
            #print(*i, sep = " | ")

    def addRow(self, vRow, rowNum): #adds row to a matrix
        if (len(vRow) == self.y) & (rowNum == self.x): #check if array count and column number are even
            for i in range(self.y): #for every element in row / for every column
                self.rows[rowNum][i] = vRow[i] #add element in specified row (rowNum)
        else:
            print("Wrong number of row or number of elements in array is not even to number of columns in matrix.")


m = Matrix(4,2)
r1 = [1, 2]
m.addRow(r1, 5)
m.printMatrix()
#print(m.rows[0][0])
#m.rows[0][0] = "not empty"
#m.printMatrix()



#class Row:
