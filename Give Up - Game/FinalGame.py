#----------------------------------------------#
# Final Game                                   #
# By: Ethan Zohar                              #
# June 19, 2017                                #
# Holds the main code for my final game        #
#----------------------------------------------#

from FinalGameClasses import * # Imports all the classes from the classes file
import pygame       #
import random as r  # Imports modules used
import math         #
pygame.init() # Initializes pygame

#-----------------------------------------------#
HEIGHT = 750                                    #
WIDTH  = 1200                                   #
GRIDSIZE = 30                                   # Variables for the screen
GROUND = 19*GRIDSIZE                            #
screen=pygame.display.set_mode((WIDTH,HEIGHT))  #
#-----------------------------------------------#

#-----------------------#
inPlay = True           #
gameScreen = 0          #
WHITE = (255,255,255)   # Variables for the main structure of the game
BLACK = (0,0,0)         #
level = 1               #
rightTrigger = False    #
framecount = 0          #
#-----------------------#

weightBlocks = [] # For the blocks that the fallen weights take up

#-----------------------#
jumpTrigger = False     #
jumpCount = 0           # Variables for
stopYTrigger = False    # the player
playerNum = 1           #
#-----------------------#

#---------------------------#
gravity = 1                 #
slowDown = 2                #
jumpSpeed = 10              #
starSpeed = 10              #
shootSpeed = 20             # Variables for obstacles
bombSpeed = 10              #
fallSpeed = 15              #
laserSpeed = 60             #
mach = 10                   #
laserShootTrigger = False   #
#---------------------------#

font = pygame.font.SysFont("Ariel Black",50)    # Initializes the small font
font2 = pygame.font.SysFont("Ariel Black",120)  # Initializes the large font 

#---------------------------------------------------------------#
oof = pygame.mixer.Sound('oof2.wav')                            #
oof.set_volume(1000)                                            #
starshooterSound = pygame.mixer.Sound('starshooterSound.wav')   #
starshooterSound.set_volume(0.9)                                #
weightSound = pygame.mixer.Sound('weightSound.wav')             #
weightSound.set_volume(0.2)                                     # Initializes all of
bombSound = pygame.mixer.Sound('bombSound.wav')                 # the sounds
bombSound.set_volume(0.9)                                       #
springSound = pygame.mixer.Sound('springSound.wav')             #
springSound.set_volume(0.3)                                     #
laserSound = pygame.mixer.Sound('laserSound2.wav')              #
laserSound.set_volume(0.3)                                      #
#---------------------------------------------------------------#

#---------------------------------------------------------------------------------------#
playerImg = []                                                                          #
for i in range(3):                                                                      #
    imgList = []                                                                        #
    for j in range(11):                                                                 #
        imgList.append(pygame.image.load('p' + str(i+1) + '_walk' + str(j+1) + '.png')) #
        imgList[j] = imgList[j].convert_alpha()                                         #
        imgList[j] = pygame.transform.scale(imgList[j], (35, 50))                       # Loads all of the images used for
    playerImg.append(imgList)                                                           # for the player walking animation
    imgList = []                                                                        #
    for j in range(11):                                                                 #
        imgList.append(pygame.image.load('p' + str(i+1) + '_walk' + str(j+1) + '.png')) #
        imgList[j] = imgList[j].convert_alpha()                                         #
        imgList[j] = pygame.transform.scale(imgList[j], (35, 50))                       #
        imgList[j] = pygame.transform.flip(imgList[j], True, False)                     #
    playerImg.append(imgList)                                                           #
#---------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------#
playerImglarge = []                                                                     #
for i in range(3):                                                                      #
    imgList = []                                                                        #
    for j in range(11):                                                                 # Loads all of the images used for
        imgList.append(pygame.image.load('p' + str(i+1) + '_walk' + str(j+1) + '.png')) # the end screen walking animation
        imgList[j] = imgList[j].convert_alpha()                                         #
        imgList[j] = pygame.transform.scale(imgList[j], (350, 500))                     #
    playerImglarge.append(imgList)                                                      #
#---------------------------------------------------------------------------------------#
    
#---------------------------------------------------------------------------#
playerStand = []                                                            #
for i in range(3):                                                          #
    playerStand.append(pygame.image.load('p' + str(i+1) + '_stand.png'))    #
    playerStand[i] = playerStand[i].convert_alpha()                         #
    playerStand[i] = pygame.transform.scale(playerStand[i], (35, 50))       #
                                                                            # Loads all of the images used for
playerStandL = []                                                           # the player standing
for i in range(3):                                                          #
    playerStandL.append(pygame.image.load('p' + str(i+1) + '_stand.png'))   #
    playerStandL[i] = playerStandL[i].convert_alpha()                       #
    playerStandL[i] = pygame.transform.scale(playerStandL[i], (35, 50))     #
    playerStandL[i] = pygame.transform.flip(playerStandL[i], True, False)   #
#---------------------------------------------------------------------------#

#-----------------------------------------------------------------------#
jumpImg = []                                                            #
for i in range(3):                                                      #
    jumpImg.append(pygame.image.load('p' + str(i+1) + '_jump.png'))     #
    jumpImg[i] = jumpImg[i].convert_alpha()                             #
    jumpImg[i] = pygame.transform.scale(jumpImg[i], (35, 50))           #
                                                                        # Loads all of the images used for
jumpImgL = []                                                           # the player jumping
for i in range(3):                                                      #
    jumpImgL.append(pygame.image.load('p' + str(i+1) + '_jump.png'))    #
    jumpImgL[i] = jumpImgL[i].convert_alpha()                           #
    jumpImgL[i] = pygame.transform.scale(jumpImgL[i], (35, 50))         #
    jumpImgL[i] = pygame.transform.flip(jumpImgL[i], True, False)       #
#-----------------------------------------------------------------------#

#---------------------------------------------------------------------------------------#
weightImg = [] #Weight Pictures                                                         #
for i in range(2):                                                                      #
    weightImg.append(pygame.image.load('weight' + str(i) + '.png'))                     #
    weightImg[i] = weightImg[i].convert_alpha()                                         #
    weightImg[i] = pygame.transform.scale(weightImg[i], (GRIDSIZE, GRIDSIZE))           #
                                                                                        #
laserImg = [] #Laser Pictures                                                           #
for i in range(4):                                                                      #
    laserImg.append(pygame.image.load('laser' + str(i) + '.png'))                       #
    laserImg[i] = laserImg[i].convert_alpha()                                           #
    laserImg[i] = pygame.transform.scale(laserImg[i], (GRIDSIZE, GRIDSIZE))             #
                                                                                        #
laserBeamImg = [] #laserbeam Pictures                                                   #
for i in range(2):                                                                      #
    laserBeamImg.append(pygame.image.load('laserBeam' + str(i) + '.png'))               #
    laserBeamImg[i] = laserBeamImg[i].convert_alpha()                                   #
    laserBeamImg[i] = pygame.transform.scale(laserBeamImg[i], (GRIDSIZE, GRIDSIZE))     #
                                                                                        #
spikeImg = [] #Spike Pictures                                                           #
for i in range(4):                                                                      #
    spikeImg.append(pygame.image.load('spike' + str(i) + '.png'))                       #
    spikeImg[i] = spikeImg[i].convert_alpha()                                           #
    spikeImg[i] = pygame.transform.scale(spikeImg[i], (GRIDSIZE, GRIDSIZE))             #
                                                                                        #
bombImg = [] #Bomb Pictures                                                             #
for i in range(3):                                                                      # Loads all of the images for
    bombImg.append(pygame.image.load('bomb' + str(i) + '.png'))                         # all of the obstacles animations
    bombImg[i] = bombImg[i].convert_alpha()                                             # and the numbers for the
    bombImg[i] = pygame.transform.scale(bombImg[i], (GRIDSIZE, GRIDSIZE))               # lives counter
                                                                                        #
explosionImg = [] #Explosion Pictures                                                   #
for i in range(12):                                                                     #
    explosionImg.append(pygame.image.load('explosion' + str(i) + '.png'))               #
    explosionImg[i] = explosionImg[i].convert_alpha()                                   #
    explosionImg[i] = pygame.transform.scale(explosionImg[i], (GRIDSIZE*3, GRIDSIZE*3)) #
                                                                                        #
springImg = [] #Spring Pictures                                                         #
for i in range(2):                                                                      #
    springImg.append(pygame.image.load('spring' + str(i) + '.png'))                     #
    springImg[i] = springImg[i].convert_alpha()                                         #
    springImg[i] = pygame.transform.scale(springImg[i], (GRIDSIZE, GRIDSIZE))           #
                                                                                        #
starShooterImg = [] #StarShooter Pictures                                               #
for i in range(4):                                                                      #
    starShooterImg.append(pygame.image.load('starShooter' + str(i) + '.png'))           #
    starShooterImg[i] = starShooterImg[i].convert_alpha()                               #
    starShooterImg[i] = pygame.transform.scale(starShooterImg[i], (GRIDSIZE, GRIDSIZE)) #
                                                                                        #
numbersImg = [] #Numbers Pictures                                                       #
for i in range(10):                                                                     #
    numbersImg.append(pygame.image.load('num' + str(i) + '.png'))                       #
    numbersImg[i] = numbersImg[i].convert_alpha()                                       #
    numbersImg[i] = pygame.transform.scale(numbersImg[i], (64, 80))                     #
numX = 5.5*GRIDSIZE                                                                     #
numY = 21*GRIDSIZE                                                                      #
#---------------------------------------------------------------------------------------#

#-----------------------------------------------------------------------------------#
heartImg = pygame.image.load('hud_heartFull.png')                                   #
heartImg = heartImg.convert_alpha()                                                 #
heartImg = pygame.transform.scale(heartImg, (GRIDSIZE*3, GRIDSIZE*3))               #
heartX = 0.5*GRIDSIZE                                                               #
heartY = 21*GRIDSIZE                                                                #
                                                                                    #
hudXImg = pygame.image.load('hud_x.png')                                            #
hudXImg = hudXImg.convert_alpha()                                                   #
hudXImg = pygame.transform.scale(hudXImg, (GRIDSIZE*2, GRIDSIZE*2))                 #
hudX = 3.5*GRIDSIZE                                                                 #
hudY = 22*GRIDSIZE-GRIDSIZE//2                                                      #
                                                                                    #
giveupImg = pygame.image.load('giveup2.png')                                        #
giveupImg = giveupImg.convert_alpha()                                               #
giveupImg = pygame.transform.scale(giveupImg, (GRIDSIZE*20, GRIDSIZE*3))            #
giveupX = GRIDSIZE*19.5                                                             #
giveupY = GRIDSIZE*21                                                               #
giveupW = GRIDSIZE*20                                                               #
giveupH = GRIDSIZE*3                                                                #
                                                                                    #
blockImg = pygame.image.load('boxAlt.png')                                          #
blockImg = blockImg.convert_alpha()                                                 #
blockImg = pygame.transform.scale(blockImg, (GRIDSIZE, GRIDSIZE))                   #
                                                                                    #
grassMidImg = pygame.image.load('grassMid.png')                                     #
grassMidImg = grassMidImg.convert_alpha()                                           #
grassMidImg = pygame.transform.scale(grassMidImg, (GRIDSIZE, GRIDSIZE))             #
                                                                                    #
grassCenterImg = pygame.image.load('grassCenter.png')                               #
grassCenterImg = grassCenterImg.convert_alpha()                                     #
grassCenterImg = pygame.transform.scale(grassCenterImg, (GRIDSIZE, GRIDSIZE))       #
                                                                                    #
starImg = pygame.image.load('star.png')                                             #
starImg = starImg.convert_alpha()                                                   #
starImg = pygame.transform.scale(starImg, (GRIDSIZE, GRIDSIZE))                     #
                                                                                    #
bombShooterImg = pygame.image.load('bombShooter.png')                               #
bombShooterImg = bombShooterImg.convert_alpha()                                     #
bombShooterImg = pygame.transform.scale(bombShooterImg, (GRIDSIZE, GRIDSIZE))       #
                                                                                    #
wallImg = pygame.image.load('castleCenter.png')                                     #
wallImg.convert_alpha()                                                             #
wallImg = pygame.transform.scale(wallImg, (GRIDSIZE, GRIDSIZE))                     #
                                                                                    #
backImg = pygame.image.load('bg.png')                                               #
backImg.convert_alpha()                                                             #
backImg = pygame.transform.scale(backImg, (GRIDSIZE, GRIDSIZE))                     #
                                                                                    #
doorImgTop = pygame.image.load('door_openTop.png')                                  # Loads all of the extra individual
doorImgTop.convert_alpha()                                                          # images that are used
doorImgTop = pygame.transform.scale(doorImgTop, (GRIDSIZE*2, GRIDSIZE*2))           #
                                                                                    #
doorImgBottom = pygame.image.load('door_openMid.png')                               #
doorImgBottom.convert_alpha()                                                       #   
doorImgBottom = pygame.transform.scale(doorImgBottom, (GRIDSIZE*2, GRIDSIZE*2))     #
                                                                                    #
door2ImgTop = pygame.image.load('door_closedTop.png')                               #
door2ImgTop.convert_alpha()                                                         #
door2ImgTop = pygame.transform.scale(door2ImgTop, (GRIDSIZE*2, GRIDSIZE*2))         #
                                                                                    #
door2ImgBottom = pygame.image.load('door_closedMid.png')                            #
door2ImgBottom.convert_alpha()                                                      #
door2ImgBottom = pygame.transform.scale(door2ImgBottom, (GRIDSIZE*2, GRIDSIZE*2))   #
                                                                                    #
exitSign = pygame.image.load('signExit.png')                                        #
exitSign.convert_alpha()                                                            #
exitSign = pygame.transform.scale(exitSign, (GRIDSIZE*2, GRIDSIZE*2))               #
exitX = GRIDSIZE * 35                                                               #
exitY = GRIDSIZE * 17                                                               #
                                                                                    #
largeP1 = pygame.image.load('p1_front.png')                                         #
largeP1.convert_alpha()                                                             #
largeP1X = 267                                                                      #
largeP1Y = 250                                                                      #
                                                                                    #
p1Lock = pygame.image.load('lock_green.png')                                        #
p1Lock.convert_alpha()                                                              #
p1Lock = pygame.transform.scale(p1Lock, (66,66))                                    #
p1LockY = 380                                                                       #
                                                                                    #
largeP2 = pygame.image.load('p2_front.png')                                         #
largeP2.convert_alpha()                                                             #
largeP2X = 567                                                                      #
largeP2Y = 250                                                                      #
                                                                                    #
p2Lock = pygame.image.load('lock_blue.png')                                         #
p2Lock.convert_alpha()                                                              #
p2Lock = pygame.transform.scale(p2Lock, (66,66))                                    #
p2LockY = 380                                                                       #
                                                                                    #
largeP3 = pygame.image.load('p3_front.png')                                         #
largeP3.convert_alpha()                                                             #
largeP3X = 867                                                                      #
largeP3Y = 250                                                                      #
                                                                                    #
p3Lock = pygame.image.load('lock_red.png')                                          #
p3Lock.convert_alpha()                                                              #
p3Lock = pygame.transform.scale(p3Lock, (66,66))                                    #
p3LockY = 380                                                                       #
                                                                                    #
bridge = pygame.image.load('bridge.png')                                            #
bridge.convert_alpha()                                                              #
bridge = pygame.transform.scale(bridge,(66,66))                                     #
bridgeY = 294                                                                       #
                                                                                    #
key = pygame.image.load('hud_keyYellow.png')                                        #
key.convert_alpha()                                                                 #
keyY = 460                                                                          #
#-----------------------------------------------------------------------------------#

Walls = [Wall(0,0,GRIDSIZE, 1,20), Wall(39,0,GRIDSIZE, 1,20), Wall(1,0,GRIDSIZE, 38,1), Wall(1,19,GRIDSIZE, 38,1)] # Creates all the walls that surround the screen

#-------------------------------------------#
available = []                              #
for i in range(2,38): # Top                 #
    available.append((i, 1, 2))             #
for i in range(3, 37): # Bottom             # 
    available.append((i, 18, 0))            #
for i in range(1, 16):                      #
    available.append((1, i, 1)) # Left      #
    available.append((38, i, 3)) # Right    # Initializes lists that hold all
                                            # of the available blocks for the 
availableBlocks = []                        # game to use as positions to spawn in
for i in range(3, 37):                      #
    for j in range(3, 16):                  #
        availableBlocks.append((i,j))       #
for i in range(3, 37):                      #
    for j in range(16,19):                  #
        availableBlocks.append((i,j))       #
#-------------------------------------------#

#---------------------------#
obstacles = []              #
for i in range(7):          # Creates an empty list for the obstacles to be appended to
    obstacles.append([])    #
#---------------------------#

#-----------#
doorX = 37  #
doorY = 15  # Initializes all the x and y
doorX2 = 1  # positions for the door
doorY2 = 15 #
#-----------#

#---------------------------------------------------#
occupiedBlocks = []                                 #
for i in range(40):                                 # Inializes a list that holds all the
    occupiedBlocks.append((i, GROUND//GRIDSIZE))    # occupied blocks on the screen
    occupiedBlocks.append((i, 0))                   #
#---------------------------------------------------#

def fill(x, y, sizeX, sizeY, screen, gridsize, img):
    """ (int, int, int, int, str, int, image) -> (none)
    Fills a rectangle with a given size with a given image
    """
    x *= gridsize
    y *= gridsize
    for i in range (sizeX): # Loop through the width
        for j in range (sizeY): # Loop through the height
            screen.blit(img, (x+i*gridsize,y+j*gridsize)) # Draw the image

def spawn(obstacle, occupied):
    """ (list, list) -> (list, list)
    Returns a list of the obstacles and the opccupied blocks when given the the same lists that it returns
    """
    choose = False # A variable used for the while loop
    while choose == False:
        num1 = r.randint(0,6) # Generates a random number corrisponding to the obstacle
        num2 = r.randint(0,len(available)-1) # Generates a random number corrisponding to the position
        if len(available) < 3: # If there are less than 3 positions available
            num1 = 6 # Spawn a wall
        if num1 == 0 and available[num2][2] == 2:   # Weight
            obstacle[num1].append(Weight(available[num2], GRIDSIZE)) # Append it to the obstacle list
            for i in range(len(availableBlocks)): # Run through all available blocks
                if availableBlocks[i][0] == available[num2][0] and availableBlocks[i][1] == available[num2][1]: # If the available block is the new position of the obstacle
                    break # Break the for loop
            availableBlocks.pop(i) # Pop the available position
            choose = True # Break the while loop
        elif num1 == 1: # Laser
            obstacle[num1].append(Laser(available[num2], GRIDSIZE)) # Append it to the obstacle list
            for i in range(len(availableBlocks)):
                if availableBlocks[i][0] == available[num2][0] and availableBlocks[i][1] == available[num2][1]:# If the available block is the new position of the obstacle
                    break # Break the for loop
            availableBlocks.pop(i)# Pop the available position
            choose = True # Break the while loop
        elif num1 == 2: # Spike
            obstacle[num1].append(Spike(available[num2], GRIDSIZE)) # Append it to the obstacle list
            for i in range(len(availableBlocks)):
                if availableBlocks[i][0] == available[num2][0] and availableBlocks[i][1] == available[num2][1]:# If the available block is the new position of the obstacle
                    break # Break the for loop
            availableBlocks.pop(i)# Pop the available position
            choose = True # Break the while loop
        elif num1 == 3 and available[num2][2] == 2: # Bomb
            obstacle[num1].append(Bomb(available[num2], GRIDSIZE)) # Append it to the obstacle list
            for i in range(len(availableBlocks)):
                if availableBlocks[i][0] == available[num2][0] and availableBlocks[i][1] == available[num2][1]:# If the available block is the new position of the obstacle
                    break # Break the for loop
            availableBlocks.pop(i)# Pop the available position
            choose = True # Break the while loop
        elif num1 == 4 and available[num2][2] == 0: # Spring
            obstacle[num1].append(Spring(available[num2], GRIDSIZE)) # Append it to the obstacle list
            for i in range(len(availableBlocks)):
                if availableBlocks[i][0] == available[num2][0] and availableBlocks[i][1] == available[num2][1]:# If the available block is the new position of the obstacle
                    break # Break the for loop
            availableBlocks.pop(i)# Pop the available position
            choose = True # Break the while loop
        elif num1 == 5: # Star shooter
            obstacle[num1].append(StarShooter(available[num2], GRIDSIZE)) # Append it to the obstacle list
            for i in range(len(availableBlocks)):
                if availableBlocks[i][0] == available[num2][0] and availableBlocks[i][1] == available[num2][1]:# If the available block is the new position of the obstacle
                    break # Break the for loop
            availableBlocks.pop(i)# Pop the available position
            choose = True # Break the while loop
        elif num1 == 6: # Blocks
            newBlocks = Blocks(available[num2], GRIDSIZE, r.randint(3,7)) # Make a new wall
            newBlocks.checkValidandReplace(GRIDSIZE, availableBlocks, available, obstacle[num1]) # Check to see if that wall is available
            occupied = newBlocks.addAvailable(GRIDSIZE, available, availableBlocks, occupied) # Add the walls position to the occupied list
            obstacle[num1].append(newBlocks) # Append it to the obstacle list
            available.pop(num2) # Pop the walls position from the available list
            choose = True # Break the while loop
    return obstacle, occupied

def redraw_screen():
    if gameScreen == 0: # If the game has not started yet
        for wall in Walls:                          # Draw the 
            wall.draw(screen, GRIDSIZE, wallImg)    # walls
        fill(1,1,38,18,screen,GRIDSIZE, backImg)            #
        fill(0,20,40,1,screen, GRIDSIZE, grassMidImg)       # Fill the screen with the proper images
        fill(0,21,40,4,screen, GRIDSIZE, grassCenterImg)    #
        screen.blit(largeP1, (largeP1X, largeP1Y))  #
        screen.blit(p1Lock, (largeP1X, p1LockY))    #
        screen.blit(largeP2, (largeP2X, largeP2Y))  #
        screen.blit(p2Lock, (largeP2X, p2LockY))    # Draws all the images
        screen.blit(largeP3, (largeP3X, largeP3Y))  # for the start screen
        screen.blit(p3Lock, (largeP3X, p3LockY))    #
        screen.blit(bridge,(largeP1X, bridgeY))     #
        screen.blit(bridge,(largeP2X, bridgeY))     #
        screen.blit(bridge,(largeP3X, bridgeY))     #
        message1 = 'Welcome to my first game without Ron in it'                         #
        message2 = 'Use the arrow keys to select a character, press space to confirm'   #
        message3 = '1. Use the arrow keys to move during the game'                      #
        message4 = '2. Try to get to the exit door'                                     #
        message5 = '3. Avoid the obstacles'                                             #
        message6 = '4. You have 5 chances to complete the level'                        #
        text1 = font.render(message1, 1, WHITE)                                         #
        text2 = font.render(message2, 1, WHITE)                                         #
        text3 = font.render(message3, 1, WHITE)                                         # Draws all the
        text4 = font.render(message4, 1, WHITE)                                         # start screen test
        text5 = font.render(message5, 1, WHITE)                                         #
        text6 = font.render(message6, 1, WHITE)                                         #
        screen.blit(text1, (GRIDSIZE*8,GRIDSIZE*1.5))                                   #
        screen.blit(text2, (GRIDSIZE*2.5,GRIDSIZE*3))                                   #
        screen.blit(text3, (GRIDSIZE*1,GRIDSIZE*20.5))                                  #
        screen.blit(text4, (GRIDSIZE*1,GRIDSIZE*21.5))                                  #
        screen.blit(text5, (GRIDSIZE*1,GRIDSIZE*22.5))                                  #
        screen.blit(text6, (GRIDSIZE*1,GRIDSIZE*23.5))                                  #
        if playerNum == 0: # Green player
            screen.blit(key, (largeP1X+11, keyY)) # Draw the key under the player
        elif playerNum == 1: # Blue player
            screen.blit(key, (largeP2X+11, keyY)) # Draw the key under the player
        else: # Red player
            screen.blit(key, (largeP3X+11, keyY)) # Draw the key under the player
    elif gameScreen == 1: # If the game is being played
        for wall in Walls:                          # Draw the 
            wall.draw(screen, GRIDSIZE, wallImg)    # walls
        fill(1,1,38,18,screen,GRIDSIZE, backImg)            #
        fill(0,20,40,1,screen, GRIDSIZE, grassMidImg)       # Fill the screen with the proper images
        fill(0,21,40,4,screen, GRIDSIZE, grassCenterImg)    #
        screen.blit(doorImgTop, (doorX*GRIDSIZE, doorY*GRIDSIZE))                   #
        screen.blit(doorImgBottom, (doorX*GRIDSIZE, doorY*GRIDSIZE+GRIDSIZE*2))     #
        screen.blit(door2ImgTop, (doorX2*GRIDSIZE, doorY2*GRIDSIZE))                #
        screen.blit(door2ImgBottom, (doorX2*GRIDSIZE, doorY2*GRIDSIZE+GRIDSIZE*2))  #
        screen.blit(exitSign, (exitX, exitY))                                       # Draws al the images for the main game
        screen.blit(heartImg, (heartX, heartY))                                     #
        screen.blit(hudXImg, (hudX, hudY))                                          #
        screen.blit(numbersImg[player.lives], (numX, numY))                         #
        screen.blit(giveupImg,(giveupX, giveupY))                                   #
        message1 = 'Level:' + str(level)                   #
        text1 = font2.render(message1, 1, WHITE)            # Draw the text on the screen
        screen.blit(text1, (GRIDSIZE*8.5,GRIDSIZE*21+10))   #
        #---Draws the player---#
        player.draw(screen, playerStandL[playerNum], playerStand[playerNum], jumpImgL[playerNum], jumpImg[playerNum], playerImg[playerNum*2],  playerImg[playerNum*2+1], framecount)
        for weight in obstacles[0]:                                 #
            weight.draw(screen, weightImg)                          #
        for laser in obstacles[1]:                                  #
            laser.laserDraw(screen, laserBeamImg)                   #
            laser.draw(screen, laserImg)                            #
        for spike in obstacles[2]:                                  #
            spike.draw(screen, spikeImg)                            #
        for bomb in obstacles[3]:                                   #
            if bomb.explode:                                        #
                bomb.bombExplode(screen, explosionImg, GRIDSIZE)    # Draws all of the obstacles
            else:                                                   # on the screen
                bomb.bombDraw(screen, bombImg)                      #
            bomb.draw(screen, bombShooterImg)                       #
        for spring in obstacles[4]:                                 #
            spring.draw(screen, springImg)                          #
        for star in obstacles[5]:                                   #
            star.starDraw(screen, starImg)                          #
            star.draw(screen, starShooterImg)                       #
        for blocks in obstacles[6]:                                 #
            blocks.draw(screen, blockImg)                           #
    else: # If the game is over
        for wall in Walls:                          # Draw the 
            wall.draw(screen, GRIDSIZE, wallImg)    # walls
        fill(1,1,38,18,screen,GRIDSIZE, backImg)            #
        fill(0,20,40,1,screen, GRIDSIZE, grassMidImg)       # Fill the screen with the proper images
        fill(0,21,40,4,screen, GRIDSIZE, grassCenterImg)    #
        screen.blit(playerImglarge[playerNum][framecount%11], (GRIDSIZE*1, GRIDSIZE*2.5)) # Draws the player image on the screen
        message1 = 'You got to level ' + str(level)     #
        message2 = 'LOL Ron would'                      #
        message3 = 'have done better!'                  #
        message4 = 'Better luck next'                   #
        message5 = 'time?'                              #
        text1 = font2.render(message1, 1, WHITE)        #
        text2 = font2.render(message2, 1, WHITE)        #
        text3 = font2.render(message3, 1, WHITE)        # Draws all of the text on the screen
        text4 = font2.render(message4, 1, WHITE)        #
        text5 = font2.render(message5, 1, WHITE)        #
        screen.blit(text1, (GRIDSIZE*14, GRIDSIZE*2))   #
        screen.blit(text2, (GRIDSIZE*14, GRIDSIZE*6))   #
        screen.blit(text3, (GRIDSIZE*14, GRIDSIZE*9))   #
        screen.blit(text4, (GRIDSIZE*14, GRIDSIZE*13))  #
        screen.blit(text5, (GRIDSIZE*14, GRIDSIZE*16))  #
    pygame.display.update() # Updates the screen

while inPlay:   # Runs a while loop for the main code
    if gameScreen == 0: # If the game hasn't started
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # Quit
                inPlay = False              # 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:                 #
                    player = Player(doorX2*GRIDSIZE+5, -100)    # Start the
                    player.y = GROUND - player.height           # game
                    gameScreen = 1                              #
                if event.key == pygame.K_LEFT and playerNum > 0:    #
                    playerNum -= 1                                  # Move the key
                if event.key == pygame.K_RIGHT and playerNum < 2:   # under the players
                    playerNum += 1                                  #
    elif gameScreen == 1: # If the game is being played
        occupied = occupiedBlocks + weightBlocks # Sets up the list of all the blocks that 
        framecount += 1 # Increase framecount
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT] and rightTrigger == False: # Right
            if player.x < WIDTH-GRIDSIZE*2: # If it can move right
                if (math.ceil((player.x+10)/ GRIDSIZE), math.floor((player.y+player.height/2)/GRIDSIZE)) not in occupied and (math.ceil((player.x+10)/ GRIDSIZE), math.floor(player.y/GRIDSIZE)) not in occupied: # If it can move right
                    player.move_right() # Move
                    if player.move != 'jump':   #
                        player.move = 'right'   # Change the player image 
                    player.moveOld = 'right'    #
                else:
                    player.stopX() # Stop the player
            else:
                player.stopX() # Stop the player
        elif keys[pygame.K_LEFT]: # Left
            if player.x > GRIDSIZE: # If it can move left
                 if (math.floor(player.x / GRIDSIZE), math.floor((player.y+player.height/2)/GRIDSIZE)) not in occupied and (math.floor(player.x / GRIDSIZE), math.floor(player.y/GRIDSIZE)) not in occupied: # If it can move left
                    player.move_left() # Move
                    if player.move != 'jump':   #
                        player.move = 'left'    # Change the player image
                    player.moveOld = 'left'     #
                 else:
                    player.stopX() # Stop the player
            else:
                player.stopX() # Stop the player
        else:
            player.stopX() # Stop the player

        if keys[pygame.K_RIGHT] == False: # If you let go of right
            rightTrigger = False # Let you move                                                                                                     
            
        if keys[pygame.K_LEFT] == False and keys[pygame.K_RIGHT] == False and player.speedY == 0 and player.move != 'jump': # If the player is not moving
            player.move = 'none' # Tell the game that the player has stopped
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # Quit
                inPlay = False              #
            if event.type == pygame.MOUSEBUTTONDOWN:                                            #
                (mX,mY)=pygame.mouse.get_pos()                                                  # Give up
                if giveupX <= mX <= giveupX + giveupW and giveupY <= mY <= giveupY + giveupH:   # button
                    gameScreen = 2                                                              #
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:    #
                    if player.jumps > 0:        # Jumps
                        player.jump()           #
                        player.jumps += -1      #
                        
#-------------------------------------------------------------------#
        xFloor = math.floor((player.x + player.width/2)/ GRIDSIZE)  #
        xCeil = math.ceil((player.x + player.width/2)/ GRIDSIZE)    # Sets up variables
        yFloor = math.floor((player.y-player.height/2)/GRIDSIZE)    # for simplifying if statements
        yCeil = math.ceil((player.y-player.height/2)/GRIDSIZE)      #
#-------------------------------------------------------------------#
        
        if player.moveOld == 'right':   #
            xFloor -= 1                 # Adjust the player
            xCeil -= 1                  #
            
        if player.move == 'jump':                                           #
            if (xFloor, yCeil) in occupied or (xCeil, yCeil) in occupied:   #
                player.stopY()                                              # Stop the player when it hits its head
                while (player.y - player.height/2) % GRIDSIZE != 0:         #
                    player.y += 1                                           #
                    
        if (xCeil, math.floor((player.y+player.height)/GRIDSIZE)) not in occupied and (xFloor, math.floor((player.y+player.height)/GRIDSIZE)) not in occupied: # If the player can fall
            player.fall(gravity, mach) # Fall
            stopYTrigger = False
        elif stopYTrigger == False and player.speedY > 0: # If the player needs to stop
            player.stopY() # Stop 
            while (player.y + player.height) % GRIDSIZE != 0:   # Move onto
                player.y -= 1                                   # the grid
            player.move = player.moveOld    #
            player.jumps = 2                # Adjust player values
            stopYTrigger = True             #

        if player.speedY == 0 and player.move != 'jump': # Reset
            player.jumps = 2                             # jumps

        if player.y+player.height == GROUND and player.x > doorX*GRIDSIZE: # If the player hits the exit door
            rightTrigger = True
            player.lives = 5 # Reset lives
            level += 1 # Level up
            for i in obstacles[0]:  #
                i.bringToTop()      #
                i.sound = False     #
            for i in obstacles[1]:  #
                i.clearShots()      # Reset all obstacles
            for i in obstacles[3]:  #
                i.shoot()           #
            for i in obstacles[5]:  #
                i.clearShots()      #
            (obstacles, occupiedBlocks) = spawn(obstacles,occupiedBlocks) # Spawn a new obstacle
            weightBlocks = [] # Clear weightBlocks
            frameCount = 0 # Reset framecount
            player.respawn() # Respawn the player

        if player.death: # If the player dies
            rightTrigger = True
            oof.play() # Playe the death sound
            for i in obstacles[0]:  #
                i.bringToTop()      #
                i.sound = False     #
            for i in obstacles[1]:  #
                i.clearShots()      #
            for i in obstacles[3]:  # Reset all of the obstacles
                i.shoot()           #
            for i in obstacles[5]:  #
                i.clearShots()      #
            weightBlocks = []       #
            frameCount = 0          #
            player.death = False # Break the if statement

        if player.lives < 0:    # Ends the game
            gameScreen = 2      #
            
        if player.speedY > 0:       #
            groundTrigger = False   # Tells the game that the player is stopped
            wallTrigger = False     #

        for i in obstacles[0]:  # Weights
            i.checkDrop(GRIDSIZE, player, obstacles[6]) # Checks to see how far it can fall and if it should fall
            i.collision(GRIDSIZE, player) # Checks to see if it hit a player
            if i.state == 0: # If it is falling
                weightBlocks = i.drop(GRIDSIZE, fallSpeed, obstacles[6], weightBlocks)
            if i.state == 2 and i.sound == False: # If it hit the ground
                weightSound.play()
                i.sound = True # Tell the game that it has played a sound

        for i in obstacles[1]:  # Lasers
            if len(i.laserBeam) > 0:
                i.collision(GRIDSIZE, player) # Checks to see if it hit a player
                
        for i in obstacles[2]: # Spikes
            i.collision(GRIDSIZE, player)

        for i in obstacles[3]:  # Bombs
            if i.firstShot == False:
                i.shoot()
                i.firstShot = True
            i.bombDrop(GRIDSIZE, bombSpeed, obstacles[6])
            if framecount % 30 == 0:
                i.timer = (i.timer + 1) % 4 # Increase the timer of the bomb
            if i.timer == 0 and i.newBombTrigger == False:
                bombSound.play()        #
                i.explode = True        # Explodes the bomb
                i.newBombTrigger = True #
            if i.timer > 0:   
                i.newBombTrigger = False
            i.playerCollision(GRIDSIZE, player) # Checks to see if it hit a player

        for i in obstacles[4]:  # Springs
            i.collision(GRIDSIZE, player) # Checks to see if it hit a player
            if i.sound:
                springSound.play()
                i.sound = False
        
        for i in obstacles[5]:  # Starshooters
            i.starMove(starSpeed)
            i.collision(GRIDSIZE, obstacles[6])
            i.playerCollision(GRIDSIZE, player) # Checks to see if it hit a player
            
        if framecount % shootSpeed == 0 and len(obstacles[5]) > 0:
            starshooterSound.play()
            for i in obstacles[5]:
                i.shoot() # Shoots stars

        if framecount % laserSpeed == 0:
            if laserShootTrigger == False:
                for i in obstacles[1]:
                    i.shoot(GRIDSIZE, obstacles[6]) #Shoots lasers
                    laserSound.play()
                laserShootTrigger = True
            else:
                for i in obstacles[1]:
                    i.clearShots() # Clears the lasers on the screen
                laserShootTrigger = False
                
        player.update() # Move the player
        
    else: # If the game is over
        for event in pygame.event.get():    #
            if event.type == pygame.QUIT:   # Allow the player to quit
                inPlay = False              #
        framecount+=1 # Increase framerate for the image
    redraw_screen() # Redraw the screen

pygame.quit() # Quit pygame
