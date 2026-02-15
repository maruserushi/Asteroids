import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH

class Shot(CircleShape):
    def __init__(self, x, y, radius, live, damage):
        super().__init__(x, y, radius, live, damage)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)
