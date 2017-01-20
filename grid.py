from utils import create_grid, grid_spaces

# Grid class represents the state of the grid the robot is trying to move through
class Grid(object):
    
    # n_rows and n_cols are ints, the dimensions of the grid
    # obstacles is a list of tuples representing points on the grid
    # start and goal are tuples representing a point on the grid
    def __init__(self, n_rows, n_cols, obstacles, start, goal):
        self.grid = create_grid(n_rows, n_cols, grid_spaces['empty'])
        for obstacle in obstacles:
            self.grid[obstacle[0]][obstacle[1]] = grid_spaces['obstacle']
        self.start = start
        self.goal = goal
        self.find_path()

    # print the grid in a pleasant to look at way
    def display(self):
        for row in range(len(self.grid)):
            to_print = ''
            for col in range(len(self.grid[row])):
                if (row, col) == self.goal:
                    to_print += grid_spaces['goal']
                elif (row, col) == self.start:
                    to_print += grid_spaces['start']
                elif (row, col) in self.path:
                    to_print += grid_spaces['path']
                else:
                    to_print += self.grid[row][col]
            print to_print

    # check if a position is legal for a robot to move to.
    # returns True if the position is on the grid and is not an obstacle, False otherwise.
    def validate_position(self, coordinates):
        if coordinates[0] >= len(self.grid) or coordinates[1] >= len(self.grid[0]) \
           or coordinates[0] < 0 or coordinates[1] < 0 \
           or self.grid[coordinates[0]][coordinates[1]] == grid_spaces['obstacle']:
            return False
        else:
            return True

    # find shortest path from start to goal. strategy:
    # 1. make a queue of points to check, initially just the goal point
    # 2. make a map of distances of each point to the goal point. initially just goal point with distance 0
    # 3. go through each point in the queue. for each point:
    # 3a. make a list of neighboring points
    # 3b. remove neighbors that are off the grid, are obstacles, or have already been checked
    # 3c. add remaining neighbors to queue and their distances to the map (current distance + 1)
    # 3d. if the neighbor is the starting point, then we found a shortest path
    # 4. if no shortest path has been found, there is no path from start to goal
    # 5. to determine the path, make a list initially with only self.start. until we add goal to the list:
    # 5a. check the neighbors of the last added space until we find one whose distance is 1 less than the current distance
    # 5b. add that neighbor to the list and repeat
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
                if not self.validate_position(neighbor):
                    # neighbor is off the grid or an obstacle
                    continue
                if dist.get(neighbor) != None:
                    # neighbor has already been visited
                    continue
                if neighbor == self.start:
                    path_found = True
                queue.append(neighbor)
                dist[neighbor] = dist[current] + 1
            i += 1
        if not path_found:
            print 'No path exists'
            self.path = []
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
            



