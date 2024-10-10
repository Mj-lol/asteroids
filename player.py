from circleshape import *
from constants import *
import constants
from shot import Shot
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation=0
        self.timer = 0
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen):
        pygame.draw.polygon(screen, "black", self.triangle(), 2)
    def rotate(self,dt):
        self.rotation+= (PLAYER_TURN_SPEED*dt)
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer-=dt
        if keys[pygame.K_a]:
            self.rotate(-1*dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(-1*dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        if keys[pygame.K_r]:
            constants.COOLDOWN = 0
        if keys[pygame.K_p]:
            constants.COOLDOWN += 0.1
            return
        if keys[pygame.K_l]:
            constants.COOLDOWN -= 0.1
            return
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    def shoot(self):
        if self.timer > 0:
            return
        self.timer = constants.COOLDOWN
        s = Shot(self.position.x, self.position.y)
        s.velocity = pygame.Vector2(0,1).rotate(self.rotation)*PLAYER_SHOOT_SPEED
