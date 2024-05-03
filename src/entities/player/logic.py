import arcade
from .player import Player
from core.events import (
    EventsManager,
    OnGameInit,
    OnKeyPress,
)
from utils.config import CELL_WIDTH, ROOT_PATH


def player_init(game, event: OnGameInit, em: EventsManager):
    game.player = Player(*game.map.center_index)

    game.player_sprite = arcade.Sprite(
        f"{ROOT_PATH}/../assets/detector.png",
        scale=0.15,
    )
    game.player_sprite.center_x = game.player.x * CELL_WIDTH + CELL_WIDTH / 2
    game.player_sprite.center_y = game.player.y * CELL_WIDTH + CELL_WIDTH / 2


def player_move(game, event: OnKeyPress, em: EventsManager):
    if event.key == arcade.key.S:
        game.player.y -= 1
        game.player_sprite.center_y -= CELL_WIDTH
    elif event.key == arcade.key.W:
        game.player.y += 1
        game.player_sprite.center_y += CELL_WIDTH
    elif event.key == arcade.key.A:
        game.player.x -= 1
        game.player_sprite.center_x -= CELL_WIDTH
    elif event.key == arcade.key.D:
        game.player.x += 1
        game.player_sprite.center_x += CELL_WIDTH


subscriptions = {
    OnGameInit: player_init,
    OnKeyPress: player_move,
}
