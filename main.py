import pygame
import sys
import db

pygame.init()
pygame.font.init()
db.initialize_db()

w = 1920
h = 1080
display = pygame.display.set_mode((w, h), pygame.FULLSCREEN)
clock = pygame.time.Clock()

# Fonts
default_font = "./assets/fonts/DeutscheZierschrift.ttf"


class Text:
    def __init__(self, font, text="", action=None):
        self.font = font
        self.text = text
        self.functionality = action
        self.color = (255, 255, 255)

    def change_font(self, font):
        self.font = font

    def change_text(self, new_text):
        self.text = new_text

    def render(self, location=None, h_offset=0, v_offset=0, size=50):
        text_surface = pygame.font.Font(self.font, size).render(self.text, True, self.color)
        text_rect = text_surface.get_rect(center=((w / 2) + h_offset, (h / 2) + v_offset))

        if location is None:
            display.blit(text_surface, dest=text_rect)
        else:
            display.blit(text_surface, dest=location)

    def get_w(self):
        return pygame.font.SysFont(self.font, 120).render(self.text, True, (255, 255, 255)).get_width()

    def do_action(self):
        if self.functionality == "exit":
            sys.exit()


# Items and weapons
class Item:
    def __init__(self, name):
        self.name = name
        self.coin_value = None


class Weapon(Item):
    def __init__(self, name, speed):
        super().__init__(name)
        self.speed = speed
        self.damage = 10


class Bow(Weapon):
    def __init__(self, name, speed):
        super().__init__(name, speed)
        self.range = 50


class Sword(Weapon):
    def __init__(self, name, speed):
        super().__init__(name, speed)
        self.range = 10


# Player
class Player:
    def __init__(self):
        self.items = []


class Menu:
    def __init__(self, vertical_offset, font_size, text_header, *menu_items):
        self.text_header = text_header
        self.vertical_offset = vertical_offset
        self.font_size = font_size
        self.list_menu_items = []
        for menu_item in menu_items:
            self.list_menu_items.append(menu_item)
        self.current_round = - 1

    def render(self):
        v_offset = self.vertical_offset
        self.text_header.render(v_offset=v_offset - 160, size=round(self.font_size * 1.8))
        for list_menu_item in self.list_menu_items:
            list_menu_item.render(v_offset=v_offset, size=self.font_size)
            v_offset += 120

    def cycle(self, direction):
        total_rounds = len(self.list_menu_items) - 1
        last_round = self.current_round

        if direction == "down":
            if self.current_round != total_rounds:
                self.current_round += 1
            else:
                self.current_round = 0
        if direction == "up":
            if self.current_round != 0:
                self.current_round -= 1
            else:
                self.current_round = total_rounds

        self.list_menu_items[last_round].color = "white"
        self.list_menu_items[self.current_round].color = "red"


# player = Player(400, 300, 32, 32)
mainMenu = Menu(-90, 60,
                Text(default_font, "Larpland"),
                Text(default_font, "Start"),
                Text(default_font, "Instellingen", "settings"),
                Text(default_font, "Uitgang", "exit"))

tabIndex = 0

db.get_random_weapon()

menu = True
while True:
    display.fill((0, 0, 0))

    if menu:
        mainMenu.render()

    for event in pygame.event.get():

        pressed = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if pressed[pygame.K_TAB] or pressed[pygame.K_DOWN]:
                if menu:
                    mainMenu.cycle("down")
            elif pressed[pygame.K_UP]:
                if menu:
                    mainMenu.cycle("up")
            elif pressed[pygame.K_SPACE]:
                if menu:
                    mainMenu.list_menu_items[mainMenu.current_round].do_action()

    vertical = -100

    clock.tick(60)
    pygame.display.update()
