#Start :

#Libary:============================================================================

from asyncio import Barrier
from logging import root
from venv import create
import pygame
import sys
import random

#PYgame:============================================================================

pygame.init()

#Variables:============================================================================

root1 = pygame.display.set_mode((620, 370))
root_clock = pygame.time.Clock()
root_floor_number = 0
gravity = 0.1
main_c_movement = 0
Barrier_list = []
game_status = True

#def:============================================================================


def Barrier_rect1 () :
    random_Barrier1 = random.randrange(30, 280)
    Barrier_rect1 = root_Barrier1.get_rect(midtop = (700, int(random_Barrier1)))
    return Barrier_rect1

def Barrier_move1 (Barrier_list) :
    for Barrier in Barrier_list :
        Barrier.centerx -= int(5)
    inside_Barrier = [Barrier for Barrier in Barrier_list if Barrier.right >-40]
    return inside_Barrier

def display_Barrier1 (Barrier_list) :
    for Barrier in Barrier_list :
        root1.blit(root_Barrier1,(Barrier))

def check_collision1 (Barrier_list) :
    for Barrier in Barrier_list :
        if main_c_rectangle.colliderect(Barrier) :
            return False
        if main_c_rectangle.top <= -30 or main_c_rectangle.bottom >= 320 :
            return False
    return True


#Roots:============================================================================

root_background = pygame.image.load("image/background.png")  
root_floor = pygame.image.load("image/floor1.png")
root_Barrier1 = pygame.image.load("image/C1.png")
root_main_c = pygame.image.load("image/main_c1.png")

create_Barrier = pygame.USEREVENT
pygame.time.set_timer(create_Barrier, 1300)

#Rectangle of Shape:============================================================================

main_c_rectangle = root_main_c.get_rect(center=(100, 200))

#WhileTrue:============================================================================

while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE :
                main_c_movement = 0
                main_c_movement -= 4  
            if event.key == pygame.K_r and game_status == False :
                game_status = True
                Barrier_list.clear()
                main_c_movement += gravity
                main_c_rectangle.center = (100, 190)
                main_c_rectangle.centery += int(main_c_movement)
        if event.type == create_Barrier :
            Barrier_list.append(Barrier_rect1())
    Barrier_move1(Barrier_list)
    root1.blit(root_background, (0, 0))
    if game_status :
        game_status = check_collision1(Barrier_list)

#Roots_blit:============================================================================

        root_floor_number -= 1
        root1.blit(root_floor, (root_floor_number, 328))
        root1.blit(root_floor, (root_floor_number + 576, 328))
        root1.blit(root_main_c , main_c_rectangle)
        Barrier_list = Barrier_move1 (Barrier_list)
        display_Barrier1 (Barrier_list)
        check_collision1 (Barrier_list)

#Roots_blit:============================================================================

        main_c_movement += gravity
        main_c_rectangle.centery += int(main_c_movement)

#Display_Floor:============================================================================

        if root_floor_number <= -576 :
            root_floor_number = 0

#display:============================================================================

    pygame.display.update()
    root_clock.tick(90)

#End