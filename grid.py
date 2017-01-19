# helper function to create a 2-d list
def create_grid(n_rows, n_cols, contents):
    result = []
    for row in range(n_rows):
        result.append([])
        for col in range(n_cols):
            result[row].append(contents)
    return result

# some constants for use in grids
empty_grid_space = '.'
obstacle_grid_space = 'X'
robot_grid_space = 'R'
goal_grid_space = '$'

# Grid class represents the state of the grid the robot is trying to move through
class Grid(object):
    
    # n_rows and n_cols are ints, the dimensions of the grid
    # obstacles is a list of tuples representing points on the grid
    # start and goal are tuples representing a point on the grid
    def __init__(self, n_rows, n_cols, obstacles, start, goal):
        self.grid = create_grid(n_rows, n_cols, empty_grid_space)
        for obstacle in obstacles:
            self.grid[obstacle[0]][obstacle[1]] = obstacle_grid_space
        self.robot_position = start
        self.goal = goal

    # print the grid in a pleasant to look at way
    def display(self):
        for row in range(len(self.grid)):
            to_print = ''
            for col in range(len(self.grid[row])):
                if (row, col) == self.robot_position:
                    to_print += robot_grid_space
                elif (row, col) == self.goal:
                    to_print += goal_grid_space
                else:
                    to_print += self.grid[row][col]
            print to_print
