import pygame
from gui import main_menu
from constants import *
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Connect 4")

main_menu(screen) 