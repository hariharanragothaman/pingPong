import pygame

BLACK = (0, 0, 0)

"""
Consider a sprite as an object.
An object can have different properties (e.g. width, height, colour, etc.) and methods 
    (e.g. jump(), hide(), moveForward(), etc.).
Like in the industry an object is built from a mould.
In computing the mould is called a Class.
"""

# class Paddle imports the Sprite class - So any real world objects have to import them
class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__() # call the parent class constructor
        # Pass in the color of the paddle, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the paddle (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def moveUp(self, pixels):
        self.rect.y -= pixels
        #Check that you are not going too far (off the screen)
        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self, pixels):
        self.rect.y += pixels
        #Check that you are not going too far (off the screen)
        if self.rect.y > 400:
            self.rect.y = 400
