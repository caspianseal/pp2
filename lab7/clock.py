import sys
import pygame
from pygame.locals import *
import time
import math

# Function to load an image
def load_image(image_path):
    return pygame.image.load(image_path).convert_alpha()

# Function to rotate an image
def rotate_image(image, angle):
    return pygame.transform.rotate(image, angle)

# Function to get the angle for rotation based on time
def get_angle():
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min

    # Calculate angles for Mickey's hands
    seconds_angle = -6 * seconds
    minutes_angle = -6 * minutes - seconds * 0.1  # Taking seconds into account for more precision in minutes hand

    return seconds_angle, minutes_angle

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 1400, 1050
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Mickey Mouse Clock')

text2 = font_small.render(f'minutes: {minutes}', antialias = true, BLACK)
text1 = font_small.render(f'seconds: {seconds}' antialias = true, BLACK)
# Load images
background_image = load_image('mainclock.png')
right_hand_image = load_image('rightarm.png')
left_hand_image = load_image('leftarm.png')

# Get initial positions for Mickey's hands
right_hand_position = (screen_width // 2, screen_height // 2)
left_hand_position = (screen_width // 2, screen_height // 2)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background_image, (0, 0))

    # Get rotation angles
    seconds_angle, minutes_angle = get_angle()

    # Rotate and blit Mickey's hands
    rotated_right_hand = rotate_image(right_hand_image, seconds_angle)
    rotated_left_hand = rotate_image(left_hand_image, minutes_angle)

    # Calculate positions for Mickey's hands
    right_hand_rect = rotated_right_hand.get_rect(center=right_hand_position)
    left_hand_rect = rotated_left_hand.get_rect(center=left_hand_position)

    # Blit Mickey's hands
    screen.blit(rotated_right_hand, right_hand_rect)
    screen.blit(rotated_left_hand, left_hand_rect)

    pygame.display.flip()
    pygame.time.delay(1000)  # Update every second
