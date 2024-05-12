import os

# map configuration
# Set how many rows and columns we will have
ROW_COUNT = 20
COLUMN_COUNT = 20

# map events
EVENT_PROBABILITY = 0.01

# display configuration
GAME_TITLE = "Light and Darkness"

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

LOG_LEVEL = "DEBUG"

# project structure
ROOT_PATH = os.path.join(os.path.dirname(__file__), "../..")
SRC_PATH = os.path.join(ROOT_PATH, "src")
ASSETS_PATH = os.path.join(ROOT_PATH, "assets")
PLUGINS_PATH = os.path.join(SRC_PATH, "core", "core_plugins")
