#Grid Game by Miles Burne 26/4/18
#imports
import random
import time
import math

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

    def get_parent(self):
        return(self.parent)

class Tree():
    #constructor
    def __init__(self):
        self.user_grid, self.side_length = self.user_grid_get()
        #self.side_length = side
        self.start_grid = Grid(0,0,self.side_length, 0, self.user_grid)
        self.target_grid = self.get_target()
        self.end_grid = 0 #will be filled when found
        #now_tier will hold the tier currently being operated on, which will be added to when a new grid is 'found', and will be popped off when 'solved'
        self.now_tier = [self.start_grid]
        self.solution = False
        self.IDs = 1
        self.current_grid = []
        self.visited = []
        

    def user_grid_get(self):
        size_input = True
        number_in = True
        q = input("Would you like to use your own grid? Please type Y or N:\n")
        if q.strip(" ") == "Y" or q.strip(" ") == "y":
            #getting grid size
            while size_input == True:
                size = input("Please enter a size for the side:\n")
                try:
                    size = int(size)
                    size_input = False
                except:
                    print("Please enter an integer")

            #getting all the possible numbers
            numbers = []
            for x in range(0, ((size)**2)):
                numbers.append(x)

            #getting the grid
            print("Please enter each integer in row by row format. The program will inform you of each new row.")
            grid = []
            for x in range(0, size):
                row = []
                print("Row",x,":\n")
                for x in range(0, size):
                    number_in = True
                    while number_in == True:
                        numb = input()
                        try:
                            index = numbers.index(int(numb))
                            numbers.pop(index)
                            row.append(int(numb))
                            number_in = False
                        except:
                            print("Integer must be between and include 0 &", (size**2)-1, "and not be used twice or more.")
                            print("Please enter that integer again.\n")
                grid.append(row)
            print("Grid entered successfully")
            return(grid, size)
        else:
            #getting grid size
            while size_input == True:
                size = input("Please enter a size for the side:\n")
                try:
                    size = int(size)
                    size_input = False
                except:
                    print("Please enter an integer")
            return(0, size)
            








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
                    outer_pos = self.current_grid.grid_get().index(x)
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
            if opposites[self.current_grid.get_move()] == "L":
                "this breaks code"/1
            if inner_pos-1 <0:
                "this breaks code"/1

            number_carry = new_grid[outer_pos][inner_pos-1] #this is the number which is being moved
            new_grid[outer_pos][inner_pos-1] = 0 #0 is moved into place
            new_grid[outer_pos][inner_pos] = number_carry #number is moved into place
            #checking for duplicates
            if new_grid in self.visited:
                pass
            else:
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
            if opposites[self.current_grid.get_move()] == "R":
                "this breaks code"/1
            number_carry = new_grid[outer_pos][inner_pos+1] #this is the number which is being moved
            new_grid[outer_pos][inner_pos+1] = 0 #0 is moved into place
            new_grid[outer_pos][inner_pos] = number_carry #number is moved into place
            #checking for duplicates
            if new_grid in self.visited:
                pass
            else:
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
            if opposites[self.current_grid.get_move()] == "U":
                "this breaks code"/1 #1
            if outer_pos-1 <0:
                "this breaks code"/1
            number_carry = new_grid[outer_pos-1][inner_pos] #this is the number which is being moved
            new_grid[outer_pos-1][inner_pos] = 0 #0 is moved into place
            new_grid[outer_pos][inner_pos] = number_carry #number is moved into place
            #checking for duplicates
            if new_grid in self.visited:
                pass
            else:
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
            if opposites[self.current_grid.get_move()] == "D":
                "this breaks code"/1
            number_carry = new_grid[outer_pos+1][outer_pos] #this is the number which is being moved
            new_grid[outer_pos+1][inner_pos] = 0 #0 is moved into place
            new_grid[outer_pos][inner_pos] = number_carry #number is moved into place
            #checking for duplicates
            if new_grid in self.visited:
                pass
            else:
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
        #getting times for reference
        times = time.localtime()
        print("The time is", str(times[3])+":"+str(times[4])+":"+str(times[5])+"\n")
        #showing number of combinations
        print("For this grid there are", math.factorial(self.side_length**2),"combinations")
        #displaying the initial grid to the user
        print("Initial Grid:")
        for x in self.now_tier[0].grid_get():
                print(x)
        print("\nSolving...")
        while self.solution == False:
            self.current_grid = self.now_tier.pop(0)
            self.visited.append(self.current_grid.grid_get())
            '''
            for x in self.current_grid.grid_get():
                print(x)
            print("\n")
            '''
            self.LEFT_MOVE()
            self.RIGHT_MOVE()
            self.UP_MOVE()
            self.DOWN_MOVE()
            if self.IDs%10000 == 0:
                print("Node number", self.IDs, "reached.")
            
        #solution found
        self.solution_found()

    #runs when the program reaches is target
    def solution_found(self):
        moves = {"L":"Left","R":"Right","U":"Up","D":"Down", 0:"Initial"}
        patient_0_f = False
        solve_route = []
        parent = self.end_grid
        while patient_0_f == False:
            solve_route.append(parent)
            if parent.get_move() == 0:
                patient_0_f = True
            parent = parent.get_parent()
        print("Solution found in", self.end_grid.get_ID(), "grids and",len(solve_route),"moves")
        print("Moves are:\n")
        for x in range(0, len(solve_route)):
            display_grid = solve_route.pop(len(solve_route)-1)
            print(" ",moves[display_grid.get_move()])
            print("\n")
            for x in display_grid.grid_get():
                print(x)
            print("\n")
            
        



tree = Tree()
tree.tree_create()
