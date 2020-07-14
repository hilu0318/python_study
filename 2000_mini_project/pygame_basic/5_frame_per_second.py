import pygame

pygame.init()
screen_width = 480
screen_height = 640

pygame.display.set_caption("Mado Game")

clock = pygame.time.Clock()

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

to_x = 0
to_y = 0
FPS_SPEED   = 60
SPEED       = 0.5
# TARG_SPEED  = 300
# SPEED = TARG_SPEED / FPS_SPEED




running = True # 게임 진행중인지 확인
while running:
    dt = clock.tick(FPS_SPEED) # 초당 프레임 수
    # print(f"fps : {str(clock.get_fps())}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                to_x += SPEED
            elif event.key == pygame.K_LEFT:
                to_x -= SPEED
            elif event.key == pygame.K_UP:
                to_y -= SPEED
            elif event.key == pygame.K_DOWN:
                to_y += SPEED
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    character_x += to_x * dt
    character_y += to_y * dt
    
    if character_x + to_x < 0:
        character_x = 0
    elif character_x + to_x > screen_width - character_width:
        character_x = screen_width - character_width
    # else:
        
    
    if character_y + to_y < 0:
        character_y = 0
    elif character_y + to_y > screen_height - character_height:
        character_y = screen_height - character_height
    # else:
        

    character_y += to_y
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x, character_y))
    # screen.fill((106, 255, 17))
    pygame.display.update() # 화면 계속 그리기

pygame.quit()