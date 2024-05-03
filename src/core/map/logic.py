import arcade
from .map import Map
from core.events import (
    EventsManager,
    OnGameInit,
)
from utils.config import ROW_COUNT, COLUMN_COUNT, CELL_WIDTH


def map_init(game, event: OnGameInit, em: EventsManager):
    game.map = Map(ROW_COUNT, COLUMN_COUNT)

    # 1d list for arcade to render
    game.cell_sprites = arcade.SpriteList()

    # 2d list to control the game
    game.cell_sprites_2d = []

    # two basic textures for the cells
    game.texture_1 = arcade.make_soft_square_texture(
        CELL_WIDTH, (193, 154, 107), outer_alpha=255
    )
    game.texture_2 = arcade.make_soft_square_texture(
        CELL_WIDTH, (205, 166, 119), outer_alpha=255
    )


subscriptions = {
    OnGameInit: map_init,
}
