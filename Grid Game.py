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
        print(self.now_tier)
        self.solution = False
        self.IDs = 1
        self.current_grid = start_grid
        

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
        for x in current_grid.grid_get():
                try:
                    inner_pos = x.index(0)
                    outer_pos = current_grid.grid_get.index(x)
                except:
                    pass
        return(outer_pos, inner_pos)

    #moves '0' to the LEFT if possible
    def LEFT_MOVE(self):
        opposites = {"L":"R", "R":"L", "U":"D", "D":"U", 0:"patient 0"} #tell the program which moves are opposites
        number_carry = 0
        new_grid = current_grid
        try:
            #if opposites[current_grid.get_move()] == "L":
                #"this breaks code"/1
            if inner_pos-1 <0:
                "this breaks code"/1
            number_carry = new_grid[outer_pos][inner_pos-1] #this is the number which is being moved
            new_grid[outer_pos][inner_pos-1] = 0 #0 is moved into place
            new_grid[outer_pos][inner_pos] = number_carry #number is moved into place
            return(new_grid)
        except:
            return(0)

    #moves '0' to the RIGHT if possible
    def RIGHT_MOVE(self):
        opposites = {"L":"R", "R":"L", "U":"D", "D":"U", 0:"patient 0"} #tell the program which moves are opposites
        number_carry = 0
        new_grid = current_grid
        #opposites[current_grid.get_move()]
        try:
            #if opposites[current_grid.get_move()] == "R":
                #"this breaks code"/1
            number_carry = new_grid[outer_pos][inner_pos+1] #this is the number which is being moved
            new_grid[outer_pos][inner_pos+1] = 0 #0 is moved into place
            new_grid[outer_pos][inner_pos] = number_carry #number is moved into place
            return(new_grid)
        except:
            return(0)

    #moves '0' UP if possible
    def UP_MOVE(self):
        opposites = {"L":"R", "R":"L", "U":"D", "D":"U", 0:"patient 0"} #tell the program which moves are opposites
        number_carry = 0
        new_grid = current_grid
        try:
           # if opposites[current_grid.get_move()] == "U":
               # "this breaks code"/1
            if outer_pos-1 >0:
                "this breaks code"/1
            number_carry = new_grid[outer_pos-1][inner_pos] #this is the number which is being moved
            new_grid[outer_pos-1][inner_pos] = 0 #0 is moved into place
            new_grid[outer_pos][inner_pos] = number_carry #number is moved into place
            return(new_grid)
        except:
            return(0)

    #moves '0' DOWN if possible
    def DOWN_MOVE(self):
        opposites = {"L":"R", "R":"L", "U":"D", "D":"U", 0:"patient 0"} #tell the program which moves are opposites
        number_carry = 0
        new_grid = current_grid
        try:
            #if opposites[current_grid.get_move()] == "D":
               # "this breaks code"/1
            number_carry = new_grid[outer_pos+1][outer_pos] #this is the number which is being moved
            new_grid[outer_pos+1][inner_pos] = 0 #0 is moved into place
            new_grid[outer_pos][inner_pos] = number_carry #number is moved into place
            return(new_grid)
        except:
            return(0)
            






    def make_move(self):
        '''
        RULES:
          - Program will not do the reverse of the previous move
          - Program can only move the '0' left, right, up or down
          - Program can have a max of 4 'solutions' per grid, and a min of 2
          - Program can only move if move is possible
          - Program will stop when a solution is found
        '''

        LEFT_MOVE()
        RIGHT_MOVE()
        UP_MOVE()
        DOWN_MOVE()
        








        
        '''
        IDs = 1
        solution_grids = [] #2d array to store the new moves
        print("origiaonakl")
        for y in self.now_tier[0].grid_get():
            print(y)
        input()
        while self.solution != True:
            print("New parent")
            current = self.now_tier.pop(0)
            current_grid = current.grid_get()
            for x in current_grid:
                try:
                    inner_pos = x.index(0)
                    outer_pos = current_grid.index(x)
                    print(inner_pos, outer_pos)
                except:
                    pass
            
            #LEFT MOVE
            left_grid = self.LEFT_MOVE(current_grid, inner_pos, outer_pos)
            print("left", left_grid)
            #if left_grid != 0:
                #solution_grids.append([left_grid, "L"])
                
            #RIGHT MOVE
            right_grid = self.RIGHT_MOVE(current_grid, inner_pos, outer_pos)
            print("right", right_grid)
            #if right_grid != 0:
                #solution_grids.append([right_grid, "R"])
            #UP MOVE
            up_grid = self.UP_MOVE(current_grid, inner_pos, outer_pos)
            print("up", up_grid)
            #if up_grid != 0:
                #solution_grids.append([up_grid, "U"])
            #DOWN MOVE
            down_grid = self.DOWN_MOVE(current_grid, inner_pos, outer_pos)
            print("down", down_grid)
            #if down_grid != 0:
                #solution_grids.append([down_grid, "D"])
            #print(solution_grids)
            print(current.grid_get())
            
            for x in solution_grids:
                if x == self.target_grid:
                    #Solution Found!
                    print("Solution Found")
                    self.solution = True
                    self.end_grid = x
                grid = Grid(IDs, current_grid, self.side_length, x[1], x[0])
                current_grid.add_child(grid)
                IDs += 1
                self.now_tier.append(grid)
                print("solution")
            
            if right_grid != 0:
                grid = Grid(IDs, current_grid, self.side_length, "R", right_grid)
                current.add_child(right_grid)
                IDs += 1
                print("\nRight:")
                for y in right_grid:
                    print(y)
                input()

            if left_grid != 0:
                grid = Grid(IDs, current_grid, self.side_length, "L", left_grid)
                current.add_child(left_grid)
                IDs += 1
                print("\nLeft:")
                for y in left_grid:
                    print(y)
                input()

            if up_grid != 0:
                grid = Grid(IDs, current_grid, self.side_length, "U", up_grid)
                current.add_child(up_grid)
                IDs += 1
                print("\nUp:")
                for y in up_grid:
                    print(y)
                input()

            if down_grid != 0:
                grid = Grid(IDs, current_grid, self.side_length, "D", down_grid)
                current.add_child(down_grid)
                IDs += 1
                print("\nDown:")
                for y in down_grid:
                    print(y)
                input()

            solution_grids = []
            '''
            
            
            
            
            
            
        
tree = Tree()
tree.make_move()

























