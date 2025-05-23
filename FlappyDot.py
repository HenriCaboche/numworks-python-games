import kandinsky
import ion
import time
import math
import random

playerY = 111 - 15
pipeX = 320
pipeSize = 30
playerSize = 30
gateSize = playerSize + 20
gateY = random.randint(0,222 - gateSize)
playerVelocity = 1
running = True
score = ""
score30 = ""
start = time.monotonic()
groundBuffer = 10

while running :

    # Update player and pipe position
    playerY += playerVelocity
    pipeX -= 1
    
    # Resets the pipe and increments the score
    if pipeX <= -pipeSize:
        pipeX = 320
        gateY = random.randint(0,222 - gateSize)
        score += "*"
    if len(score) >= 30 :
        score30 += "*"
        score = ""
        kandinsky.fill_rect(0,0,320,20,"white")

    # Manages player input
    if ion.keydown(ion.KEY_OK) == True:
        playerVelocity = -1
    else:
        playerVelocity = 1
    
    # Game over system
    if  100 < pipeX < 100 + playerSize and not gateY < playerY < gateY + gateSize:
        running = False
     # Kills the player if it goes below the screen
    if playerY > 222 + playerSize + groundBuffer :
        running = False

    # Renders the game
    kandinsky.fill_rect(pipeX,0,playerSize,222,kandinsky.color(255,0,0))
    kandinsky.fill_rect(pipeX,gateY,playerSize,gateSize,kandinsky.color(255,255,255))
    kandinsky.fill_rect(100,playerY,playerSize,playerSize,kandinsky.color(0,0,0))
    kandinsky.draw_string(score30,0,20)    
    time.sleep(1/500)
    kandinsky.draw_string(score,0,0)
    kandinsky.fill_rect(pipeX,0,playerSize,222,kandinsky.color(255,255,255))
    kandinsky.fill_rect(100,playerY,playerSize,playerSize,kandinsky.color(255,255,255))

# Ends game
kandinsky.draw_string("Game Over",0,0)
time.sleep(0.5)
print("Score:",len(score)+30*len(score30))
print ("Time:", round(time.monotonic() - start,1), "seconds")
print("Game by HenriCaboche")