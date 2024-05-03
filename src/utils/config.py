import os

# map configuration
# Set how many rows and columns we will have
ROW_COUNT = 20
COLUMN_COUNT = 20

# terrain configuration
TERRAIN_SCALE = 10
TERRAIN_COMPLEXITY = 100
TERRAIN_AMPLITUDE = 0.6
SEED = None

# display configuration
GAME_TITLE = "The Action"

# cell and boarder
CELL_WIDTH = 40

# sidebar
SIDEBAR_DEFAULT_FONT_SIZE = 15
SIDEBAR_WIDTH = 250
SIDEBAR_TEXT_X_MARGIN = 10
SIDEBAR_TEXT_Y_MARGIN = 10 + SIDEBAR_DEFAULT_FONT_SIZE
SIDEBAR_LINE_SPACING = 10 + SIDEBAR_DEFAULT_FONT_SIZE

# bottom sidebar
BOTTOM_SIDEBAR_FONT_SIZE = 12
BOTTOM_SIDEBAR_X_MARGIN = 10
BOTTOM_SIDEBAR_X_SPACING = 10
BOTTOM_SIDEBAR_Y_SPACING = 5
BOTTOM_SIDEBAR_HEIGHT = SIDEBAR_DEFAULT_FONT_SIZE + BOTTOM_SIDEBAR_Y_SPACING * 2

# grid and screen
GRID_WIDTH = CELL_WIDTH * COLUMN_COUNT
GRID_HEIGHT = CELL_WIDTH * ROW_COUNT
SCREEN_WIDTH = GRID_WIDTH
SCREEN_HEIGHT = GRID_HEIGHT

# consequence matters
# 1. game_logging is the first one for logging
# 2. when drawing, the order matters to determine which layer is on top
DEFAULT_MODULES = [
    "utils.game_logging",
    "core.basic_logic",
    "core.map",
    "structures.home",
    "entities.player",
]
LOG_LEVEL = "DEBUG"

# project structure
ROOT_PATH = os.path.join(os.path.dirname(__file__), "../..")
SRC_PATH = os.path.join(ROOT_PATH, "src")
ASSETS_PATH = os.path.join(ROOT_PATH, "assets")
