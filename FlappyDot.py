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

while running :
    playerY += playerVelocity
    pipeX -= 1
    if pipeX <= -pipeSize:
        pipeX = 320
        gateY = random.randint(0,222 - gateSize)
        score += "*"
    if ion.keydown(ion.KEY_OK) == True:
        playerVelocity = -1
    else:
        playerVelocity = 1
    
    if  100 < pipeX < 100 + playerSize and not gateY < playerY < gateY + gateSize:
        running = False

    kandinsky.fill_rect(pipeX,0,playerSize,222,kandinsky.color(255,0,0))
    kandinsky.fill_rect(pipeX,gateY,playerSize,gateSize,kandinsky.color(255,255,255))
    kandinsky.fill_rect(100,playerY,playerSize,playerSize,kandinsky.color(0,0,0))
    time.sleep(1/500)
    kandinsky.draw_string(score,0,0)
    kandinsky.fill_rect(pipeX,0,playerSize,222,kandinsky.color(255,255,255))
    kandinsky.fill_rect(100,playerY,playerSize,playerSize,kandinsky.color(255,255,255))
kandinsky.draw_string("Game Over",0,0)
time.sleep(0.5)
print("Score:",len(score))
print("Game by HenriCaboche")