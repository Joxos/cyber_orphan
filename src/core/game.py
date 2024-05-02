import arcade
from core.events import (
    OnGameSetup,
    OnDraw,
    OnMouseMotion,
    OnLeftMousePress,
    OnRightMousePress,
    OnLeftMouseRelease,
    OnRightMouseRelease,
    OnUpdate,
    OnKeyPress,
    OnGameInit,
    OnKeyRelease,
)


class Game(arcade.Window):
    def __init__(self, width, height, title, events_manager=None):
        super().__init__(width, height, title)
        self.events_manager = events_manager
        self.events_manager.set_game_ref(self)
        self.events_manager.new_event(OnGameInit())

    def setup(self):
        self.events_manager.new_event(OnGameSetup())

    def on_draw(self):
        self.events_manager.new_event(OnDraw())

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        self.events_manager.new_event(OnMouseMotion(x, y, delta_x, delta_y))

    def on_mouse_press(self, x, y, button, key_modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.events_manager.new_event(OnLeftMousePress(x, y, key_modifiers))
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            self.events_manager.new_event(OnRightMousePress(x, y, key_modifiers))

    def on_mouse_release(self, x, y, button, key_modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.events_manager.new_event(OnLeftMouseRelease(x, y, key_modifiers))
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            self.events_manager.new_event(OnRightMouseRelease(x, y, key_modifiers))

    def on_update(self, delta_time):
        self.events_manager.new_event(OnUpdate(delta_time))

    def on_key_press(self, key, key_modifiers):
        """
        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        self.events_manager.new_event(OnKeyPress(key, key_modifiers))

    def on_key_release(self, key, key_modifiers):
        self.events_manager.new_event(OnKeyRelease(key, key_modifiers))
