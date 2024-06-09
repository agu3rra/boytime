import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Boy Time")

# Load the sprite image
sprite_image = pygame.image.load("boytime/assets/sprites/boytime/stand.png")

# Get the sprite's rectangle
sprite_rect = sprite_image.get_rect()

# Set the initial position of the sprite
sprite_rect.x = 100
sprite_rect.y = 100

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the sprite
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sprite_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        sprite_rect.x += 5
    if keys[pygame.K_UP]:
        sprite_rect.y -= 5
    if keys[pygame.K_DOWN]:
        sprite_rect.y += 5

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the sprite
    screen.blit(sprite_image, sprite_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()