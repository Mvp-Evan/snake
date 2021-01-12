import pygame
import random
import food
import snake
pygame.init()

# prepare the first value for posaton and direction
food_posation_x = random.randint(11, 501)
food_posation_y = random.randint(11, 501)
snake_posation_x = 256
snake_posation_y = 256
snake_direction = 1
snake_len = 15
left = 1
right = 0
up = 2
down = 3
# Set the height and width of the screen
size = [512, 512]
screen = pygame.display.set_mode(size)

#prepare the colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
speed = 10
while done == False:

    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(speed)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN: # import the key board to control
            if event.key == pygame.K_UP:
                if snake_direction != 3:
                    snake_direction = up
            elif event.key == pygame.K_LEFT:
                if snake_direction != 0:
                    snake_direction = left
            elif event.key == pygame.K_RIGHT:
                if snake_direction != 1:
                    snake_direction = right
            elif event.key == pygame.K_DOWN:
                if snake_direction != 2:
                    snake_direction = down

    # Clear the screen and set the screen background
    screen.fill(black)
    pygame.draw.rect(screen,white,[10,10,492,492])

 #### make snake to move #############################################################################################
    snake.Move_snake(screen,blue,snake_posation_x,snake_posation_y,snake_len)
    if snake_direction == left:
        snake_posation_x -= 5
        if snake_posation_x <= 10:
            snake_posation_x = 10
    elif snake_direction == up:                   # left = 1 ; right = 0 ; up = 2 ; down = 3
        snake_posation_y -= 5
        if snake_posation_y <= 10:
            snake_posation_y = 10
    elif snake_direction == right:
        snake_posation_x += 5
        if snake_posation_x >= 502-snake_len:
            snake_posation_x = 502-snake_len
    elif snake_direction == down:
        snake_posation_y += 5
        if snake_posation_y >= 502-7:
            snake_posation_y = 502-7

 ######################################################################################################################

    #make food to move
    food.Move_food(screen, red, food_posation_x, food_posation_y)
    if food_posation_x >= snake_posation_x and food_posation_x <= snake_posation_x + snake_len and food_posation_y >= snake_posation_y and food_posation_y <= snake_posation_y + 7:
        food_posation_x = random.randint(11, 501)
        food_posation_y = random.randint(11, 501)
        snake_len += 10
        speed += 2
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

# Tidy up
pygame.quit()