from loguru import logger
from utils.config import ROOT_PATH, SRC_PATH, ASSETS_PATH
import os
from core.events import (
    OnKeyPress,
    OnKeyRelease,
    OnGameInit,
    OnLeftMousePress,
    OnLeftMouseRelease,
    OnRightMousePress,
    OnRightMouseRelease,
)
from utils.utils import coordinate_to_grid
from core.layout import layout_manager, LAYOUTS
from core.plugin import Plugin

from utils.utils import get_key_by_value


class Logging(Plugin):
    def __init__(self, runtime):
        super().__init__(runtime)
        self.subscriptions = {
            OnKeyPress: self.log_key_press,
            OnKeyRelease: self.log_key_release,
            OnGameInit: self.log_path_solving,
            OnLeftMousePress: self.log_left_mouse_press,
            OnRightMousePress: self.log_right_mouse_press,
            OnLeftMouseRelease: self.log_left_mouse_release,
            OnRightMouseRelease: self.log_right_mouse_release,
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

    def log_left_mouse_press(self, event: OnLeftMousePress):
        if layout_manager.on_layout(LAYOUTS.GRID, event.x, event.y):
            row, column = coordinate_to_grid(event.x, event.y)
            logger.debug(
                f"Left mouse press on cell. Coordinates: ({event.x}, {event.y}). Grid coordinates: ({row}, {column})"
            )
            return

        logger.debug(
            f"Left mouse press on sidebar. Coordinates: ({event.x}, {event.y})."
        )

    def log_right_mouse_press(self, event: OnRightMousePress):
        if layout_manager.on_layout(LAYOUTS.GRID, event.x, event.y):
            row, column = coordinate_to_grid(event.x, event.y)
            logger.debug(
                f"Right mouse press on cell. Coordinates: ({event.x}, {event.y}). Grid coordinates: ({row}, {column})"
            )
            return

        logger.debug(
            f"Right mouse press on sidebar. Coordinates: ({event.x}, {event.y})."
        )

    def log_left_mouse_release(self, event: OnLeftMouseRelease):
        if layout_manager.on_layout(LAYOUTS.GRID, event.x, event.y):
            row, column = coordinate_to_grid(event.x, event.y)
            logger.debug(
                f"Left mouse release on cell. Coordinates: ({event.x}, {event.y}). Grid coordinates: ({row}, {column})"
            )
            return

        logger.debug(
            f"Left mouse release on sidebar. Coordinates: ({event.x}, {event.y})."
        )

    def log_right_mouse_release(self, event: OnRightMouseRelease):
        if layout_manager.on_layout(LAYOUTS.GRID, event.x, event.y):
            row, column = coordinate_to_grid(event.x, event.y)
            logger.debug(
                f"Right mouse release on cell. Coordinates: ({event.x}, {event.y}). Grid coordinates: ({row}, {column})"
            )
            return

        logger.debug(
            f"Right mouse release on sidebar. Coordinates: ({event.x}, {event.y})."
        )
