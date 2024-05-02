import arcade
from core.map.map import Map
from core.events import (
    EventsManager,
    OnGameInit,
    OnGameSetup,
)
from utils.utils import grid_to_central_coordinate
from utils.config import ROW_COUNT, COLUMN_COUNT, CELL_WIDTH, SEED


def map_init(game, event: OnGameInit, em: EventsManager):
    game.map = Map(ROW_COUNT, COLUMN_COUNT, SEED)

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


def map_setup(game, event: OnGameSetup, em: EventsManager):
    arcade.set_background_color(arcade.color.BLACK)

    for row in range(ROW_COUNT):
        game.cell_sprites_2d.append([])
        for column in range(COLUMN_COUNT):
            sprite = arcade.Sprite()
            sprite.center_x, sprite.center_y = grid_to_central_coordinate(row, column)
            if (row + column) % 2 == 0:
                sprite.texture = game.texture_1
            else:
                sprite.texture = game.texture_2
            game.cell_sprites.append(sprite)
            game.cell_sprites_2d[row].append(sprite)

    game.draw_list.append(game.cell_sprites)


subscriptions = {
    OnGameInit: map_init,
    OnGameSetup: map_setup,
}
