import pygame

pygame.init()
screen_width = 480
screen_height = 640
FPS_SPEED   = 60

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
CHAR_SPEED       = 0.5
# TARG_SPEED  = 300
# SPEED = TARG_SPEED / FPS_SPEED


# 캐릭터(스프라이트) 불러오기
enemy = pygame.image.load("D:/workspace/python/2000_mini_project/pygame_basic/enemy.png")
enemy_size = character.get_rect().size
enemy_width     = enemy_size[0]
enemy_height    = enemy_size[1]
enemy_x = (screen_width - enemy_width) / 2
enemy_y = (screen_height - enemy_height) / 2

enemy_to_x = 0
enemy_to_y = 0
ENEM_SPEED = 0.2

# 폰트 정의
game_font = pygame.font.Font(None, 40)
total_time = 10

start_ticks = pygame.time.get_ticks()

running = True # 게임 진행중인지 확인
while running:
    dt = clock.tick(FPS_SPEED) # 초당 프레임 수
    # print(f"fps : {str(clock.get_fps())}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                to_x += CHAR_SPEED
            elif event.key == pygame.K_LEFT:
                to_x -= CHAR_SPEED
            elif event.key == pygame.K_UP:
                to_y -= CHAR_SPEED
            elif event.key == pygame.K_DOWN:
                to_y += CHAR_SPEED
            
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
    
        
    
    if character_y + to_y < 0:
        character_y = 0
    elif character_y + to_y > screen_height - character_height:
        character_y = screen_height - character_height
    
    character_rect = character.get_rect()
    character_rect.left = character_x
    character_rect.top  = character_y

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x
    enemy_rect.top  = enemy_y
    
    # rect 간의 간섭 여부 확인 가능한 함수가 존재함!
    if character_rect.colliderect(enemy_rect):
        print("충돌!! 충돌!!")
        running = False

    character_y += to_y
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x, character_y))
    screen.blit(enemy, (enemy_x, enemy_y))
    
    # 타이머 삽입.
    elapsed_times = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(str(int(total_time - elapsed_times)), True, (255, 255, 255))
    if total_time - elapsed_times < 0:
        print("타임아웃!! 타임아웃!!")
        pygame.time.delay(2000)
        running = False
    screen.blit(timer, (10, 10))

    # screen.fill((106, 255, 17))
    pygame.display.update() # 화면 계속 그리기

pygame.quit()