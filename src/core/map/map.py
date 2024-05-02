# map object
class Map:
    def __init__(self, row_count, column_count, seed):
        self.map_grid = [[0 for j in range(column_count)] for i in range(row_count)]
