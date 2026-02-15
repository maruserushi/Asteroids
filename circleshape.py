import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, live, damage):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        self.live = live
        self.damage = damage
        self.armor = 0

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

    def take_damage(self, other):
        damage_taken = other.damage
        if self.armor > 0:
            if self.armor >= damage_taken:
                self.armor -= damage_taken
                damage_taken = 0
            elif self.armor < damage_taken:
                self.armor = 0
                damage_taken = damage_taken - self.armor
        if damage_taken > 0:
            self.live -= damage_taken
            if self.live <= 0:
                return True
            else:
                return False

    def collides_with(self, other):
        distance = self.position.distance_to(other.position)
        if distance <= (self.radius + other.radius):
            return True
        else:
            return False
