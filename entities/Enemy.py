from entities.Entity import Entity


class Enemy(Entity):

    def __init__(self, x, y, width, color, speed):
        super().__init__(x, y, width, color)
        self.speed = speed

    def move_from_top(self, delta):
        self.y = self.y + delta

    def move_from_left(self, delta):
        self.x = self.x + delta

    def move_from_right(self, delta):
        self.x = self.x - delta
