from enum import Enum, auto
from utils.config import (
    GRID_WIDTH,
    GRID_HEIGHT,
)


class LAYOUTS(Enum):
    GRID = auto()
    RIGHT_SIDEBAR = auto()
    BOTTOM_SIDEBAR = auto()


class Layout:
    def __init__(self, name, start_x, start_y, width, height):
        self.name = name
        self.start_x = start_x
        self.start_y = start_y
        self.width = width
        self.height = height


class LayoutManager:
    def __init__(self):
        self.layouts = {}

    def add_layout(self, layout: Layout):
        self.layouts[layout.name] = layout

    def on_layout(self, layout_name, x, y):
        layout = self.layouts.get(layout_name)
        if (
            x >= layout.start_x
            and x <= layout.start_x + layout.width
            and y >= layout.start_y
            and y <= layout.start_y + layout.height
        ):
            return layout_name
        return None

    def get_layouts_below(self, x, y):
        layouts = []
        for layout in self.layouts:
            result = self.on_layout(layout.name, x, y)
            if result is not None:
                layouts.append(result)
        return layouts


layout_manager = LayoutManager()
layout_manager.add_layout(Layout(LAYOUTS.GRID, 0, 0, GRID_WIDTH, GRID_HEIGHT))
