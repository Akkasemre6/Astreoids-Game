import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidsfield import AsteroidField
from shot import Shot


def main():
    #pygame init
    pygame.init()


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    

    #containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers =(updatable,)
    Shot.containers = (updatable,)


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
        
        for astroid in asteroids:
            if player.check_collision(astroid):
                print("Game Over")
                pygame.quit()


        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
