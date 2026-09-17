import pygame
import random

pygame.init()

# 화면 설정
WIDTH = 500
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("장애물 피하기")

clock = pygame.time.Clock()

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 100, 255)
RED = (255, 70, 70)

# 플레이어
player = pygame.Rect(225, 600, 50, 50)
player_speed = 7

# 장애물
obstacle = pygame.Rect(
    random.randint(0, WIDTH - 50),
    -50,
    50,
    50
)

obstacle_speed = 10

# 점수
score = 0

# 글꼴
font = pygame.font.SysFont(None, 40)

running = True
game_over = False

while running:

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if not game_over:

        # 캐릭터 이동
        if keys[pygame.K_LEFT]:
            player.x -= player_speed

        if keys[pygame.K_RIGHT]:
            player.x += player_speed

        # 화면 밖으로 나가지 않도록 제한
        if player.left < 0:
            player.left = 0

        if player.right > WIDTH:
            player.right = WIDTH

        # 장애물 이동
        obstacle.y += obstacle_speed

        # 장애물이 화면 아래로 지나갔을 때
        if obstacle.top > HEIGHT:
            obstacle.y = -50
            obstacle.x = random.randint(0, WIDTH - 50)

            score += 1

            # 점수가 올라갈수록 빨라짐
            obstacle_speed += 0.3

        # 충돌 확인
        if player.colliderect(obstacle):
            game_over = True

    # 화면 그리기
    screen.fill(WHITE)

    # 플레이어
    pygame.draw.rect(screen, BLUE, player)

    # 장애물
    pygame.draw.rect(screen, RED, obstacle)

    # 점수
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (20, 20))

    # 게임 오버
    if game_over:
        game_over_text = font.render("GAME OVER", True, RED)
        screen.blit(
            game_over_text,
            (WIDTH // 2 - 100, HEIGHT // 2)
        )

    pygame.display.update()

    clock.tick(60)

pygame.quit()