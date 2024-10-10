from circleshape import CircleShape
import pygame
import random
from constants import ASTEROID_KINDS, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position,self.radius, 2)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        one = self.velocity.rotate(angle)
        two = self.velocity.rotate(-angle)
        newrad = self.radius-ASTEROID_MIN_RADIUS
        on = Asteroid(self.position.x, self.position.y, newrad)
        tw = Asteroid(self.position.x, self.position.y, newrad)
        on.velocity = one*1.2
        tw.velocity = two*1.2
