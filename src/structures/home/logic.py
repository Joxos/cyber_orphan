import arcade
from .home import Home
from core.events import (
    EventsManager,
    OnGameInit,
)
from utils.config import CELL_WIDTH, ASSETS_PATH


def home_init(game, event: OnGameInit, em: EventsManager):
    game.home = Home()

    game.home_sprite = arcade.Sprite(
        f"{ASSETS_PATH}/home.png",
        scale=0.08,
    )
    game.home_sprite.center_x = game.map.center_index[0] * CELL_WIDTH + CELL_WIDTH / 2
    game.home_sprite.center_y = game.map.center_index[1] * CELL_WIDTH + CELL_WIDTH / 2


subscriptions = {
    OnGameInit: home_init,
}
