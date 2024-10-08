from circleshape import *
from constants import *
import random
import pygame

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)

  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    else:
      random_angle = random.uniform(20, 50)
      pos = pygame.math.Vector2.rotate(self.velocity, random_angle)
      neg = pygame.math.Vector2.rotate(self.velocity, -random_angle)
      new_radius = self.radius - ASTEROID_MIN_RADIUS
      asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
      asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
      asteroid_one.velocity = pos * 1.2
      asteroid_two.velocity = neg * 1.2


