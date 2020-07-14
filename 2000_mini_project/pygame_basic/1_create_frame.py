import pygame

pygame.init()
screen_width = 480
screen_height = 640

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Mado Game")

running = True # 게임 진행중인지 확인
while running:
    for event in pygame.event.get():
        print(event.type)
        if event.type == pygame.QUIT:
            print(event.type)
            running = False
pygame.quit()