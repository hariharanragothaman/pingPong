import pygame

# Initializing the game engine
pygame.init()

# Defining some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Opening a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PONG")

# Flag to run Game loop until user exits game window!
carry_on = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

while carry_on:
    # -- Main event loop
    for event in pygame.event.get(): # user did something
        if event.type == pygame.QUIT: # If user clicked close
            carry_on = False

    # -------- Game logic should go here
    # --- Drawing code should go here
    # First, clear the screen to black.
    screen.fill(BLACK)
    #Draw the net
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
