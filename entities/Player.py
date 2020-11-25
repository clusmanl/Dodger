from entities.Entity import Entity


class Player(Entity):

    def move(self, delta):
        self.x = self.x + delta
