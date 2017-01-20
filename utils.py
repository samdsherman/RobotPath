# helper function to create a 2-d list
def create_grid(n_rows, n_cols, contents):
    result = []
    for row in range(n_rows):
        result.append([])
        for col in range(n_cols):
            result[row].append(contents)
    return result

# helper function to get the neighbors of a point on a grid
def get_neighbors(coordinates, diagonal = False):
    if diagonal:
        return [(coordinates[0] + 1, coordinates[1] + 1), (coordinates[0] - 1, coordinates[1] - 1),
                (coordinates[0] + 1, coordinates[1] - 1), (coordinates[0] - 1, coordinates[1] + 1)]
    else:
        return [(coordinates[0], coordinates[1] + 1), (coordinates[0], coordinates[1] - 1),
                (coordinates[0] + 1, coordinates[1]), (coordinates[0] - 1, coordinates[1])]

# some constants for drawing grids
grid_spaces = {
    'empty': '.',
    'obstacle': 'X',
    'goal': '$',
    'start': '+',
    'path': 'o'
}
