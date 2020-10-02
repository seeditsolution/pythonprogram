def getQuestion():
    """ Input question(9x9) to solve from user
        0 shows empty space """
    print("Enter the sudoku 9*9 grid\ntype 0 to denote empty space\nEach row is space separated 9 values\n")
    grid = []  #store the row in a line

    #entering the rows
    i=1
    while i < 10:
        row = input(f"Enter the {i} th row : ")
        row = list(map(int,row.strip().split(' ')))
        states = [x in range(10) for x in row]  #check for invalid numbers
        if len(row)!=9 or False in states:
            continue
        grid.append(row)
        i+=1

    return grid

def possibleValues(grid,r,c):
    """return the set of possible values at r,c of the grid
    """
    values = set(range(1,10))

    values -= set(grid[r])  #do not need to repeat row elements
    values -= set([grid[x][c] for x in range(9)]) #do not need to repeat column elements

    #calculating the 3*3 box coordinates
    if r in [0,1,2]:
        rows=[0,1,2]
    elif r in [3,4,5]:
        rows=[3,4,5]
    else:
        rows=[6,7,8]

    if c in [0,1,2]:
        cols=[0,1,2]
    elif c in [3,4,5]:
        cols=[3,4,5]
    else:
        cols=[6,7,8]

    values -= set([grid[i][j] for i in rows for j in cols])

    return values

def Solver(grid,r,c):
    """
    Recursive function to make use of backTracking
    Solves the grid at the position r and c if grid[r][c]==0
    else find the next zero. If the grid is full/solved, return true, else return false
    """
    while(grid[r][c]!=0): # find the position of element = 0
        c+=1
        if c==9:
            c=0
            r+=1
        if r==9:
            return True #there is no 0 element => grid is full

    for p in possibleValues(grid,r,c):
        grid[r][c]=p
        if Solver(grid,r,c) == True:
            return True
    grid[r][c]=0
    return False  #no possible solution

grid = getQuestion()
result = Solver(grid,0,0)
if result:
    print("Solution found as ")
    for r in grid:
        for c in r:
            print(c,end=" ")
        print()
else:
    print("No solution found!")
