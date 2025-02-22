import circleshape
import pygame
import constants
import random 

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)
    def update(self, dt_s):
        self.position += self.velocity * dt_s
    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(30, 50)
        new_radius = self.radius -constants.ASTEROID_MIN_RADIUS
        
        
        new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid.velocity = 1.2*self.velocity.rotate(random_angle)
        
        new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid.velocity = 1.2*self.velocity.rotate(-random_angle)