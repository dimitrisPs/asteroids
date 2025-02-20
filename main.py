import pygame
from constants import *

FPS=60

def main():
    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    pygame.init()
    pgc = pygame.time.Clock()
    dt_s = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while(True):
        
        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        
        screen.fill((0, 0, 0))
        pygame.display.flip()
        
        # wait for 1 frame and compute delta time
        dt_s = pgc.tick(FPS)/1000


if __name__ == '__main__':
    main()  