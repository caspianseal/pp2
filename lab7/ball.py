import pygame
import sys

pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Ball")

# Load the PNG image of the ball
ball_image = pygame.image.load("coin.png")
# Resize the ball image to match the desired radius
ball_image = pygame.transform.scale(ball_image, (50, 50))  # Adjust the size as needed

ball_rect = ball_image.get_rect()
ball_rect.center = (screen_width // 2, screen_height // 2)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_rect.y -= 20
            elif event.key == pygame.K_DOWN:
                ball_rect.y += 20
            elif event.key == pygame.K_LEFT:
                ball_rect.x -= 20
            elif event.key == pygame.K_RIGHT:
                ball_rect.x += 20

    # Keep the ball within the screen boundaries
    ball_rect.x = max(ball_rect.width // 2, min(screen_width - ball_rect.width // 2, ball_rect.x))
    ball_rect.y = max(ball_rect.height // 2, min(screen_height - ball_rect.height // 2, ball_rect.y))

    screen.fill((255, 255, 255))
    screen.blit(ball_image, ball_rect)
    pygame.display.flip()
    clock.tick(60)
