from core.events import Event


class PlayerKilledEvent(Event):
    def __init__(self):
        super().__init__()


registrations = [PlayerKilledEvent]
