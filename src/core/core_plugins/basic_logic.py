from core.events import OnDraw, OnGameInit, EventsManager, OnMouseMotion
from core.plugin import Plugin
from core.runtime import Runtime

class BasicLogic(Plugin):
    def __init__(self, runtime: Runtime):
        super().__init__(runtime)
        self.subscriptions = {OnMouseMotion: self.on_mouse_motion, OnDraw: self.on_draw, OnGameInit: self.on_game_init}

    def setup(self):
        super().setup()

    def on_mouse_motion(self, event: OnMouseMotion):
        # realtime mouse position
        self.runtime.game.mouse_x = event.x
        self.runtime.game.mouse_y = event.y


    def on_draw(self, event: OnDraw):
        self.runtime.game.clear()

        for sprite in self.runtime.game.draw_list:
            sprite.draw()


    def on_game_init(self, event:OnGameInit):
        # we use a draw list to avoid problems
        # when multiple modules want to draw and clear the screen after previous module has drawn up
        self.runtime.game.draw_list = []

        self.runtime.game.mouse_x = 0
        self.runtime.game.mouse_y = 0