import pygame, pymunk

class Obstacle():
    def __init__(self, surface, space, vertices, center, radius, color, elasticity, friction, doesCollide):

        self.surface = surface
        self.vertices = vertices
        self.center = center
        self.radius = radius

        self.doesCollide = doesCollide

        self.color = color

        if doesCollide:
            self.body_type = pymunk.Body.STATIC
            self.body = pymunk.Body(body_type = self.body_type)
            if self.vertices != [] and self.radius == 0:
                self.shape = pymunk.Poly(self.body, self.vertices)
            else:
                self.shape = pymunk.Circle(self.body, self.radius)
                self.body.position = self.center
            self.shape.elasticity = elasticity
            self.shape.friction = friction
            space.add(self.body, self.shape)
    
    def draw(self):
        '''Draws the obstacle on its surface.'''

class Square(Obstacle):
    def __init__(self, surface, space, pos, size, color, elasticity = 0, friction = 0, doesCollide = True):
        vertices = [pos, (pos[0] + size[0], pos[1]), (pos[0], pos[1] + size[1]), (pos[0] + size[0], pos[1] + size[1])]
        super().__init__(surface, space, vertices, 0, 0, color, elasticity, friction, doesCollide)
        self.size = size
        self.rect = pygame.Rect(pos[0], pos[1], self.size[0], self.size[1])

    def draw(self):
        super().draw()
        pygame.draw.rect(self.surface,self.color,self.rect)

class Triangle(Obstacle):
    def __init__(self, surface, space, vertices, color, elasticity = 0, friction = 0, doesCollide = True):
        super().__init__(surface, space, vertices, 0, 0, color, elasticity, friction, doesCollide)

    def draw(self):
        super().draw()
        pygame.draw.polygon(self.surface,self.color,self.vertices)

class Circle(Obstacle):
    def __init__(self, surface, space, center, radius, color, elasticity, friction = 0, doesCollide = True):
        super().__init__(surface, space, [], center, radius, color, elasticity, friction, doesCollide)
    
    def draw(self):
        super().draw()
        pygame.draw.circle(self.surface, self.color, self.center, self.radius)

class String():
    def __init__(self, surface, space, color, body1, attatchment, identifier='body'):

        self.surface = surface
        self.color = color

        self.doesCollide = False

        self.body1 = body1
        if identifier == 'body':
            self.body2 = attatchment
        elif identifier == 'position':
            self.body2 = pymunk.Body(body_type=pymunk.Body.STATIC)
            self.body2.position = attatchment
        joint = pymunk.PinJoint(self.body1, self.body2)
        space.add(joint)

    def draw(self):
        '''Draws the circle its surface.'''
        pos = ((self.body1.position), (self.body2.position))
        pygame.draw.line(self.surface, self.color, pos[0], pos[1])