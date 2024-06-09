import pygame
from pygame import Surface

def main():
    # Initialize Pygame
    pygame.init()

    # Set up the game window
    screen: Surface = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Boy Time")

    # Load the sprite image
    sprite_image: Surface = pygame.image.load(
        "boytime/assets/sprites/boytime/stand.png")

    # Scale the sprite image
    original_width, original_height = sprite_image.get_size()
    scaled_width = int(original_width * 0.25)
    scaled_height = int(original_height * 0.25)
    sprite_image = pygame.transform.scale(
        sprite_image, (scaled_width, scaled_height))

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

if __name__ == "__main__":
    main()