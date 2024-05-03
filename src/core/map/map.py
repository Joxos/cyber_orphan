from collections import deque


# map object
class Map:
    def __init__(self, row_count, column_count):
        self.map = deque(
            deque(0 for _ in range(column_count)) for _ in range(row_count)
        )
        self.center_index = (row_count // 2, column_count // 2)



if __name__ == "__main__":
    m = Map(10, 10, 123)
    print(m.map)
