from loguru import logger
from utils.config import ROOT_PATH, SRC_PATH, ASSETS_PATH
import os
from core.events import OnKeyPress, OnKeyRelease, OnGameInit
from core.plugin import Plugin

from utils.utils import get_key_by_value


class Logging(Plugin):
    def __init__(self, runtime):
        super().__init__(runtime)
        self.subscriptions = {
            OnKeyPress: self.log_key_press,
            OnKeyRelease: self.log_key_release,
            OnGameInit: self.log_path_solving,
        }

    def setup(self):
        return super().setup()

    def log_key_press(self, event: OnKeyPress):
        logger.debug(f"Key pressed: {get_key_by_value(event.key)}")

    def log_key_release(self, event: OnKeyRelease):
        logger.debug(f"Key released: {get_key_by_value(event.key)}")

    def log_path_solving(self, event: OnGameInit):
        logger.debug("Path solved:")
        logger.debug(f"ROOT_PATH is {os.path.abspath(ROOT_PATH)}")
        logger.debug(f"SRC_PATH is {os.path.abspath(SRC_PATH)}")
        logger.debug(f"ASSETS_PATH is {os.path.abspath(ASSETS_PATH)}")
        logger.debug(f"Current working directory is {os.getcwd()}")

    # def log_left_mouse_press(game, event: OnLeftMousePress, em: EventsManager):
    #     if layout_manager.on_layout(LAYOUTS.GRID, event.x, event.y):
    #         row, column = coordinate_to_grid(event.x, event.y)
    #         logger.debug(
    #             f"Left mouse press on cell. Coordinates: ({event.x}, {event.y}). Grid coordinates: ({row}, {column}), Height: {game.map.height_map[row][column]}, Color: {game.cell_sprites_2d[row][column].color}"
    #         )
    #         return

    #     logger.debug(f"Left mouse press on sidebar. Coordinates: ({event.x}, {event.y}).")

    # def log_right_mouse_press(game, event: OnRightMousePress, em: EventsManager):
    #     if layout_manager.on_layout(LAYOUTS.GRID, event.x, event.y):
    #         row, column = coordinate_to_grid(event.x, event.y)
    #         logger.debug(
    #             f"Right mouse press on cell. Coordinates: ({event.x}, {event.y}). Grid coordinates: ({row}, {column}), Height: {game.map.height_map[row][column]}, Color: {game.cell_sprites_2d[row][column].color}"
    #         )
    #         return

    #     logger.debug(f"Right mouse press on sidebar. Coordinates: ({event.x}, {event.y}).")

    # def log_left_mouse_release(game, event: OnLeftMouseRelease, em: EventsManager):
    #     if layout_manager.on_layout(LAYOUTS.GRID, event.x, event.y):
    #         row, column = coordinate_to_grid(event.x, event.y)
    #         logger.debug(
    #             f"Left mouse release on cell. Coordinates: ({event.x}, {event.y}). Grid coordinates: ({row}, {column}), Height: {game.map.height_map[row][column]}, Color: {game.cell_sprites_2d[row][column].color}"
    #         )
    #         return

    #     logger.debug(f"Left mouse release on sidebar. Coordinates: ({event.x}, {event.y}).")

    # def log_right_mouse_release(game, event: OnRightMouseRelease, em: EventsManager):
    #     if layout_manager.on_layout(LAYOUTS.GRID, event.x, event.y):
    #         row, column = coordinate_to_grid(event.x, event.y)
    #         logger.debug(
    #             f"Right mouse release on cell. Coordinates: ({event.x}, {event.y}). Grid coordinates: ({row}, {column}), Height: {game.map.height_map[row][column]}, Color: {game.cell_sprites_2d[row][column].color}"
    #         )
    #         return

    #     logger.debug(
    #         f"Right mouse release on sidebar. Coordinates: ({event.x}, {event.y})."
    #     )
