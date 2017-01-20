from grid import Grid
from utils import grid_spaces, get_neighbors

# ExtendedGrid class is like the Grid class, but the robot can move diagonally
class ExtendedGrid(Grid):

    # find shortest path from start to goal, allowing diagonal movement. strategy:
    # 1. make a queue of points to check, initially just the goal point
    # 2. make a map of distances of each point to the goal point. initially just goal point with distance 0
    # 3. go through each point in the queue. for each point:
    # 3a. make a list of neighboring points
    # 3b. remove neighbors that are off the grid, are obstacles, or have already been visited at a shorter distance
    # 3c. add remaining neighbors to queue and their distances to the map
    #    (current distance + 1 for orthogonal neighbors or + sqrt(2) for diagonal neighbors)
    # 3d. if the neighbor is the starting point, then we found a shortest path
    # 4. if no shortest path has been found, there is no path from start to goal
    # 5. to determine the path, make a list initially with only self.start. until we add goal to the list:
    # 5a. check the neighbors of the last added space to find the one whose distance is smallest
    # 5b. add that neighbor to the list and repeat
    def find_path(self):
        queue = [self.goal]
        dist = {self.goal: 0}
        i = 0
        path_found = False
        while i < len(queue) and not path_found:
            current = queue[i]
            orthogonals = get_neighbors(current)
            diagonals = get_neighbors(current, True)
            for orthogonal in orthogonals:
                if not self.validate_position(orthogonal):
                    # orthogonal is off the grid or an obstacle
                    continue
                if dist.get(orthogonal) != None and dist[orthogonal] <= dist[current] + 1:
                    # we already found a faster path to orthogonal
                    continue
                if orthogonal == self.start:
                    path_found = True
                queue.append(orthogonal)
                dist[orthogonal] = dist[current] + 1
            for diagonal in diagonals:
                if not self.validate_position(diagonal):
                    # diagonal is off the grid or an obstacle
                    continue
                if dist.get(diagonal) != None and dist[diagonal] <= dist[current] + (2**.5):
                    # we already found a faster path to diagonal
                    continue
                if diagonal == self.start:
                    path_found = True
                queue.append(diagonal)
                dist[diagonal] = dist[current] + (2**.5)
            i += 1
        if not path_found:
            print 'No path exists'
            self.path = []
            return
        self.path = [self.start]
        while self.path[-1] != self.goal:
            current = self.path[-1]
            neighbors = get_neighbors(current) + get_neighbors(current, True)
            best_neighbor = None
            for neighbor in neighbors:
                if dist.get(neighbor) == None:
                    # neighbor is not part of the shortest path
                    continue
                if best_neighbor == None or dist[best_neighbor] > dist[neighbor]:
                    best_neighbor = neighbor
            self.path.append(best_neighbor)



