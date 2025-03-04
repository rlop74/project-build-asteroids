# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init() # initialize pygame
    clock = pygame.time.Clock() # create a clock for framerate control
    updatable = pygame.sprite.Group() # group for updating objects
    drawable = pygame.sprite.Group() # group for drawable objects
    asteroids = pygame.sprite.Group() # group for asteroid objects
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    Player.containers = (updatable, drawable) # Assign sprite groups to the Player class
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # instantiate Player object / creating Player instance

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # create a game screen or window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # player rotation
        updatable.update(dt)
        
        screen.fill("black") # black background
        
        # draw triangle ship
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip() # update the display
        
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
