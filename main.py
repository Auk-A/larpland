import pygame
import sys
import db

pygame.init()
pygame.font.init()
db.start_connection()
w = 1920
h = 1080
display = pygame.display.set_mode((w, h), pygame.FULLSCREEN)

clock = pygame.time.Clock()


class Text:
    def __init__(self, font):
        self.text = "test"
        self.font = font

    def change_font(self, font):
        self.font = font

    def change_text(self, new_text):
        self.text = new_text

    def render(self, location=None, h_offset=0, v_offset=0):
        text_surface = pygame.font.SysFont(self.font, 80).render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=((w / 2) + h_offset, (h / 2) + v_offset))

        if location is None:
            display.blit(text_surface, dest=text_rect)
        else:
            display.blit(text_surface, dest=location)

    def get_w(self):
        return pygame.font.SysFont(self.font, 80).render(self.text, True, (255, 255, 255)).get_width()


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

    mainText.render(v_offset=200)
    # player.main(display)

    clock.tick(60)
    pygame.display.update()
