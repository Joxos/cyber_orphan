from .player import Player


class Detector(Player):
    def __init__(self, x, y, yin=40, yang=30, sanity=1, max_sanity=15):
        super().__init__(x, y, yin, yang, sanity, max_sanity)
        self.image_path = "assets/detector.png"
