from core.events import (
    EventsManager,
    OnGameSetup,
)


def home_setup(game, event: OnGameSetup, em: EventsManager):
    game.draw_list.append(game.home_sprite)


subscriptions = {
    OnGameSetup: home_setup,
}
