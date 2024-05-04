from collections import deque
from entities.map_events.map_event import get_random_event_type
from utils.config import EVENT_PROBABILITY
from random import random
from utils.game_logging import logger


# map object
class Map:
    def __init__(self, row_count, column_count):
        self.map = deque(
            deque(0 for _ in range(column_count)) for _ in range(row_count)
        )
        self.row_count = row_count
        self.column_count = column_count
        self.center_index = (row_count // 2, column_count // 2)
        self.map_events = []

    def generate_map_events(self):
        # every grid has a 1/EVENT_PROBABILITY chance of having an event using MapEventType.get_random_event_type()
        for row in range(self.row_count):
            for column in range(self.column_count):
                if self.map[row][column] == 0 and random() < EVENT_PROBABILITY:
                    event_type = get_random_event_type()
                    logger.debug(
                        f"Generated event at {row, column} with type {event_type.__name__}"
                    )
                    self.map_events.append(event_type((row, column)))


if __name__ == "__main__":
    m = Map(10, 10, 123)
    print(m.map)
