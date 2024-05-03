class Player:
    def __init__(self, x, y, yin, yang, sanity, max_sanity):
        self.x = x
        self.y = y
        self.yin = yin
        self.yang = yang
        self.sanity = sanity
        self.max_sanity = max_sanity

    def yang_damage(self, amount):
        self.yang -= amount
