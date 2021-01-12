import pygame

def Move_snake(screen,color,snake_posation_x,snake_posation_y,len):
    pygame.draw.rect(screen,color,[snake_posation_x,snake_posation_y,len,7])

