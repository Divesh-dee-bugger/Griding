


class Grid:



    def __init__(self, col, row):
        self.row = row
        self.col = col
        self.lines = set()


        self.grid = [

        ]

        for i in range(0, self.row):
            self.grid.append([])

            for j in range(0, self.col):
                self.grid[i].append("")



    def _validate(self, col=0, row=0):

        # print(row, col)

        if row > self.row+1:
            raise IndexError("Cell not found!")
        
        elif col > self.col+1:
            raise IndexError("Cell not found!")
        
    


    def addVal(self, row, col, val=""):

        self._validate(row, col)

        if self.grid[col-1][row-1] != "":
            raise ValueError("The cell aready has a value!")
        
        else:
            self.grid[col-1][row-1] = val



    def changeVal(self, row, col, val):
        
        self._validate(row, col)

        if self.grid[col-1][row-1] == "":
            raise ValueError("The cell is already empty!")
        
        else:
            self.grid[col-1][row-1] = val



    def remVal(self, row, col):
        
        self._validate(row, col)

        if self.grid[col-1][row-1] == "":
            raise ValueError("The cell is already empty!")
        
        else:
            self.grid[col-1][row-1] = ""



    def printGrid(self):

        col_widths = [0] * self.col

        # Step 1: calculate column widths
        for row in self.grid:
            for i in range(self.col):
                val = row[i] if row[i] != "" else "."
                col_widths[i] = max(col_widths[i], len(val))

        # Step 2: create horizontal line
        line = "+"
        for w in col_widths:
            line += "-" * (w + 2) + "+"

        print(line)

        # Step 3: print rows
        for idx, row in enumerate(self.grid):

            print("|", end="")
            for i in range(self.col):
                val = row[i] if row[i] != "" else "."
                print(f" {val:<{col_widths[i]}} |", end="")
            print()

            # Step 4: print line if needed
            if (idx + 1) in self.lines:
                print(line)

        print(line)



    def addLine(self, row):
        if not (1 <= row <= self.row):
            raise IndexError("Invalid row for line placement!")
        
        self.lines.add(row)



    def clear(self):
        for i in range(0, self.row):
            for j in range(0, self.col):
                self.grid[i][j] = ""



    def getVal(self, row, col):
        
        self._validate(row, col)

        return self.grid[col-1][row-1]
    
    

    def getRow(self, row):

        self._validate(row=row)

        return self.grid[row-1]
    


    def getCol(self, col):

        self._validate(col=col)

        column = []
        
        for i in range(0, len(self.grid)):
            item = self.grid[i][col-1]
            column.append(item)

        # "::".join(column)   TODO: Later

        return list(column)
    
    


    def findVal(self, val):

        results = []

        for i in range(self.row):
            for j in range(self.col):

                if self.grid[i][j] == val:
                    results.append((j+1, i+1))   # (x, y)

        return results
    

            

    



