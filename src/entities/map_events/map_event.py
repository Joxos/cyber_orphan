from random import randint, random
from utils.logger import logger
from utils.config import ASSETS_PATH


class MapEvent:
    def __init__(self, location, description):
        self.description = description
        self.location = location

    def interact(self):
        pass


class DeadlyGamblingMachine(MapEvent):
    def __init__(
        self,
        location,
        description="在废墟中意外发现的赌博机，好奇坐上去却没想到被绑住，看来只有战胜这台该死的机器才能脱身。",
    ):
        super().__init__(location, description)
        self.clip = [int(random() + 0.5) for _ in range(randint(4, 7))]
        self.image_path = f"{ASSETS_PATH}/deadly_gambling_machine.png"
        self.sprite = None
        logger.debug(f"Deadly gambling machine at {location} has clip {self.clip}")

    def interact(self):
        return super().interact()


class BurialPlace(MapEvent):
    def __init__(
        self,
        location,
        description="大量的遗体堆积于此，稀有材料概率大幅增加的同时有可能碰上残破遗骸",
    ):
        super().__init__(location, description)

    def interact(self):
        return super().interact()


rarities = {
    DeadlyGamblingMachine: 10,
}


def get_random_event_type():
    sum_weights = sum(rarities.values())
    choice = randint(0, sum_weights)
    weights = 0
    for event_type, weight in rarities.items():
        weights += weight
        if choice <= weights:
            return event_type


if __name__ == "__main__":
    for _ in range(10):
        print(get_random_event_type())
