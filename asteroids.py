from circleshape import CircleShape
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y=y
        self.radius=radius
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.x,self.y),self.radius, 2)
    def update(self, dt):
        self.x, self.y += (self.velocity*dt)
