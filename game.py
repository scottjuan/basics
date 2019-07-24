import pygame

pygame.init()
screen_info = pygame.display.Info()

size = (width, height) = (800, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (150, 127, 0)

fish = pygame.image.load("fish.png")
image_rect = fish.get_rect()
speed = pygame.math.Vector2(20, 20)


def main():
    while True:
        clock.tick(60)
        move()
        screen.fill(color)
        screen.blit(fish, image_rect)
        pygame.display.flip()


def move():
    image_rect.move_ip(speed)
    if image_rect.right > width:
        speed.x *= -1
    if image_rect.left < 0:
        speed.x *= -1
    if image_rect.bottom > height:
        speed.y *= -1
    if image_rect.top < 0:
        speed.y *= -1


if __name__ == "__main__":
    main()
