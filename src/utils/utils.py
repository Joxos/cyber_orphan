from utils.config import (
    CELL_WIDTH,
    SIDEBAR_WIDTH,
    BOTTOM_SIDEBAR_HEIGHT,
    COLUMN_COUNT,
    ROW_COUNT,
    GAME_TITLE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    PLUGINS_PATH,
)
from core.layout import layout_manager, LAYOUTS
from core.runtime import Runtime
from core.events import EventsManager, DEFAULT_EVENT_LIST
from core.plugin import PluginManager
from core.game import Game
import arcade


def mix_color(a, b):
    return ((a[0] + b[0]) // 2, (a[1] + b[1]) // 2, (a[2] + b[2] // 2))


def grid_to_central_coordinate(row, column):
    x = (
        column * CELL_WIDTH  # column starts from 0
        + CELL_WIDTH / 2
    )
    y = (
        row * CELL_WIDTH  # row starts from 0
        + CELL_WIDTH / 2
    )
    return [x, y]


def coordinate_to_grid(x, y):
    if layout_manager.on_layout(LAYOUTS.GRID, x, y):
        column = (x - SIDEBAR_WIDTH) // CELL_WIDTH
        row = (y - BOTTOM_SIDEBAR_HEIGHT) // CELL_WIDTH
        if column < COLUMN_COUNT and row < ROW_COUNT:
            return [row, column]
        else:
            return [row - 1, column - 1]


def row_column_on_grid(row, column):
    if row < 0 or row >= ROW_COUNT or column < 0 or column >= COLUMN_COUNT:
        return False
    return True


def get_whole_runtime():
    runtime, plugin_manager, events_manager, game = (
        Runtime(),
        PluginManager(),
        EventsManager(),
        Game(SCREEN_WIDTH, SCREEN_HEIGHT, GAME_TITLE),
    )
    events_manager.runtime, runtime.events_manager = runtime, events_manager
    runtime.game, game.runtime = game, runtime
    plugin_manager.runtime, runtime.plugin_manager = runtime, plugin_manager

    events_manager.register(DEFAULT_EVENT_LIST)
    plugin_manager.load_plugins(PLUGINS_PATH)
    plugin_manager.setup_plugins()
    game.setup()
    return runtime, plugin_manager, events_manager, game


def get_key_by_value(value):
    for key, val in arcade.key.__dict__.items():
        if val == value:
            return key
    return None
