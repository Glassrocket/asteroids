import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
   print("Starting asteroids!")
   print(f"Screen width: {SCREEN_WIDTH}")
   print(f"Screen height: {SCREEN_HEIGHT}")

   pygame.init()
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   clock = pygame.time.Clock()
   
   updatable = pygame.sprite.Group()
   drawable = pygame.sprite.Group()
   asteroids = pygame.sprite.Group()
   shots = pygame.sprite.Group()

   Player.containers = (updatable, drawable)
   Asteroid.containers = (asteroids, updatable, drawable)
   AsteroidField.containers = updatable
   Shot.containers = (shots, updatable, drawable)
   
   asteroid_field = AsteroidField()
   player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

   dt = 0

   # Main game loop
   while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            return

      #Updates updatable group
      for obj in updatable:
            obj.update(dt)
      # Collision check
      for asteroid in asteroids:
         if player.collides_with(asteroid):
                  print("Game Over!")
                  sys.exit()
         #Killing shots and Asteroids on collision
         for shot in shots:
            if shot.collides_with(asteroid):
                  shot.kill()
                  asteroid.kill()
      # Fill the screen with the background color
      screen.fill(BACKGROUND_COLOR)
      # Draws drawable group
      for obj in drawable:
            obj.draw(screen)
      # limit the framerate to 60 FPS
      dt = clock.tick(60) / 1000
      # Update the display
      pygame.display.flip()

      

if __name__ == "__main__":
    main()