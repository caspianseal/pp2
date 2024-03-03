import pygame
import sys

pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Ball")

ball_radius = 25
ball_color = (255, 0, 0)
ball_position = [screen_width // 2, screen_height // 2]

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_position[1] -= 20
            elif event.key == pygame.K_DOWN:
                ball_position[1] += 20
            elif event.key == pygame.K_LEFT:
                ball_position[0] -= 20
            elif event.key == pygame.K_RIGHT:
                ball_position[0] += 20

    ball_position[0] = max(ball_radius, min(screen_width - ball_radius, ball_position[0]))
    ball_position[1] = max(ball_radius, min(screen_height - ball_radius, ball_position[1]))

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, ball_color, ball_position, ball_radius)
    pygame.display.flip()
    clock.tick(60)
