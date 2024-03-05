import pygame
import sys
from datetime import datetime

pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mickey Clock")

mickey_image = pygame.image.load("mickeyclock.jpeg")
mickey_rect = mickey_image.get_rect(center=(screen_width//2, screen_height//2))

def rotate_hand(image, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_image.get_rect(center=mickey_rect.center)
    return rotated_image, rotated_rect

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    current_time = datetime.now()
    hour = current_time.hour
    minute = current_time.minute
    second = current_time.second

    minute_hand_image, minute_hand_rect = rotate_hand(mickey_image, -minute * 6)
    second_hand_image, second_hand_rect = rotate_hand(mickey_image, -second * 6)

    screen.fill((255, 255, 255))
    screen.blit(mickey_image, mickey_rect)
    screen.blit(minute_hand_image, minute_hand_rect)
    screen.blit(second_hand_image, second_hand_rect)

    pygame.display.flip()
    clock.tick(60)
