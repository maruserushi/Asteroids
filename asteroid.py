import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_BASE_DAMAGE, ASTEROID_MIN_LIVE
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, live, damage):
        super().__init__(x, y, radius, live, damage)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split_spawn(self, radius, position, velocity, live, damage):
        asteroid = Asteroid(position.x, position.y, radius, live, damage)
        asteroid.velocity = velocity

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            self.split_spawn((self.radius - ASTEROID_MIN_RADIUS), self.position, (self.velocity.rotate(angle) * 1.2), (self.live - ASTEROID_MIN_LIVE), (self.damage - ASTEROID_BASE_DAMAGE))
            self.split_spawn((self.radius - ASTEROID_MIN_RADIUS), self.position, (self.velocity.rotate(-abs(angle)) * 1.2), (self.live - ASTEROID_MIN_LIVE), (self.damage - ASTEROID_BASE_DAMAGE))
