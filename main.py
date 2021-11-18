import pygame
import sys
import db

pygame.init()
pygame.font.init()
db.start_connection()

display = pygame.display.set_mode((800, 600), pygame.FULLSCREEN)
clock = pygame.time.Clock()


class Text:
    def __init__(self, font):
        self.text = ""
        self.font = font

    def change_font(self, font):
        self.font = font

    def change_text(self, new_text):
        self.text = new_text

    def render(self, location):
        text_surface = pygame.font.SysFont(self.font, 30).render(self.text, True, (255, 255, 255))
        display.blit(text_surface, dest=location)


class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def main(self, display_area):
        pygame.draw.rect(display_area, (255, 0, 0), (self.x, self.y, self.width, self.height))


# player = Player(400, 300, 32, 32)
mainText = Text("Calibri")


while True:
    display.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    mainText.render((100, 100))
    # player.main(display)

    clock.tick(60)
    pygame.display.update()
