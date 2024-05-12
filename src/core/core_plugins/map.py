import arcade
from collections import deque
from core.runtime import Runtime
from entities.map_events.map_event import get_random_event_type
from utils.config import EVENT_PROBABILITY
from random import random
from utils.utils import grid_to_central_coordinate
from utils.game_logging import logger
from utils.config import ROW_COUNT, COLUMN_COUNT, CELL_WIDTH
from core.plugin import Plugin, PluginConfig
from core.events import OnGameSetup,OnDraw


class MapConfig(PluginConfig):
    def __init__(self, row_count, column_count, cell_width):
        self.row_count = row_count
        self.column_count = column_count
        self.cell_width = cell_width

class Map(Plugin):
    def __init__(self, runtime: Runtime):
        super().__init__(runtime)

    @property
    def registrations(self):
        return []
    
    @property
    def subscriptions(self):
        return {OnGameSetup: self.setup}

    def setup(self):
        super().setup()

        config = MapConfig(ROW_COUNT, COLUMN_COUNT, CELL_WIDTH)
        self.row_count = config.row_count
        self.column_count = config.column_count
        self.cell_width = config.cell_width
        self.map = deque(
            deque(0 for _ in range(self.column_count)) for _ in range(self.row_count)
        )
        self.center_index = (self.row_count // 2, self.column_count // 2)
        self.map_events = []

        # 1d list for arcade to render
        self.cell_sprites = arcade.SpriteList()
        # 2d list to control the game
        self.cell_sprites_2d = []

        # two basic textures for the cells
        self.texture_1 = arcade.make_soft_square_texture(
            self.cell_width, (193, 154, 107), outer_alpha=255
        )
        self.texture_2 = arcade.make_soft_square_texture(
            self.cell_width, (205, 166, 119), outer_alpha=255
        )

        # generate basic events
        self.generate_map_events()

        arcade.set_background_color(arcade.color.BLACK)

        for row in range(self.row_count):
            self.cell_sprites_2d.append([])
            for column in range(self.column_count):
                sprite = arcade.Sprite()
                sprite.center_x, sprite.center_y = grid_to_central_coordinate(row, column)
                if (row + column) % 2 == 0:
                    sprite.texture = self.texture_1
                else:
                    sprite.texture = self.texture_2
                self.cell_sprites.append(sprite)
                self.cell_sprites_2d[row].append(sprite)

        self.runtime.game.draw_list.append(self.cell_sprites)

        for map_event in self.map_events:
            map_event.sprite = arcade.Sprite(scale=0.06)
            (
                map_event.sprite.center_x,
                map_event.sprite.center_y,
            ) = grid_to_central_coordinate(map_event.location[0], map_event.location[1])
            map_event.sprite.texture = arcade.load_texture(map_event.image_path)
            self.draw_list.append(map_event.sprite)

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
