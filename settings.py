import pygame
import sys

# Khởi tạo pygame
pygame.init()

# Thiết lập màn hình
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Ví dụ ô cược")

# Tạo hai ô cược
option1_rect = pygame.Rect(100, 100, 50, 50)
option2_rect = pygame.Rect(200, 100, 50, 50)

font = pygame.font.Font(None, 20)
font2 = pygame.font.Font(None, 20)

text1 = font.render("TAI", True, (255,255,255))
text2 = font2.render("XIU", True, (255,255,255))

# Vòng lặp chính
running = True
while running:
    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Kiểm tra nếu chuột click vào ô cược 1
            if option1_rect.collidepoint(event.pos):
                print("Bắt đầu trò chơi 1")
            # Kiểm tra nếu chuột click vào ô cược 2
            elif option2_rect.collidepoint(event.pos):
                print("Bắt đầu trò chơi 2")

    # Vẽ các phần tử lên màn hình
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 255, 0), option1_rect)
    pygame.draw.rect(screen, (255, 0, 0), option2_rect)
    screen.blit(text1, (100, 100))
    screen.blit(text2, (200, 100))

    pygame.display.flip()

# Kết thúc chương trình
pygame.quit()
sys.exit()
