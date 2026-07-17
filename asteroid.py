import pygame
import random
from circleshape import CircleShape
from logger import log_event
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self,screen: pygame.Surface):
        pygame.draw.circle(screen, "white",self.position , self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        
        random_angle = random.uniform(20,50)
        
        num_vector_1 = self.velocity.rotate(random_angle)
        num_vector_2 = self.velocity.rotate(-random_angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        child_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        child_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

        child_asteroid_1.velocity = num_vector_1 * 1.2
        child_asteroid_2.velocity = num_vector_2 * 1.2

    