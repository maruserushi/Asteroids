import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    clock = pygame.time.Clock()
    dt = 0
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    font = pygame.font.SysFont("Arial", 16)
    asteroidsfield = AsteroidField()
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for updatables in updatable:
            updatables.update(dt)
            statlive = font.render(f"Health: {player.live}", True, (255,255,255))
            statarmor = font.render(f"Armor: {player.armor}", True, (255,255,255))
            statdamage = font.render(f"Damage: {player.damage}", True, (255,255,255))
            screen.blit(statlive,(1200 - statlive.get_width() // 2, 675 - statlive.get_height() // 2))
            screen.blit(statarmor,(1200 - statarmor.get_width() // 2, 690 - statarmor.get_height() // 2))
            screen.blit(statdamage,(1200 - statdamage.get_width() // 2, 705 - statdamage.get_height() // 2))
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                if player.take_damage(asteroid):
                    log_event("player_hit")
                    print("Game over!")
                    sys.exit()
            for single_shot in shots:
                if asteroid.collides_with(single_shot):
                    log_event("asteroid_shot")
                    if asteroid.take_damage(single_shot):
                        asteroid.split()
                    single_shot.kill()
        for drawables in drawable:
            drawables.draw(screen)
        pygame.display.flip()
        dt = (clock.tick(60) / 1000)



if __name__ == "__main__":
    main()
