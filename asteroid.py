from circleshape import CircleShape
import pygame
from logger import log_event
from constants import *
from random import uniform

x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt) -> None:
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = uniform(20, 50)

            log_event("asteroid_split")
            vector1 = self.velocity.rotate(angle)
            vector2 = self.velocity.rotate(-angle)
            radd = self.radius - ASTEROID_MIN_RADIUS

            asteroid1 = Asteroid(self.position.x, self.position.y, radd)
            asteroid2 = Asteroid(self.position.x, self.position.y, radd)

            asteroid1.velocity, asteroid2.velocity = vector1 * 1.2, vector2 * 1.2