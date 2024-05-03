from core.events import (
    EventsManager,
    OnGameSetup,
)


def player_setup(game, event: OnGameSetup, em: EventsManager):
    game.draw_list.append(game.player_sprite)


subscriptions = {
    OnGameSetup: player_setup,
}
