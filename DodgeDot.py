import kandinsky
import time
import ion
import random
import math

crate_position_x = random.randint(0,290)
crate_position_y = 0
crate_falling_velocity = 0

player_position_x = 160
player_position_y = 111
player_velocity_y = 0
player_velocity_x = 0
score = ""

# Calculate the distance between the crate and the player
crate_distance_x = math.fabs(player_position_x - crate_position_x)

# Main game loop
while True :

    # Update the player position
    player_position_x += player_velocity_x
    player_position_y += player_velocity_y

    # Caps the speed of the crate
    if crate_falling_velocity < 5 :
        crate_falling_velocity += 1
    
    # Renders the player and the crate
    kandinsky.fill_rect(crate_position_x,crate_position_y,30,30,kandinsky.color(255,0,0))
    kandinsky.fill_rect(player_position_x,player_position_y,30,30,kandinsky.color(0,0,0))
    time.sleep(0.015 / math.log10(len(score + "**")))
    
    # Creates the "ground" for the player
    # Simulates gravity
    if crate_position_y >= 200:
        crate_position_x = random.randint(0,290)
        crate_position_y = 0
        kandinsky.fill_rect(0,0,320,222,kandinsky.color(255,255,255))
        score += "*"
    
    kandinsky.draw_string(score,0,0)

    # Manages input
    if ion.keydown(ion.KEY_RIGHT):
        player_velocity_x = 4
    if ion.keydown(ion.KEY_LEFT):
        player_velocity_x = -4
    
    # Crate collision and game over system
    crate_distance_x = math.fabs(player_position_x - crate_position_x)
    if crate_distance_x < 30 and crate_position_y > 160 :
        while True :
            kandinsky.draw_string("Game over. Press BACK",0,0)
            print(len(score))

    # Refreshes the player
    kandinsky.fill_rect(player_position_x,player_position_y,30,30,kandinsky.color(255,255,255))
    