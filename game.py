# Eric Nguyen - wvu9cs
# Kevin Zhao - twq8db
# Final Project - game.py
# 12/07/21 - CS 1110 - Fall Semester 2021

# Comments Included Below, Checkpoints 1 and 2 comments have been modified to include only relevant information

# ------------------------------ CHECKPOINT 1 BELOW ------------------------------ #

'''
Overall description:
This is a two player game.

Five Required Features:
1) User Input
2) Start Screen
3) Game over
4) Small Enough Window
5) Graphics/Images

Four Optional Requirements: (We chose these)
1) Restart from Game Over
2) Sprite Animation
3) Health Bar
4) Two Players Simultaneously
5) Timer (Extra, if time permits)


How we will fulfill these requirements:
The game will start on a homework. (Required Features 2)
Player 1 and Player 2 will each have their own Sprite representation // (Sprite subject to change). (Optional Requirement 2 AND 4)
Player 1 will use W-A-S-D for controls; Player 2 will use the arrow keys. (Required Features 1)
Each player will have their own health bar (in the top corners). (Optional Requirement 3)
A counter will be used to time how the winning message appears. (Optional Requirement 5)
The window will be 800x600 pixels. (Required Features 4)
Graphics / Images will be updated to be very game-friendly. (Required Features 5)
Game Over screen will be prompted when one of the players wins. (Required Features 3)
There will be a "Restart" menu prompted on the Game over Screen. (Optional Requirement 1)

'''
# ------------------ CHECK POINT 2 UPDATES ------ GAME CHANGES --------------------------------------------------------

'''
We are changing our game idea to something similar to Super Smash Bros.
There are two players. Each player has the goal of jumping onto the other player. The player with the most points at the end will win the game. We may decide
to do a version of Best of 3 Matches, or something very similar to this.

We are adding floating platforms to make the game more interesting and giving players vantage points to jump from.

Please contact us if there are any issues and we will address them:
Eric Nguyen: wvu9cs@virginia.edu
Kevin Zhao: twq8db@virginia.edu

'''

# ------------------ FINAL SUBMISSION UPDATES ------ GAME CHANGES -----------------------------------------------------

'''
The final version of the game is very similar to Super Smash Bros.
Player 1 is on the Left (W-A-S-D Controls). Player 2 is on the right (Arrow Key Controls).
Each players' objective is to defeat (jump directly on top [bottom_touches()]) the other player. Each player has 5 healthpoints per round, and the game
operates by best of 3 rounds. Once a player loses 5 healthpoints (or falls of the map), the round ends and the other player wins that round.
Once the game ends, a Game Over screen will display with the option to Restart (press r) and the winner of the game.

Five Required Features:
1) User Input (Player 1's Controls: WASD // Player 2's Controls: Arrow Keys)
2) Start Screen ("Welcome To Smash Press Space to Start")
3) Game Over Screen ("Game Over Press R to Restart Player 1/2 Wins")
4) Small Enough Window (The window is 800x600)
5) Graphics/Images (Appropriate)

Four Optional Requirements: (We did extra; some of these apply to other optional categories as well.)
1) Restart from Game Over (On the Game Over Screen, you can press 'r' on the keyboard to restart the game)
2) Sprite Animation (There are 4 Sprite Animations total -- Player 1 (Yellow Character), Player 2 (Gray Character), 
                                                            Player 1's Healthbar (Top left corner), Player 2's Healthbar (Top right corner)
3) Health Bar (There is a health bar for EACH character. The health bar changes to reflect how much health (5 lives) each character has left before they lose the round.
4) Two Players Simultaneously (There is Player 1 (Yellow guy on the left) and Player 2 (Gray guy on the right))
5) Timer (There is a timer at the end of each round to display the winner message ("Player 1/2 wins") and to prevent the players from moving until the next round)

'''

# ---------------------------------------------------------------------------------------------------------------------


# -------------------------------------------- CODE BELOW -------------------------------------------------------------

import gamebox
import pygame

# Screen size
camera = gamebox.Camera(800, 600)

# Define the two players in sprites
fan_sprite = gamebox.load_sprite_sheet('Player1_Image.png', 1, 6)
p1 = gamebox.from_image(265, 475, fan_sprite[-1])
p1.scale_by(.55)
fan_sprite2 = gamebox.load_sprite_sheet('Player2_Image.png', 1, 6)
p2 = gamebox.from_image(530, 475, fan_sprite2[-1])
p2.scale_by(.55)

# Player 1's full heatlh bar (5)
health_sprite1_full = gamebox.load_sprite_sheet("HealthBar2.png", 6, 1)
h1_full = gamebox.from_image(75, 35, health_sprite1_full[5])
h1_full.scale_by(0.15)
# Player 1's high health bar (4)
health_sprite1_high = gamebox.load_sprite_sheet("HealthBar2.png", 6, 1)
h1_high = gamebox.from_image(75, 35, health_sprite1_high[3])
h1_high.scale_by(0.15)
# Player 1's mid health bar (3)
health_sprite1_mid = gamebox.load_sprite_sheet("HealthBar2.png", 6, 1)
h1_mid = gamebox.from_image(75, 35, health_sprite1_mid[2])
h1_mid.scale_by(0.15)
# Player 1's less health bar (2)
health_sprite1_less = gamebox.load_sprite_sheet("HealthBar2.png", 6, 1)
h1_less = gamebox.from_image(75, 35, health_sprite1_less[1])
h1_less.scale_by(0.15)
# Player 1's low health bar (1)
health_sprite1_low = gamebox.load_sprite_sheet("HealthBar2.png", 6, 1)
h1_low = gamebox.from_image(75, 35, health_sprite1_low[0])
h1_low.scale_by(0.15)

# Player 2's full health bar (5)
health_sprite2_full = gamebox.load_sprite_sheet("HealthBar2.png", 6, 1)
h2_full = gamebox.from_image(725, 35, health_sprite2_full[5])
h2_full.scale_by(0.15)
# Player 2's high health bar (4)
health_sprite2_high = gamebox.load_sprite_sheet("HealthBar2.png", 6, 1)
h2_high = gamebox.from_image(725, 35, health_sprite2_high[3])
h2_high.scale_by(0.15)
# Player 2's mid health bar (3)
health_sprite2_mid = gamebox.load_sprite_sheet("HealthBar2.png", 6, 1)
h2_mid = gamebox.from_image(725, 35, health_sprite2_mid[2])
h2_mid.scale_by(0.15)
# Player 2's full health bar (2)
health_sprite2_less = gamebox.load_sprite_sheet("HealthBar2.png", 6, 1)
h2_less = gamebox.from_image(725, 35, health_sprite2_less[1])
h2_less.scale_by(0.15)
# Player 2's low health bar (1)
health_sprite2_low = gamebox.load_sprite_sheet("HealthBar2.png", 6, 1)
h2_low = gamebox.from_image(725, 35, health_sprite2_low[0])
h2_low.scale_by(0.15)

# Floor and platforms
floor = gamebox.from_color(400, 550, "black", 600, 30)
plat1 = gamebox.from_color(125, 300, "black", 150, 15)
plat2 = gamebox.from_color(400, 175, "black", 150, 15)
plat3 = gamebox.from_color(675, 300, "black", 150, 15)
plat4 = gamebox.from_color(400, 375, "black", 150, 15)

# Score
score = ""

# health_counter1 for how many lives Player 1 has left
health_counter1 = 5

# health_counter2 for how many lives Player 2 has left
health_counter2 = 5

# Gameover boolean
gameover = False

# Game Begin boolean
game_on = False

# counter for create_counter
counter = 0

# text for create_counter
text = ""

# Do we need this? I don't think so. Remove if not necessary
begin = 0

# num for create_counter
num = 4

# List of Platforms
platforms = [floor, plat1, plat2, plat3, plat4]

# round counter for best of three rounds
round_counter = 0

# win counters
p1_win_counter = 0
p2_win_counter = 0

# Boolean for if the round is over
counter_round_over = False

# The recent winner is store in this
recent_winner = ""


# Player 1's moving
p1_move = False


# Player 1's current frame image
current_frame1 = 0


# Player 1 Walking Right
walk_right1 = True

# Player 2's moving
p2_move = False


# Player 2's current frame image
current_frame2 = 0


# Player 2 Walking Right
walk_right2 = True




def check_start_screen(keys):
    '''
    This function checks if the space bar has been pressed.
    This controls when the start screen is dismissed.
    :param keys: This parameter is used to work with the Tick function
    :return: No return, changes the game_on variable to true.
    '''
    global game_on
    if pygame.K_SPACE in keys:
        game_on = True


def clear_counter():
    '''
    This function resets all of the listed global variables to their default values once the round has ended
    and the counter needs to be restarted
    :return: No return
    '''
    global counter_round_over
    global num
    global text
    global recent_winner
    counter_round_over = False
    num = 4
    text = ""
    recent_winner = ""
    p1.x = 265
    p1.y = 475
    p2.x = 530
    p2.y = 475



def check_round_over():
    '''
    This function checks if the round is over when either one of the characters' health reaches 0. Then, it will increment
    the winner's count and set counter_round_over as True to begin the counter.
    :return: No return
    '''
    global round_counter
    global game_on
    global p1_win_counter
    global p2_win_counter
    global health_counter1
    global health_counter2
    global counter_round_over
    global recent_winner

    if health_counter1 == 0:
        p2_win_counter += 1
        counter_round_over = True
        recent_winner = "p2"
    if health_counter2 == 0:
        p1_win_counter += 1
        counter_round_over = True
        recent_winner = "p1"


def check_game_over():
    '''
    This function checks if the game is over if there have been 3 rounds. If it is over, it'll set gameover as True
    :return: No return
    '''
    global round_counter
    global game_on
    global gameover
    if round_counter == 3:
        gameover = True


def clear_game():
    '''
    This function resets all the listed global variables to their initial values to reset the game
    :return: No return
    '''
    global round_counter
    global game_on
    global p1_win_counter
    global p2_win_counter
    global health_counter1
    global health_counter2
    global counter
    global score
    global gameover
    global text
    global num
    global counter

    score = ""
    health_counter1 = 5
    health_counter2 = 5
    counter = 0
    text = ""
    num = 4
    round_counter = 0
    p1_win_counter = 0
    p2_win_counter = 0
    p1.x = 265
    p1.y = 475
    p2.x = 530
    p2.y = 475


def getScore():
    '''
    This function tells us who the winner is.
    :return: When it is returned, it will draw on the screen Player 1/2 Wins
    '''
    global p1_win_counter
    global p2_win_counter

    p1 = p1_win_counter
    p2 = p2_win_counter

    if p1 < p2:
        return camera.draw(gamebox.from_text(400, 400, "Player 2 Wins", 100, "Red", bold=True))
    else:
        return camera.draw(gamebox.from_text(400, 400, "Player 1 Wins", 100, "Red", bold=True))


# FUNCTIONS move_p2(keys) and move_p1(keys) were written based on the Class Lecture on November 8th from the powerpoint.
def move_p2(keys):
    '''
    This function moves Player 2 and animates the sprite movement
    :param keys: Default parameter for tick
    :return: No return
    '''
    global p2_move
    global current_frame2
    global walk_right2
    p2_move = False
    if pygame.K_RIGHT in keys:
        if p2.x + 30 > 800:
            p2.x = 800
            p2_move = True
        else:
            if not walk_right2:
                p2.flip()
                walk_right2 = True
            p2.x += 15
            p2_move = True
    if pygame.K_LEFT in keys:
        if p2.x - 30 < 0:
            p2.x = 0
            p2_move = True
        else:
            if walk_right2:
                p2.flip()
                walk_right2 = False
            p2.x -= 15
            p2_move = True
    if pygame.K_UP in keys and (
            p2.bottom_touches(floor) or p2.bottom_touches(plat1) or p2.bottom_touches(
        plat2) or p2.bottom_touches(
        plat3) or p2.bottom_touches(plat4)):
        if p2.y - 200 < 0:
            p2.y = 0
            p2_move = True
        else:
            p2.y -= 150
            p2_move = True

    if p2_move:
        current_frame2 += 1
        if current_frame2 >= 4:
            current_frame2 = 0
        p2.image = fan_sprite2[current_frame2]
    else:
        p2.image = fan_sprite2[-1]


def move_p1(keys):
    '''
    This function moves Player 1 and animates the sprite movement
    :param keys: Default parameter for tick
    :return: No return
    '''
    global p1_move
    global current_frame1
    global walk_right1
    p1_move = False
    if pygame.K_d in keys:
        if p1.x + 30 > 800:
            p1.x = 800
            p1_move = True
        else:
            if not walk_right1:
                p1.flip()
                walk_right1 = True
            p1.x += 15
            p1_move = True
    if pygame.K_a in keys:
        if p1.x - 30 < 0:
            p1.x = 0
            p1_move = True
        else:
            if walk_right1:
                p1.flip()
                walk_right1 = False
            p1.x -= 15
            p1_move = True
    if pygame.K_w in keys and (
            p1.bottom_touches(floor) or p1.bottom_touches(plat1) or p1.bottom_touches(
        plat2) or p1.bottom_touches(
        plat3) or p1.bottom_touches(plat4)):
        if p1.y - 200 < 0:
            p1.y = 0
            p1_move = True
        else:
            p1.y -= 150
            p1_move = True

    if p1_move:
        current_frame1 += 1
        if current_frame1 >= 4:
            current_frame1 = 0
        p1.image = fan_sprite[current_frame1]
    else:
        p1.image = fan_sprite[-1]


# ------------------------------------------------------ #
# ------------------------ TICK ------------------------ #
# ------------------------------------------------------ #


def tick(keys):
    '''
    This is where the game actions take place.
    :param keys: This parameter is used to work with gamebox.time_loop()
    :return: No return
    '''

    # Global Variables to be used
    global game_on
    global platforms
    global health_counter1
    global health_counter2
    global round_counter
    global counter
    global text
    global gameover
    global p2_win_counter
    global p1_win_counter
    global num
    global counter_round_over
    global recent_winner

    # Set the background as white
    camera.clear('Tan')


    # Start menu text before the Space Bar is pressed
    if game_on == False:
        camera.draw(gamebox.from_text(400, 250, "Welcome to Smash", 100, "Red", bold=True))
        camera.draw(gamebox.from_text(400, 315, "Press Space to Start", 50, "Red", bold=False))
    # The Game Over menu
    if gameover:
        camera.draw(gamebox.from_text(400, 250, "Game Over", 100, "Red", bold=True))
        camera.draw(gamebox.from_text(400, 315, "Press r to Restart", 50, "Red", bold=False))


        # Get the score
        getScore()


        # Press R to restart the game
        if pygame.K_r in keys:
            gameover = False
            game_on = True
            clear_game()
            clear_counter()
        keys.clear()


    # Calling the function to see if the space bar has been pressed
    check_start_screen(keys)
    if num < 1:
        clear_counter()
        print("num" + str(counter_round_over))
    check_game_over()


    # Don't let Player 1 go through/touch the platforms
    for wall in platforms:
        if p1.move_to_stop_overlapping(wall):
            p1.y = wall.y - 25
            p1.speedy = 0.9


    # Don't let Player 2 go through/touch the platforms
    for wall in platforms:
        if p2.move_to_stop_overlapping(wall):
            p2.y = wall.y - 25
            p2.speedy = 0.9


    # Begin the game once the space bar is pressed
    if game_on and gameover == False:


        # Draw the Sprite Characters
        camera.draw(p1)
        camera.draw(p2)


        # Draw the Sprite Health Bar for Player 1
        if health_counter1 == 5:
            camera.draw(h1_full)
        elif health_counter1 == 4:
            camera.draw(h1_high)
        elif health_counter1 == 3:
            camera.draw(h1_mid)
        elif health_counter1 == 2:
            camera.draw(h1_less)
        elif health_counter1 == 1:
            camera.draw(h1_low)


        # Draw the Sprite Health Bar for Player 2
        if health_counter2 == 5:
            camera.draw(h2_full)
        elif health_counter2 == 4:
            camera.draw(h2_high)
        elif health_counter2 == 3:
            camera.draw(h2_mid)
        elif health_counter2 == 2:
            camera.draw(h2_less)
        elif health_counter2 == 1:
            camera.draw(h2_low)


        # Draw Platforms/Floor
        camera.draw(floor)
        camera.draw(plat1)
        camera.draw(plat2)
        camera.draw(plat3)
        camera.draw(plat4)


        # If Player 1's bottom touches Player 2's head
        # Update the health bar
        # increase a counter
        if p1.bottom_touches(p2):
            health_counter2 -= 1
            p1.x = 265
            p1.y = 475


        # If Player 2's bottom touches Player 2's head
        # Update the health bar
        # increase a counter
        if p2.bottom_touches(p1):
            health_counter1 -= 1
            p2.x = 530
            p2.y = 475


        # If Player 1 falls of the map, make the health go to 0
        # and respawn them on the platform for the next round
        if p1.y > 600:
            health_counter1 = 0
            p1.x = 265
            p1.y = 475


        # If Player 2 falls of the map, make the health go to 0
        # and respawn them on the platform for the next round
        if p2.y > 600:
            health_counter2 = 0
            p2.x = 530
            p2.y = 475


        # Check to see if the round is over
        check_round_over()


        # If the round is over, draw the winner
        if counter_round_over == True:
            if recent_winner == "p2":
                camera.draw(gamebox.from_text(400, 250, "Player 2 wins", 100, "Red", bold=True))
            if recent_winner == "p1":
                camera.draw(gamebox.from_text(400, 250, "Player 1 wins", 100, "Red", bold=True))


        # Reset health bar
        if health_counter1 == 0 or health_counter2 == 0:
            health_counter1 = 5
            health_counter2 = 5
            round_counter += 1


        # Counter for how many seconds passes, Will also be drawn in the bottom left corner
        counter += 1
        if counter_round_over:
            if counter % 30 == 0:
                num -= 1
                text = "Round " + str(round_counter + 1) + " starts in " + str(num)
            camera.draw(text, 50, "red", 400, 315)


        # Stop the players from moving when the round is over
        if counter_round_over == False:
            # Move the players and animate sprites
            move_p1(keys)
            move_p2(keys)


        # Characters are falling at an accelerating pace
        gravity = 0.75


        # This is increasing in acceleration
        p1.speedy += gravity
        if (p1.y + p1.speedy) >= 875:  # This is making sure it doesn't fall through the floor
            p1.y = 875
        else:
            p1.y += p1.yspeed


        # This is increasing in acceleration
        p2.speedy += gravity
        if (p2.y + p2.speedy) >= 875:  # This is making sure it doesn't fall through the floor
            p2.y = 875
        else:
            p2.y += p2.yspeed


    # Keep this line here
    camera.display()


# 30 Frames per second - Keep this as the last line
gamebox.timer_loop(30, tick)