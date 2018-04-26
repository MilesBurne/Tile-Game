#Grid Game by Miles Burne 26/4/18
import random

class Grid():
    #constructor
    def __init__(self, ID, parent=0, side=3, last_move=0, grid=0):
        self.side_length = side
        if grid == 0:
            self.grid = self.make_grid()
        else:
            self.grid = grid
        self.parent = parent
        self.ID = ID
        self.children = []
        self.last_move = last_move
        
    #makes grid from list of numbers
    def make_grid(self):
        numbers = []
        row = []
        grid = []
        for x in range(0, ((self.side_length)**2)):
            numbers.append(x)
        for x in range(0, self.side_length):
            row = []
            for x in range(0, self.side_length):
                row.append(numbers.pop(random.randint(0, len(numbers)-1)))
            grid.append(row)
        return(grid)

    #use this to import a grid from the user
    def grid_import(self, grid):
        self.grid = grid

    #get grid in array format         
    def grid_get(self):
        return(self.grid)

    #returns the grid ID
    def get_ID(self):
        return(self.ID)

    #add a child
    def add_child(self,child):
        self.children.append(child)

    #returns the last move so the program will not get caught in a loop
    def get_move(self):
        return(self.last_move)

class Tree():
    #constructor
    def __init__(self, side=3):
        self.side_length = side
        self.start_grid = Grid(0,0,self.side_length)
        self.target_grid = self.get_target()
        self.end_grid = 0 #will be filled when found
        #now_tier will hold the tier currently being operated on, which will be added to when a new grid is 'found', and will be popped off when 'solved'
        self.now_tier = [self.start_grid]
        self.solution = False
        self.IDs = 1
        self.current_grid = self.start_grid
        

    #making the target grid so the program can know when its done
    def get_target(self):
        numbers = []
        row = []
        grid = []
        for x in range(0, ((self.side_length)**2)):
            numbers.append(x)
        for x in range(0, self.side_length):
            row = []
            for x in range(0, self.side_length):
                row.append(numbers.pop(0))
            grid.append(row)
        return(grid)

    def current_grid_pos(self):
        inner_pos = 0
        outer_pos = 0
        for x in self.current_grid.grid_get():
                try:
                    inner_pos = x.index(0)
                    outer_pos = self.current_grid.grid_get.index(x)
                except:
                    pass
        return(outer_pos, inner_pos)

    #moves '0' to the LEFT if possible
    def LEFT_MOVE(self):
        new_grid = []
        outer_pos, inner_pos = self.current_grid_pos()
        opposites = {"L":"R", "R":"L", "U":"D", "D":"U", 0:"patient 0"} #tell the program which moves are opposites
        number_carry = 0
        #recreating current_grid
        for x in self.current_grid.grid_get():
            row = []
            for y in x:
                row.append(y)
            new_grid.append(row)

        try:
            if opposites[current_grid.get_move()] == "L":
                "this breaks code"/1
            if inner_pos-1 <0:
                "this breaks code"/1
            number_carry = new_grid[outer_pos][inner_pos-1] #this is the number which is being moved
            new_grid[outer_pos][inner_pos-1] = 0 #0 is moved into place
            new_grid[outer_pos][inner_pos] = number_carry #number is moved into place
            #instansiating grid with new_grid
            grid = Grid(self.IDs, self.current_grid, self.side_length, "L", new_grid)
            self.current_grid.add_child(grid)
            self.now_tier.append(grid)
            if grid.grid_get() == self.target_grid:
                self.end_grid = grid
                self.solution = True
            self.IDs += 1
        except:
            pass

    #moves '0' to the RIGHT if possible
    def RIGHT_MOVE(self):
        new_grid = []
        outer_pos, inner_pos = self.current_grid_pos()
        opposites = {"L":"R", "R":"L", "U":"D", "D":"U", 0:"patient 0"} #tell the program which moves are opposites
        number_carry = 0
        #recreating current_grid
        for x in self.current_grid.grid_get():
            row = []
            for y in x:
                row.append(y)
            new_grid.append(row)


        try:
            if opposites[current_grid.get_move()] == "R":
                "this breaks code"/1
            number_carry = new_grid[outer_pos][inner_pos+1] #this is the number which is being moved
            new_grid[outer_pos][inner_pos+1] = 0 #0 is moved into place
            new_grid[outer_pos][inner_pos] = number_carry #number is moved into place
            #instansiating grid with new_grid
            grid = Grid(self.IDs, self.current_grid, self.side_length, "R", new_grid)
            self.current_grid.add_child(grid)
            self.now_tier.append(grid)
            if grid.grid_get() == self.target_grid:
                self.end_grid = grid
                self.solution = True
            self.IDs += 1
        except:
            pass

    #moves '0' UP if possible
    def UP_MOVE(self):
        new_grid = []
        outer_pos, inner_pos = self.current_grid_pos()
        opposites = {"L":"R", "R":"L", "U":"D", "D":"U", 0:"patient 0"} #tell the program which moves are opposites
        number_carry = 0
        #recreating current_grid
        for x in self.current_grid.grid_get():
            row = []
            for y in x:
                row.append(y)
            new_grid.append(row)


        try:
            if opposites[current_grid.get_move()] == "U":
                "this breaks code"/1
            if outer_pos-1 >0:
                "this breaks code"/1
            number_carry = new_grid[outer_pos-1][inner_pos] #this is the number which is being moved
            new_grid[outer_pos-1][inner_pos] = 0 #0 is moved into place
            new_grid[outer_pos][inner_pos] = number_carry #number is moved into place
            #instansiating grid with new_grid
            grid = Grid(self.IDs, self.current_grid, self.side_length, "U", new_grid)
            self.current_grid.add_child(grid)
            self.now_tier.append(grid)
            if grid.grid_get() == self.target_grid:
                self.end_grid = grid
                self.solution = True
            self.IDs += 1
        except:
            pass

    #moves '0' DOWN if possible
    def DOWN_MOVE(self):
        new_grid = []
        outer_pos, inner_pos = self.current_grid_pos()
        opposites = {"L":"R", "R":"L", "U":"D", "D":"U", 0:"patient 0"} #tell the program which moves are opposites
        number_carry = 0
        #recreating current_grid
        for x in self.current_grid.grid_get():
            row = []
            for y in x:
                row.append(y)
            new_grid.append(row)


        try:
            if opposites[current_grid.get_move()] == "D":
                "this breaks code"/1
            number_carry = new_grid[outer_pos+1][outer_pos] #this is the number which is being moved
            new_grid[outer_pos+1][inner_pos] = 0 #0 is moved into place
            new_grid[outer_pos][inner_pos] = number_carry #number is moved into place
            #instansiating grid with new_grid
            grid = Grid(self.IDs, self.current_grid, self.side_length, "D", new_grid)
            self.current_grid.add_child(grid)
            self.now_tier.append(grid)
            if grid.grid_get() == self.target_grid:
                self.end_grid = grid
                self.solution = True
            self.IDs += 1
        except:
            pass
            

    #program to actually create the tree
    def tree_create(self):
        '''
        RULES:
          - Program will not do the reverse of the previous move
          - Program can only move the '0' left, right, up or down
          - Program can have a max of 4 'solutions' per grid, and a min of 2
          - Program can only move if move is possible
          - Program will stop when a solution is found
        '''
        print(self.now_tier[0].grid_get())
        while self.solution == False:
            for x in self.current_grid.grid_get():
                print(x)
            print("\n")
            self.LEFT_MOVE()
            self.RIGHT_MOVE()
            self.UP_MOVE()
            self.DOWN_MOVE()
            self.current_grid = self.now_tier.pop(0)
            input()
            print(self.now_tier[0].grid_get())
            print(self.now_tier)
        #solution found
        print("Solution Found, it took", str(self.end_grid.get_ID()),"to find the solution")
        
        



tree = Tree()
tree.tree_create()
