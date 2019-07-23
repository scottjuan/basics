import pygame

pygame.init()
screen_info = pygame.display.Info()

size = (width, height) = (800, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (0, 127, 255)

fish = pygame.image.load("fish.png")
image_rect = fish.get_rect()
speed = pygame.math.Vector2(65, 53)


def main():
    while True:
        clock.tick(60)
        move()
        screen.fill(color)
        screen.blit(fish, image_rect)
        pygame.display.flip()


def move():
    image_rect.move_ip(speed)
    width = screen_info.current_w
    if image_rect.right > width:
        speed.x *= -1
    if image_rect.left< 0:
        speed.x*=-1
    if image_rect.top< -height:
        speed.y*= -1
if __name__ == "main":
    main()
