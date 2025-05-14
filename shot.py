import pygame
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)
        self.radius = radius
        self.shot_radius = 5
        
