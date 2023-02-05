import pygame, pymunk

class Ball():
    def __init__(self, surface, space, pos, vel, mass, radius, color, elasticity = 0):

        self.surface = surface
        self.color = color

        self.doesCollide = True

        self.startPos = pos
        self.startVel = vel

        self.mass = mass
        self.inertia = 5
        self.radius = radius

        self.body_type = pymunk.Body.DYNAMIC
        self.body = pymunk.Body(self.mass, self.inertia, self.body_type)
        self.body.position = self.startPos
        self.body.velocity = self.startVel
        self.shape = pymunk.Circle(self.body, self.radius)
        self.shape.elasticity = elasticity
        space.add(self.body, self.shape)

    def draw(self):
        '''Draws the circle its surface.'''
        pos = (int(self.body.position.x), int(self.body.position.y))
        pygame.draw.circle(self.surface, self.color, pos, self.radius)