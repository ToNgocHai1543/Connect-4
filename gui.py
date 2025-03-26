import pygame
import sys
import threading
from constants import *
from offline_mode.two_player import *
from offline_mode.ai_player import play_with_ai
from online_mode.server import *
import os

# IMG_DIR = os.path.join(os.path.dirname("C:\\UET\\2nd_Semeter_2\\AI\\Connect-4\\img\\back_ground.jpg"), "img")

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main_menu(screen):

    # background = pygame.image.load(os.path.join(IMG_DIR, "background.png"))
    # screen.blit(background, (0, 0))
    
    font = pygame.font.SysFont(FONT_NAME, 40)
    while True:
        screen.fill(WHITE)
        draw_text("Connect 4", font, BLACK, screen, WIDTH // 2 - 100, 100)

        mx, my = pygame.mouse.get_pos()

        button_offline = pygame.Rect(WIDTH // 2 - 150, 200, 300, 50)
        pygame.draw.rect(screen, BLUE, button_offline)
        draw_text("Play Offline", font, WHITE, screen, WIDTH // 2 - 150, 210)

        button_online = pygame.Rect(WIDTH // 2 - 150, 300, 300, 50)
        pygame.draw.rect(screen, BLUE, button_online)
        draw_text("Play Online", font, WHITE, screen, WIDTH // 2 - 150, 310)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_offline.collidepoint((mx, my)):
                    offline_menu(screen)  
                if button_online.collidepoint((mx, my)):
                    online_menu(screen) 

        pygame.display.update()

def offline_menu(screen): 
    font = pygame.font.SysFont(FONT_NAME, 40) 
    while True:
        screen.fill(WHITE)
        draw_text("Offline Mode", font, BLACK, screen, WIDTH // 2 - 120, 100)

        mx, my = pygame.mouse.get_pos()

        button_ai = pygame.Rect(WIDTH // 2 - 100, 200, 300, 50)
        pygame.draw.rect(screen, BLUE, button_ai)
        draw_text("With AI", font, WHITE, screen, WIDTH // 2 - 80, 210)

        button_2p = pygame.Rect(WIDTH // 2 - 100, 300, 300, 50)
        pygame.draw.rect(screen, BLUE, button_2p)
        draw_text("2 People", font, WHITE, screen, WIDTH // 2 - 80, 310)

        button_back = pygame.Rect(WIDTH // 2 - 300, 500, 200, 50)
        pygame.draw.rect(screen, RED, button_back)
        draw_text("Back", font, BLUE, screen, WIDTH // 2 - 250, 500)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_ai.collidepoint((mx, my)):
                    play_with_ai()
                if button_2p.collidepoint((mx, my)):
                    play_2p()
                if button_back.collidepoint((mx, my)):
                    main_menu(screen)  

        pygame.display.update()

def online_menu(screen):
    font = pygame.font.SysFont(FONT_NAME, 40)
    server_instance = None

    while True:
        screen.fill(WHITE)
        draw_text("Online Mode", font, BLACK, screen, WIDTH // 2 - 120, 100)

        mx, my = pygame.mouse.get_pos()

        button_server = pygame.Rect(WIDTH//2-100, 200, 300, 50)
        pygame.draw.rect(screen, GREEN if server_instance is None else RED, button_server)
        draw_text("Start Server" if server_instance is None else "Stop Server", 
                 font, WHITE, screen, WIDTH//2-80, 210)
        
        button_back = pygame.Rect(WIDTH // 2 - 300, 500, 200, 50)
        pygame.draw.rect(screen, RED, button_back)
        draw_text("Back", font, BLUE, screen, WIDTH // 2 - 250, 500)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if server_instance:
                    server_instance.cleanup()
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_server.collidepoint((mx, my)):
                    if server_instance is None:
                        # server_instance = Connect4Server(screen)
                        # threading.Thread(
                        #     target=server_instance.run,
                        #     daemon=True
                        # ).start()
                        threading.Thread(
                            target=init_server(screen),
                            daemon=True
                        ).start()
                    else:
                        # server_instance.cleanup()
                        server_instance = None
                        
                if button_back.collidepoint((mx, my)):
                    if server_instance:
                        server_instance.cleanup()
                    return

        pygame.display.update()


