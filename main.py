import pygame
from constants import *
import player as plyr
import asteroid as astr
from asteroidfield import AsteroidField
import shot

def main():
    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    pygame.init()
    pgc = pygame.time.Clock()
    dt_s = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updateables_g = pygame.sprite.Group()
    drawables_g = pygame.sprite.Group()
    asteroirds_g = pygame.sprite.Group()
    shots_g = pygame.sprite.Group()
    
    astr.Asteroid.containers = updateables_g, drawables_g, asteroirds_g
    AsteroidField.containers = updateables_g
    plyr.Player.containers = updateables_g, drawables_g
    shot.Shot.containers = updateables_g, drawables_g, shots_g
    
    
    player = plyr.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    
    while(True):
        
        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
            
        
        updateables_g.update(dt_s)
        
        for asteroid in asteroirds_g:
            if asteroid.colides(player):
                print('Game Over!')
                return
        for asteroid in asteroirds_g:
            for bullet in shots_g:
                if bullet.colides(asteroid):
                    asteroid.split()
                    bullet.kill()
        
        
        for drawable in drawables_g:
            drawable.draw(screen)
            
        
        
        pygame.display.flip()
        
        # wait for 1 frame and compute delta time
        dt_s = pgc.tick(FPS)/1000


if __name__ == '__main__':
    main()  