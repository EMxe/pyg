#Oliver

#imports
import math
import time
import pygame
from pygame.locals import *

# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ray")

# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True
 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# Creates window 
WIDTH = 1000
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ray")

showShadow = True
showHUD = True    

# Defines starting position and direction
positionX = 3.0
positionY = 7.0

directionX = 1.0
directionY = 0.0

planeX = 0.0
planeY = 0.5

# Movement constants   
ROTATIONSPEED = 0.05
MOVESPEED = 0.08

# Trigeometric tuples + variables for index
TGM = (math.cos(ROTATIONSPEED), math.sin(ROTATIONSPEED))
ITGM = (math.cos(-ROTATIONSPEED), math.sin(-ROTATIONSPEED))
COS, SIN = (0,1)

# A map over the world
worldMap =  [
            [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 3, 2, 3, 0, 0, 2],
            [2, 0, 3, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 3, 1, 0, 0, 2, 0, 0, 0, 2, 3, 2, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 2, 0, 0, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 2, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 1, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 3, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 2, 1, 2, 0, 1],
            [1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 2],
            [2, 3, 1, 0, 0, 2, 0, 0, 2, 1, 3, 2, 0, 2, 0, 0, 3, 0, 3, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0, 2, 0, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 3, 0, 1, 2, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 3, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1],
            [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]]

# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: #Pressing the x Key will quit the game
                     carryOn=False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if not worldMap[int(positionX + directionX * MOVESPEED)][int(positionY)]:
            positionX += directionX * MOVESPEED
        if not worldMap[int(positionX)][int(positionY + directionY * MOVESPEED)]:
            positionY += directionY * MOVESPEED
    if keys[pygame.K_s]:
        if not worldMap[int(positionX - directionX * MOVESPEED)][int(positionY)]:
            positionX -= directionX * MOVESPEED
        if not worldMap[int(positionX)][int(positionY - directionY * MOVESPEED)]:
            positionY -= directionY * MOVESPEED
    if keys[pygame.K_a]:
        oldDirectionX = directionX
        directionX = directionX * ITGM[COS] - directionY * ITGM[SIN]
        directionY = oldDirectionX * ITGM[SIN] + directionY * ITGM[COS]
        oldPlaneX = planeX
        planeX = planeX * ITGM[COS] - planeY * ITGM[SIN]
        planeY = oldPlaneX * ITGM[SIN] + planeY * ITGM[COS]
    if keys[pygame.K_d]:
        oldDirectionX = directionX
        directionX = directionX * TGM[COS] - directionY * TGM[SIN]
        directionY = oldDirectionX * TGM[SIN] + directionY * TGM[COS]
        oldPlaneX = planeX
        planeX = planeX * TGM[COS] - planeY * TGM[SIN]
        planeY = oldPlaneX * TGM[SIN] + planeY * TGM[COS] 
    # Draws roof and floor
    screen.fill((25,25,25))
    pygame.draw.rect(screen, (50,50,50), (0, HEIGHT/2, WIDTH, HEIGHT/2))
    
           
    # Starts drawing level from 0 to < WIDTH 
    column = 0        
    while column < WIDTH:
        cameraX = 2.0 * column / WIDTH - 1.0
        rayPositionX = positionX
        rayPositionY = positionY
        rayDirectionX = directionX + planeX * cameraX
        rayDirectionY = directionY + planeY * cameraX + .000000000000001 # avoiding ZDE 

        # In what square is the ray?
        mapX = int(rayPositionX)
        mapY = int(rayPositionY)

        # Delta distance calculation
        # Delta = square ( raydir * raydir) / (raydir * raydir)
        deltaDistanceX = math.sqrt(1.0 + (rayDirectionY * rayDirectionY) / (rayDirectionX * rayDirectionX))
        deltaDistanceY = math.sqrt(1.0 + (rayDirectionX * rayDirectionX) / (rayDirectionY * rayDirectionY))

        # We need sideDistanceX and Y for distance calculation. Checks quadrant
        if (rayDirectionX < 0):
            stepX = -1
            sideDistanceX = (rayPositionX - mapX) * deltaDistanceX

        else:
            stepX = 1
            sideDistanceX = (mapX + 1.0 - rayPositionX) * deltaDistanceX

        if (rayDirectionY < 0):
            stepY = -1
            sideDistanceY = (rayPositionY - mapY) * deltaDistanceY

        else:
            stepY = 1
            sideDistanceY = (mapY + 1.0 - rayPositionY) * deltaDistanceY

        # Finding distance to a wall
        hit = 0
        while  (hit == 0):
            if (sideDistanceX < sideDistanceY):
                sideDistanceX += deltaDistanceX
                mapX += stepX
                side = 0
                
            else:
                sideDistanceY += deltaDistanceY
                mapY += stepY
                side = 1
                
            if (worldMap[mapX][mapY] > 0):
                hit = 1

        # Correction against fish eye effect
        if (side == 0):
            perpWallDistance = abs((mapX - rayPositionX + ( 1.0 - stepX ) / 2.0) / rayDirectionX)
        else:
            perpWallDistance = abs((mapY - rayPositionY + ( 1.0 - stepY ) / 2.0) / rayDirectionY)

        # Calculating HEIGHT of the line to draw
        lineHEIGHT = abs(int(HEIGHT / (perpWallDistance+.0000001)))
        drawStart = -lineHEIGHT / 2.0 + HEIGHT / 2.0

        # if drawStat < 0 it would draw outside the screen
        if (drawStart < 0):
            drawStart = 0

        drawEnd = lineHEIGHT / 2.0 + HEIGHT / 2.0

        if (drawEnd >= HEIGHT):
            drawEnd = HEIGHT - 1

        # Wall colors 0 to 3
        wallcolors = [ [], [150,0,0], [0,150,0], [0,0,150] ]
        color = wallcolors[ worldMap[mapX][mapY] ]                                  

        # If side == 1 then ton the color down. Gives a "showShadow" an the wall.
        # Draws showShadow if showShadow is True
        if showShadow:
            if side == 1:
                for i,v in enumerate(color):
                    color[i] = int(v / 1.2)                    

        # Drawing the graphics                           
        pygame.draw.line(screen, color, (column,drawStart), (column, drawEnd), 2)
        column += 2
    
    
    # Updating display
    pygame.event.pump()
    pygame.display.flip()
    
pygame.quit()