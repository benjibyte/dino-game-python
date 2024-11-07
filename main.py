import pygame
import sys

title = "Dino Game"
scaler = 2
width = 960
height = 540
tile_size = 16


def sky(surface, scale=2):
    sky_sprite = "sky.png"
    background = pygame.image.load(sky_sprite)
    background_w, background_h = background.get_size()
    scaled_background = pygame.transform.scale(background, (background_w * scale, background_h * scale))
    surface.blit(scaled_background)

    return scaled_background


def ground(surface, scale=2):
    ground_sprite = "images/ground.png"
    ground_y = height - ((tile_size * scale) * 5)
    ground_pos = (0, ground_y) 
    # apply the original tile size (tile_size) then scale it up, and then 
    # count 5 tiles and take that away from the game height

    ground = pygame.image.load(ground_sprite)
    ground_w, ground_h = ground.get_size()
    scaled_ground = pygame.transform.scale(ground, (ground_w * scale, ground_h * scale))
   

    return (scaled_ground, ground_pos)

# Dino
IS_JUMPING = False
Y_GRAVITY = 1
JUMP_HEIGHT = 12
Y_VELOCITY = JUMP_HEIGHT

JUMP_COUNT = 0
DINO_Y = height - ((tile_size  * scaler) * 7) 
DINO_X = (tile_size * scaler) * 3
def dino(surface, scale=2):
    global Y_GRAVITY
    global JUMP_HEIGHT
    global Y_VELOCITY
    global IS_JUMPING
    global DINO_X
    global DINO_Y

    if IS_JUMPING:
        DINO_Y -= Y_VELOCITY
        Y_VELOCITY -= Y_GRAVITY
        if Y_VELOCITY < (-1 * JUMP_HEIGHT):
            IS_JUMPING = False
            dino_sprite = "images/dino/dino-1x.png"
            Y_VELOCITY = JUMP_HEIGHT
        dino_sprite = "images/dino/dino-jump-1x.png"
    else:
        dino_sprite = "images/dino/dino-1x.png"
    


    # Render Dino:
    dinosaur = pygame.image.load(dino_sprite)
    dino_w, dino_h = dinosaur.get_size()
    scaled_dino = pygame.transform.scale(dinosaur, (dino_w * scale, dino_h * scale))
    surface.blit(scaled_dino, (DINO_X,DINO_Y))

LAST_POSITION = 0
SPEED = 20
def move_ground(old_x=0):
    new_x = old_x - SPEED
    y = old_y # Y Doesn't change, but i have to include it since this function returns to a tuple.
    return 

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(title)

while True:
    #load sky, ground, check events, and then dino
    sky(screen)
    floor = ground(screen)
    floor_surface = floor[0]
    floor_pos = floor[1]
    floor_x, floor_y = floor_pos if JUMP_COUNT == LAST_POSITION else move_ground(LAST_POSITION)
    screen.blit(floor_surface, floor_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    

    # Get keys pressed
    keys_pressed = pygame.key.get_just_pressed()
    # Dino
    
    if keys_pressed[pygame.K_SPACE] == True:
        IS_JUMPING = True

    dino(screen, 2)
        
    

    
    
    # update the screen display
    pygame.display.flip()