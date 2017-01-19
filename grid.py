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
start_grid_space = '='

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
        self.start = start
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
                elif (row, col) == self.start:
                    to_print += start_grid_space
                else:
                    to_print += self.grid[row][col]
            print to_print

    def find_path(self):
        queue = [self.goal]
        dist = {self.goal: 0}
        i = 0
        path_found = False
        while i < len(queue) and not path_found:
            current = queue[i]
            neighbors = [(current[0] + 1, current[1]), (current[0] - 1, current[1]),
                         (current[0], current[1] + 1), (current[0], current[1] - 1)]
            for neighbor in neighbors:
                if neighbor[0] >= len(self.grid) or neighbor[1] >= len(self.grid[0]) \
                or neighbor[0] < 0 or neighbor[1] < 0:
                    # neighbor is off the grid
                    continue
                if self.grid[neighbor[0]][neighbor[1]] == obstacle_grid_space:
                    # neighbor is an obstacle
                    continue
                if dist.get(neighbor) != None and dist[neighbor] < dist[current] + 1:
                    # neighbor has already been visited more efficiently
                    continue
                if neighbor == self.start:
                    path_found = True
                queue.append(neighbor)
                dist[neighbor] = dist[current] + 1
            i += 1
        if not path_found:
            print 'No path exists'
            return
        self.path = [self.start]
        while self.path[-1] != self.goal:
            current = self.path[-1]
            neighbors = [(current[0] + 1, current[1]), (current[0] - 1, current[1]),
                         (current[0], current[1] + 1), (current[0], current[1] - 1)]
            for neighbor in neighbors:
                if dist.get(neighbor) == dist[current] - 1:
                    self.path.append(neighbor)
                    break
            



