import kandinsky
import ion
import math
import time
import random

playerX = 145
playerSize = 30
playerVelocity = 0
crateSize = playerSize
crateX = random.randint(0,320 - playerSize)
crateY = 0
crateVelocity = 0
crateDistance = math.fabs(playerX - crateX)
running = True
score = ""
playerSpeed = 5

while running :

    # Update player position
    crateY += crateVelocity
    playerX += playerVelocity
    
    # Manages player input
    if ion.keydown(ion.KEY_LEFT):
        playerVelocity = - playerSpeed
    if ion.keydown(ion.KEY_RIGHT):
        playerVelocity = playerSpeed

    # Calculates the distance of the player from the crate
    crateDistance = math.fabs(playerX - crateX)

    # Creates map wrap
    if playerX > 320 :
        playerX = -playerSize
    if playerX < -playerSize :
        playerX = 320
    
    # Caps the speed of the crate
    if crateVelocity < 5 :
        crateVelocity += 1
    
    # Resets crate position when it touches the ground and increments the score
    if crateY >= 222 - crateSize:
        crateY = 0
        crateX = random.randint(0,320 - playerSize)
        score += "*"
    
    # Game Over system
    if crateY >= 222 - crateSize - playerSize and crateDistance <= playerSize:
        running = False
    # Renders the objects
    kandinsky.fill_rect(playerX,222 - playerSize, playerSize, playerSize,kandinsky.color(0,0,0))
    kandinsky.fill_rect(crateX,crateY, crateSize, crateSize,kandinsky.color(255,0,0))
    kandinsky.draw_string(score,0,0)
    time.sleep(1/60)
    kandinsky.fill_rect(playerX,222 - playerSize, playerSize, playerSize,kandinsky.color(255,255,255))
    kandinsky.fill_rect(crateX,crateY, crateSize, crateSize,kandinsky.color(255,255,255))

# Ends the game
kandinsky.draw_string("Game Over",0,0)
time.sleep(1)
print("Score:",len(score))
print("Game by Henri Caboche")