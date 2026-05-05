import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        ast1_vec = self.velocity.rotate(angle)
        ast2_vec = self.velocity.rotate(-angle)
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        new_ast1 = Asteroid(self.position[0], self.position[1], new_rad)
        new_ast2 = Asteroid(self.position[0], self.position[1], new_rad)
        new_ast1.velocity = ast1_vec * 1.2
        new_ast2.velocity = ast2_vec * 1.2
