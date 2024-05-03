import arcade
from core.events import (
    EventsManager,
    OnGameSetup,
)
from utils.utils import grid_to_central_coordinate
from utils.config import ROW_COUNT, COLUMN_COUNT


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
    OnGameSetup: map_setup,
}
