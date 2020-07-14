import pygame

pygame.init()
screen_width = 480
screen_height = 640

screen = pygame.display.set_mode((screen_width, screen_height))
# 배경이미지 불러오기
background = pygame.image.load("D:/workspace/python/2000_mini_project/pygame_basic/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("D:/workspace/python/2000_mini_project/pygame_basic/character.png")
character_size = character.get_rect().size
character_width     = character_size[0]
character_height    = character_size[1]
character_x = ((screen_width - character_width) / 2)
character_y = (screen_height - character_height)

pygame.display.set_caption("Mado Game")

running = True # 게임 진행중인지 확인
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x, character_y))
    # screen.fill((106, 255, 17))
    pygame.display.update() # 화면 계속 그리기

pygame.quit()