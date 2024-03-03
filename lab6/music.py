import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Music Player")

playlist = ["song1.mp3", "song2.mp3"]
current_song = 0

pygame.mixer.music.load(playlist[current_song])

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_n:
                current_song = (current_song + 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_song])
                pygame.mixer.music.play()
            elif event.key == pygame.K_p:
                current_song = (current_song - 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_song])
                pygame.mixer.music.play()

    screen.fill((255, 255, 255))
    pygame.display.flip()
    clock.tick(60)
