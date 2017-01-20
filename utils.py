# helper function to create a 2-d list
def create_grid(n_rows, n_cols, contents):
    result = []
    for row in range(n_rows):
        result.append([])
        for col in range(n_cols):
            result[row].append(contents)
    return result

# some constants for drawing grids
grid_spaces = {
    'empty': '.',
    'obstacle': 'X',
    'goal': '$',
    'start': '+',
    'path': 'o'
}
