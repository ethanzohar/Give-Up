#----------------------------------------------#
# Final Game Classes                           #
# By: Ethan Zohar                              #
# June 19, 2017                                #
# Holds all of the classes for my final game   #
#----------------------------------------------#

import random as r      # Imports used
import math             # Modules

#---------------------------------------------------------------------------------------#

class Weight(object):
    """ A block that falls from the sky killing the player
        data:                           behaviour:
            x - x                           checkDrop
            y - y                           drop
            OrgX - Original x               bringToTop
            OrgY - Original y               collision
            state - falling or not          Draw
            sound - playing a sound or not
    """
    def __init__(self, placement, gridsize):
        (x,y, face) = placement
        x *= gridsize
        y *= gridsize
        self.x = x
        self.y = y
        self.OrgX = x
        self.OrgY = y
        self.state = 1
        self.sound = False

    def checkDrop(self, gridsize, player, otherBlocks):
        """ (int, class, list) -> (none)
        Checks to see how far the weight can fall
        """
        if (self.x - gridsize <= player.x <= self.x + gridsize or self.x - gridsize <= player.x + player.width <= self.x + gridsize) and self.state == 1: # Checks to see if the player is under the weight
            collides = False    # Initializes variables
            j = 0               # For the while loop
            while collides == False: # While the weight is falling
                clear = True
                checkX = self.x
                checkY = self.y + j*gridsize
                check = (checkX, checkY) # Creates a tuple of the weights x and y
                for i in otherBlocks: # Run through all the blocks
                    if check in i.final: # If they collide
                        clear = False
                        collides = True
                if checkY > player.y+player.height: # If it hits the ground
                    collides = True
                j += 1 # Adds 1 to j for the y
            if clear: # If clear is still true
                self.state = 0 # Draw a new picture

    def drop(self, gridsize, fallSpeed, otherBlocks, weightBlocks):
        """ (int, int, list, list) -> (list)
        Returns a list of blocks that the weights occupy and drops the weights
        """
        maxDrop = gridsize*18       # 
        collides = False            # Initializes variables for the while loop
        j = 0                       #
        while collides == False: # While the weight is falling
            checkX = self.x
            checkY = self.y + j*gridsize
            check = (checkX, checkY) # Creates a tuple of the weights x and y
            for i in otherBlocks: # Run through all the blocks
                if check in i.final: # If they collide
                    collides = True
                    maxDrop = checkY - gridsize # Max drop changes
            if checkY > maxDrop: # If the weight is at maxDrop
                collides = True
            j += 1 # Adds 1 to j for the y
        if self.y < maxDrop: # If the y is less than the max drop
            self.y += fallSpeed # Move down
        else: # If it is at maxDrop
            self.state = 2 # Change image
            weightBlocks.append((self.x//gridsize, self.y/gridsize)) # Add it to weightBlocks
        return weightBlocks

    def bringToTop(self):
        """ (none) -> (none)
        Brings all the weights to the top of the screen
        """
        self.state = 1
        self.x = self.OrgX
        self.y = self.OrgY

    def collision(self, gridsize, player):
        """ (int, class) -> (none)
        Checks the collision between the player and the weight
        """
        if self.x <= player.x <= self.x + gridsize or self.x <= player.x + player.width <= self.x + gridsize: # Checks to see if it is in the players x
            if self.y <= player.y <= self.y + gridsize or self.y <= player.y + player.height <= self.y + gridsize: # Checks to see if it is in the players y
                if self.state == 0: # Checks to see if it is falling
                    player.kill() # Kill the player
    
    def draw(self, surface, image):
        """ (str, image) -> (none)
        Draws the weights
        """
        if self.state == 1:                             #
            surface.blit(image[1], (self.x, self.y))    # Draw a different image
        else:                                           # depending on the state
            surface.blit(image[0], (self.x, self.y))    #

#---------------------------------------------------------------------------------------#
        
class Laser(object):
    """ A block that shoots a laser killing the player
        data:                             behaviour:
            x - x                             laserDraw
            y - y                             clearShots
            around - size of image            collision
            size - size of image              draw
            laserBeam - list holding lasers   shoot
            facing - facing direction
    """
    def __init__(self, placement, gridsize):
        (x,y, face) = placement
        x *= gridsize
        y *= gridsize
        self.x = x
        self.y = y
        self.around = 8
        self.size = 19
        self.laserBeam = []
        self.facing = face

    def draw(self, surface, image):
        """ (str, image) -> (none)
        Draws the laser shooters
        """
        surface.blit(image[self.facing], (self.x, self.y))

    def shoot(self, gridsize, otherBlocks):
        """ (int, list) -> (none)
        Creates the laser beams positions
        """
        collides = False    # Initializes variables 
        j = 0               # for the while loop
        while collides == False: # While the laser has not collided
            append = True
            if self.facing == 0: # Up
                checkX = self.x
                checkY = self.y - j*gridsize
                check = (checkX, checkY) # Creates a tuple of the lasers x and y 
                for i in otherBlocks: # Runs through all the blocks
                    if check in i.final: # If they collide
                        collides = True
                        append = False # Dont append
                if checkY < gridsize: # If it hits the edge
                    collides = True
                    append = False # Dont append
            elif self.facing == 1: # Right
                checkX = self.x + j*gridsize
                checkY = self.y
                check = (checkX, checkY) # Creates a tuple of the lasers x and y
                for i in otherBlocks: # Runs through all the blocks
                    if check in i.final: # If they collide
                        collides = True
                        append = False # Dont append
                if checkX > gridsize*38: # If it hits the edge
                    collides = True
                    append = False # Dont append
            elif self.facing == 2: # Down
                checkX = self.x
                checkY = self.y + j*gridsize
                check = (checkX, checkY) # Creates a tuple of the lasers x and y
                for i in otherBlocks: # Runs through all the blocks
                    if check in i.final: # If they collide
                        collides = True
                        append = False # Dont append
                if checkY > gridsize*18: # If it hits the edge
                    collides = True
                    append = False # Dont append
            elif self.facing == 3: # Left
                checkX = self.x - j*gridsize
                checkY = self.y
                check = (checkX, checkY) # Creates a tuple of the lasers x and y
                for i in otherBlocks: # Runs through all the blocks
                    if check in i.final: # If they collide
                        collides = True
                        append = False # Dont append
                if checkX < gridsize: # If it hits the edge
                    collides = True
                    append = False # Dont append
            if append == True:
                self.laserBeam.append((checkX, checkY, self.facing)) # Append the position to the laser beam list
            j += 1 # Adds 1 to j for the y

    def laserDraw(self, surface, image):
        """ (str, image) -> (none)
        Draws the laser beams
        """
        for i in self.laserBeam:
            (x, y, face) = i
            surface.blit(image[self.facing%2], (x, y))

    def clearShots(self):
        """ (none) -> (none)
        Clears the laserBeam
        """
        self.laserBeam = [] # Clears the laser beams

    def collision(self, gridsize, player):
        """ (int, class) -> (none)
        Checks the collision between the player and the laser beam
        """
        for i in self.laserBeam: # Run through each of the laser beams
            (x,y,f) = i # Position
            if f == 0: # Up/Down
                if x + self.around < player.x + player.width and x + self.around + self.size > player.x: # If the x's line up
                    if y < player.y + player.height and y + gridsize > player.y: # If the y's line up
                        player.kill() # Kill the player
            else:   # Left/Right
                if x < player.x + player.width and x + gridsize > player.x: # If the x's line up
                    if y + self.around < player.y + player.height and y + self.around + self.size > player.y: # If the y's line up
                        player.kill() # Kill the player

#---------------------------------------------------------------------------------------#
        
class Spike(object):
    """ A block that kills the player when touched
        data:                           behaviour:
            x - x                           draw
            y - y                           collision
            facing - facing direction
    """
    def __init__(self, placement, gridsize):
        (x,y, face) = placement
        x *= gridsize
        y *= gridsize
        self.x = x
        self.y = y
        self.facing = face

    def draw(self, surface, image):
        """ (str, image) -> (none)
        Draws the spikes
        """
        surface.blit(image[self.facing], (self.x, self.y))
        
    def collision(self, gridsize, player):
        """ (int, class) -> (none)
        Checks the collision between the player and the spike
        """
        if self.facing == 0: # Up
            if (self.x <= player.x <= self.x + gridsize or self.x <= player.x + player.width <= self.x + gridsize) and self.y <= player.y + player.height <= self.y + gridsize: # If they collide
                player.kill() # Kill the player
        elif self.facing == 1: # Right
            if (self.y <= player.y <= self.y + gridsize or self.y <= player.y + player.height <= self.y + gridsize) and self.x <= player.x <= self.x + gridsize: # If they collide
                player.kill() # Kill the player
        elif self.facing == 2: # Down
            if (self.x <= player.x <= self.x + gridsize or self.x <= player.x + player.width <= self.x + gridsize) and self.y <= player.y <= self.y + gridsize: # If they collide
                player.kill() # Kill the player
        elif self.facing == 3: # Left
            if (self.y <= player.y <= self.y + gridsize or self.y <= player.y + player.height <= self.y + gridsize) and self.x <= player.x + player.width <= self.x + gridsize: # If they collide
                player.kill() # Kill the player

#---------------------------------------------------------------------------------------#
        
class Bomb(object):
    """ A block shoots falling bombs that kill when exploded on the player
        data:                              behaviour:
            x - x                              shoot
            y - y                              bombDrop
            maxTimer - 3 seconds               draw
            timer - current time on bomb       bombDraw
            bombState - state of falling bomb  bombExplode
            bombSize - image size              playerCollision
            explode - boolean
            firstShot - boolean
            newBombTrigger - boolean
    """
    def __init__(self, placement, gridsize):
        (x,y, face) = placement
        x *= gridsize
        y *= gridsize
        self.x = x
        self.y = y
        self.maxTimer = 3
        self.timer = 1
        self.bombState = 1
        self.bombSize = gridsize
        self.explode = False
        self.firstShot = False
        self.newBombTrigger = False

    def shoot(self):
        """ (none) -> (none)
        Shoot a bomb
        """
        self.bombX = self.x     #
        self.bombY = self.y     #
        self.bombState = 1      # Creates a new bomb at the cannon
        self.timer = 1          # 
        self.frame = 0          #
        
    def bombDrop(self, gridsize, fallSpeed, otherBlocks):
        """ (int, int, list) -> (none)
        Drops the bombs
        """
        if self.timer > 0: # If the bomb is not due to explode
            maxDrop = gridsize*18   #
            collides = False        # Initializes values for the while loop
            j = 0                   #
            while collides == False: # While the bomb should still fall
                checkX = self.x
                checkY = self.y + j*gridsize
                check = (checkX, checkY) # Creates a tuple of the bombs x and y 
                for i in otherBlocks:    # Runs through all blocks
                    if check in i.final: # If they collide
                        collides = True
                        maxDrop = checkY - gridsize # Max drop changes
                if checkY > maxDrop:     # If its greater than maxDrop
                    collides = True
                j += 1                   # Adds 1 to j for the y
            if self.bombY < maxDrop:     # If it should fall
                self.bombY += fallSpeed  # move down
    
    def draw(self, surface, image):
        """ (str, image) -> (none)
        Draws the cannons
        """
        surface.blit(image, (self.x, self.y))

    def bombDraw(self, surface, image):
        """ (str, image) -> (none)
        Draws the bombs
        """
        if self.timer > 0:
            surface.blit(image[self.timer-1], (self.bombX, self.bombY))

    def bombExplode(self, surface, image, gridsize):
        """ (str, image, int) -> (none)
        Draws the bombs exploding
        """
        surface.blit(image[self.frame], (self.bombX-gridsize, self.bombY-gridsize))
        self.frame += 1
        if self.frame == 12: # If the animation is over
            self.shoot() # Shoot a new bomb
            self.explode = False # Explode is set to false
            self.timer = 0  # Reset timer

    def playerCollision(self, gridsize, player):
        """ (int, class) -> (none)
        Checks the collision between the player and the bomb
        """
        if self.explode: # If its exploding
            if self.bombX - gridsize <= player.x + player.width and self.bombX + self.bombSize + gridsize >= player.x: # If the player is in the x
                if self.bombY - gridsize <= player.y + player.height and self.bombY + self.bombSize + gridsize >= player.y: # If the player is in the y
                    player.kill() # Kill the player

#---------------------------------------------------------------------------------------#
        
class Spring(object):
    """ A block that makes the player jump
        data:                           behaviour:
            x - x                           collision
            y - y                           draw
            state - down or up
            sound - boolean
    """
    def __init__(self, placement, gridsize):
        (x,y, face) = placement
        x *= gridsize
        y *= gridsize
        self.x = x
        self.y = y
        self.state = 1
        self.sound = False

    def collision(self, gridsize, player):
        """ (int, class) -> (none)
        Checks the collision between the player and the spring
        """
        if (self.x <= player.x <= self.x + gridsize or self.x <= player.x + player.width <= self.x + gridsize) and self.y <= player.y + player.height <= self.y + gridsize: # If the player is in the spring
            self.state = 0 # Change image
            self.sound = True # Play a sound
            player.jump() # Jump
        else:
            self.state = 1 # Change image

    def draw(self, surface, image):
        """ (str, image) -> (none)
        Draws the springs
        """
        if self.state == 0: # Down
            surface.blit(image[0],(self.x, self.y))
        else: # Up
            surface.blit(image[1],(self.x, self.y))

#---------------------------------------------------------------------------------------#

class StarShooter(object):
    """ A block that falls from the sky killing the player
        data:                           behaviour:
            x - x                           draw
            y - y                           shoot
            star - list of stars            starDraw
            starAroundX - image size        collision
            starAroundY - image size        clearShots
            starSizeX - image size          starMove
            starSizeX - image size          playerCollision
            facing - facing direction
    """
    def __init__(self, placement, gridsize):
        (x,y, face) = placement
        x *= gridsize
        y *= gridsize
        self.x = x
        self.y = y
        self.stars = []
        self.starAroundX = 9
        self.starAroundY = 10
        self.starSizeX = 17
        self.starSizeY = 16
        self.facing = face

    def draw(self, surface, image):
        """ (str, image) -> (none)
        Draws the star shooters
        """
        surface.blit(image[self.facing], (self.x, self.y))

    def shoot(self):
        """ (none) -> (none)
        Creates a new star
        """
        self.stars.append((self.x, self.y, self.facing))

    def starDraw(self, surface, image):
        """ (str, image) -> (none)
        Draws the stars
        """
        for i in self.stars:
            (x, y, face) = i
            surface.blit(image, (x, y))

    def collision(self, gridsize, otherBlocks):
        pop = [] # Creates an empty list to pop later
        for i in range(len(self.stars)): # Runs throught the index of all the stars
            (x,y,f) = self.stars[i] # Position
            if x < gridsize or x > 38*gridsize: # If the x is off the edge
                pop.append(i) # Add the index to the pop list
            elif y < gridsize or y > 18*gridsize: # If the y is off the edge
                pop.append(i) # Add the index to the pop list
            for j in otherBlocks: # Runs through all the blocks
                check = (x,y) # Creates a tuple of the stars x and y 
                if check in j.final: # If they collide
                    pop.append(i) # Add the index to the pop list
        for i in range(len(pop)): # Run through the index of the pop list
            self.stars.pop(pop[i]) # Pop all the pop lists indexes from the stars list
        
    def clearShots(self):
        """ (none) -> (none)
        Clears all the shots of the star shooters
        """
        self.stars = []

    def starMove(self, starSpeed):
        """ (int) -> (none)
        Moves the stars
        """
        moved = [] # Creates an empty list where all the moves stars will be placed
        for i in self.stars: # Runs through all the stars
            (starX,starY,facing) = i # Position
            if facing == 0: # Up
                starY += -starSpeed # Move the star
            elif facing == 1: # Right
                starX += starSpeed # Move the star
            elif facing == 2: # Down
                starY += starSpeed # Move the star
            elif facing == 3: # Left
                starX += -starSpeed # Move the star
            moved.append((starX, starY, facing)) # Add the new position for the moved list
        self.stars = moved # Move all the stars at once

    def playerCollision(self, gridsize, player):
        """ (int, class) -> (none)
        Checks the collision between the player and the stars
        """
        for i in self.stars: # Runs through all the stars
            (x,y,f) = i # Position
            if x + self.starAroundX < player.x + player.width and x + self.starAroundX + self.starSizeX > player.x: # If the x's line up
                if y + self.starAroundY < player.y + player.height and y + self.starAroundY + self.starSizeY > player.y: # if the y's line up
                    player.kill() # Kills the player

#---------------------------------------------------------------------------------------#

class Blocks(object):
    """ A block that is used to create walls
        data:                           behaviour:
            x - x                           checkValidandReplace
            y - y                           addAvailable
            size - amount of blocks         draw
            facing - direction of wall
    """
    def __init__(self, placement, gridsize, size):
        (x,y, face) = placement
        x *= gridsize
        y *= gridsize
        self.x = x
        self.y = y
        self.size = size
        self.facing = r.randint(0,1)
            
    def checkValidandReplace(self, gridsize, availableBlocks, available, otherBlocks):
        """ (int, list, list, list) -> (none)
        Checks to see if the random wall placed is valid
        """
        choose = False      #
        self.final = []     # Initializes variables used in the while loop
        save = []           #
        while choose == False:
            valid = True
            if self.facing == 0:    # Going Sideways
                for i in range(self.size): # Runs through the size of the new wall
                    checkX = (self.x/gridsize)+i
                    checkY = self.y/gridsize
                    check = (checkX,checkY) # Creates a tuple of the new walls x and y 
                    blockCheckX = self.x + i*gridsize
                    blockCheckY = self.y
                    blockCheck = (blockCheckX, blockCheckY) # Creates a tuple of the new walls x and y 
                    if check not in availableBlocks: # If the position is not available
                        valid = False
                    for j in otherBlocks: # Runs through all of the other blocks
                        if blockCheck in j.final: # If they collide
                            valid = False
            else:   # Going Down
                for i in range(self.size): # Runs through the size of the new wall
                    checkX = self.x/gridsize
                    checkY = (self.y/gridsize)+i
                    check = (checkX,checkY) # Creates a tuple of the new walls x and y 
                    blockCheckX = self.x
                    blockCheckY = self.y + i*gridsize
                    blockCheck = (blockCheckX, blockCheckY) # Creates a tuple of the new walls x and y 
                    if check not in availableBlocks: # If the position is not available
                        valid = False
                    for j in otherBlocks: # Runs through all of the other blocks
                        if blockCheck in j.final: # If they collide
                            valid = False
            if valid == False and len(availableBlocks)>0: # If the wall is not valid
                (self.x, self.y) = availableBlocks[r.randint(0,len(availableBlocks)-1)] # 
                self.x *= gridsize                                                      # Give it a new start point
                self.y *= gridsize                                                      #
                self.facing = r.randint(0,1) # Give it a random direction
            else:
                choose = True
        for i in range(self.size): # Runs through the size of the new wall
            if self.facing == 0:    # Going Sideways
                self.final.append((self.x + i*gridsize,self.y)) # Add its position to the final list
            else:   # Going Down
                self.final.append((self.x,self.y + i*gridsize)) # Add its position to the final list
            for j in range(len(available)): # Runs through all available
                for k in range(len(self.final)): # Runs through all new final positions
                    if (available[j][0], available[j][1]) == (self.final[k][0]//gridsize, self.final[k][1]//gridsize): # If they collide
                        save.append(j) # Add it to saved
            if len(save) > 0: # If saved contains something
                for j in range(len(save)-1,-1,-1): # Run through it backwards
                    available.pop(save[j]) # Pop it from available
            save = [] # Reset save
            for j in range(len(availableBlocks)): # Runs through all available blocks
                for k in range(len(self.final)): # Runs through all new final positions
                    if (availableBlocks[j][0], availableBlocks[j][1]) == (self.final[k][0]//gridsize, self.final[k][1]//gridsize): # If they collide
                        save.append(j) # Add it to saved
            if len(save) > 0: # If saved contains something
                for j in save: # Run through save
                    availableBlocks.pop(int(i)) # Pop save from available blocks
            save = [] # Reset save

    def addAvailable(self, gridsize, available, availableBlocks, occupied):
        """ (int, list, list, list) -> (list)
        Returns a list of all occupied blocks and adds available blocks
        """
        if self.facing == 0: # Going Sideways
            for i in range(self.size): # Runs through the size of the wall
                x = (self.x+(i*gridsize))//gridsize
                y = self.y//gridsize
                occupied.append((x,y)) # Adds the x and y of the wall to occupied
                if 0 < y-1 < 19 and y-1 not in available and y-1 not in availableBlocks: # If 1 block above the new wall is valid
                    available.append((x,y-1,0)) # Add it to available
                    availableBlocks.append((x,y-1)) # Add it to available blocks
                if 0 < y+1 < 19 and y+1 not in available and y+1 not in availableBlocks: # If 1 block below the new wall is valid
                    available.append((x,y+1,2)) # Add it to available
                    availableBlocks.append((x,y+1)) # Add it to available blocks
            x = self.x//gridsize 
            y = self.y//gridsize
            if 0 < x-1 < 39 and x-1 not in available and x-1 not in availableBlocks: # If 1 block to the left of the wall is valid
                available.append((x-1, y, 3)) # Add it to available
                availableBlocks.append((x-1, y)) # Add it to available blocks
            if 0 < x+self.size < 39 and x+self.size not in available and x+self.size not in availableBlocks: # If 1 block to the right of the wall is valid
                available.append((x+self.size, y,1)) # Add it to available
                availableBlocks.append((x+self.size, y)) # Add it to available blocks
        else: # Going Down
            for i in range(self.size): # Runs through the size of the wall
                x = self.x//gridsize
                y = (self.y+(i*gridsize))//gridsize
                occupied.append((x,y)) # Adds the x and y of the wall to occupied
                if 0 < x-1 < 39 and x-1 not in available and x-1 not in availableBlocks:# If 1 block left of the new wall is valid
                    available.append((x-1,y,3)) # Add it to available
                    availableBlocks.append((x-1,y)) # Add it to available blocks
                if 0 < x+1 < 39 and x+1 not in available and x+1 not in availableBlocks:# If 1 block right of the new wall is valid
                    available.append((x+1,y,1)) # Add it to available
                    availableBlocks.append((x+1,y)) # Add it to available blocks
            x = self.x//gridsize
            y = self.y//gridsize
            if 0 < y-1 < 19 and y-1 not in available and y-1 not in availableBlocks: # If 1 block above the new wall is valid
                available.append((x, y-1, 0)) # Add it to available
                availableBlocks.append((x, y-1)) # Add it to available blocks
            if 0 < y+self.size < 19 and y+self.size not in available and y+self.size not in availableBlocks: # If 1 block below the new wall is valid
                available.append((x, y+self.size,2)) # Add it to available
                availableBlocks.append((x, y+self.size)) # Add it to available blocks
        return occupied
            

    def draw(self, surface, image):
        """ (str, image) -> (none)
        Draws the blocks
        """
        for i in self.final:
            (x,y) = i
            surface.blit(image, (x,y))

#---------------------------------------------------------------------------------------#

class Wall(object):
    """ Creates invisible walls
        data:                           behaviour:
            x - x                           draw
            y - y                           
            star - list of stars            
            length - length
            height - height
    """
    def __init__(self, x, y, gridsize, length, height):
        x *= gridsize
        y *= gridsize
        self.x = x
        self.y = y
        self.length = length
        self.height = height

    def draw(self, surface, gridsize, image):
        """ (str, int, image) -> (none)
        Draws the walls
        """
        for i in range(self.length):
            surface.blit(image, (self.x+i*gridsize, self.y))
        for i in range(self.height):
            surface.blit(image, (self.x, self.y+i*gridsize))

#---------------------------------------------------------------------------------------#

class Player(object):
    """ A block that falls from the sky killing the player
        data:                           behaviour:
            x - x                           draw
            y - y                           move_right
            speedX - speed                  move_left
            speedY - speed                  stopX
            jumps - number of jumps         stopY
            move - direction moving         update
            moveOld - old direction         jump
            height - image size             fall
            width - image size              respawn
            lives - lives left              kill
            death - boolean
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speedX = 0
        self.speedY = 0
        self.jumps = 2
        self.move = 'none'
        self.moveOld = 'none'
        self.height = 50
        self.width = 35
        self.lives = 5
        self.death = False
        
    def draw(self, surface, imageL, imageR, jumpL, jumpR, imageRight, imageLeft, framecount):
        """ (str, image, image, image, image, image, image, int) -> (none)
        Draws the player
        """
        if self.move == 'none' and (self.moveOld == 'right' or self.moveOld == 'none'):
            surface.blit(imageR, (self.x, self.y))
        elif self.move == 'none' and self.moveOld == 'left':
            surface.blit(imageL, (self.x, self.y))
        elif self.move == 'right':
            surface.blit(imageRight[framecount%11], (self.x, self.y))
        elif self.move == 'left':
            surface.blit(imageLeft[framecount%11], (self.x, self.y))
        elif self.move == 'jump':
            if self.moveOld == 'left':
                surface.blit(jumpL, (self.x, self.y))
            else:
                surface.blit(jumpR, (self.x, self.y))

    def move_right(self):
        """ (none) -> (none)
        Moves the player right
        """
        self.speedX = 10

    def move_left(self):
        """ (none) -> (none)
        Moves the player left
        """
        self.speedX = -10

    def stopX(self):
        """ (none) -> (none)
        Stops the player horizontally
        """
        self.speedX = 0
        
    def stopY(self):
        """ (none) -> (none)
        Stops the player vertically
        """
        self.speedY = 0

    def update(self):
        """ (none) -> (none)
        Updates the players position
        """
        self.x += self.speedX
        self.y += self.speedY

    def jump(self):
        """ (none) -> (none)
        Makes the player jump
        """
        self.move = 'jump' # Tells it that the player is jumping
        self.speedY = -15
        self.update()

    def fall(self, gravity, mach):
        """ (int, int) -> (none)
        Makes the player fall if they are below a certain speed
        """
        if self.speedY < mach:
            self.speedY += gravity

    def respawn(self):
        """ (none) -> (none)
        Respawns the player at the start door
        """
        self.x = 35                 #
        self.y = 520                #
        self.jumps = 2              # Resets all values
        self.move = 'none'          #
        self.moveOld = 'right'      #

    def kill(self):
        """ (none) -> (none)
        Kills the player
        """
        self.lives -= 1
        self.death = True
        self.respawn()

#---------------------------------------------------------------------------------------#
