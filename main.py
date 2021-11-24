from dataclasses import dataclass

import pygame
import sys
import db
import time

pygame.init()
pygame.font.init()
db.initialize_db()

w = 1920
h = 1080
display = pygame.display.set_mode((w, h), pygame.FULLSCREEN)
clock = pygame.time.Clock()

# Fonts
menu_font = "./assets/fonts/DeutscheZierschrift.ttf"
default_font = "./assets/fonts/Augusta.ttf"


class Text:
    def __init__(self, font, text="", action=None, visibility=True):
        self.font = font
        self.text = text
        self.functionality = action
        self.color = (255, 255, 255)
        self.visibility = visibility

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

    # Tekst functionaliteit
    def do_action(self):
        if self.functionality == "exit_main":
            sys.exit()
        elif self.functionality == "enter_main":
            mainMenu.visibility = False
            default_text_box.visibility = True
        elif self.functionality == "settings_main":
            mainMenu.visibility = False
            settingsMenu.visibility = True
        elif self.functionality == "return":
            settingsMenu.visibility = False
            mainMenu.visibility = True


class Menu:
    def __init__(self, visibility, vertical_offset, font_size, text_header, *menu_items):
        self.text_header = text_header
        self.vertical_offset = vertical_offset
        self.font_size = font_size
        self.list_menu_items = []
        for menu_item in menu_items:
            self.list_menu_items.append(menu_item)
        self.current_round = - 1
        self.visibility = visibility

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


mainMenu = Menu(True, -90, 60,
                Text(menu_font, "Larpland"),
                Text(menu_font, "Enter", "enter_main"),
                Text(menu_font, "Settings", "settings_main"),
                Text(menu_font, "Exit", "exit_main"))

settingsMenu = Menu(False, -90, 60,
                    Text(menu_font, "Settings"),
                    Text(menu_font, "Menu style"),
                    Text(menu_font, "Other"),
                    Text(menu_font, "Colors"),
                    Text(menu_font, "Return", "return"))


# Items and weapons
@dataclass
class Item:
    def __init__(self, name):
        self.name = name
        self.coin_value = None


@dataclass
class Weapon(Item):
    def __init__(self, name, speed):
        super().__init__(name)
        self.speed = speed
        self.damage = 10


@dataclass
class RangedWeapon(Weapon):
    def __init__(self, name, speed):
        super().__init__(name, speed)
        self.range = 50


@dataclass
class MeleeWeapon(Weapon):
    def __init__(self, name, speed):
        super().__init__(name, speed)
        self.range = 10


@dataclass
class MagicWeapon(Weapon):
    def __init__(self, name, speed):
        super().__init__(name, speed)
        self.range = 20


# Player
class Player:
    def __init__(self):
        self.items = []


default_text_box = Text(default_font, visibility=False)
weapon = db.get_random_weapon()

time_delay = 3000
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, time_delay)

text_array = ['You wake up cold in the snow . . .', 'What is your name?']

i = 0
run = False
while True:
    display.fill((0, 0, 0))

    if mainMenu.visibility:
        mainMenu.render()
    if settingsMenu.visibility:
        settingsMenu.render()
    if default_text_box.visibility:
        mainMenu.visibility = False
        run = True

    if run:
        default_text_box.render()

    for event in pygame.event.get():
        pressed = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # Main and settings menu functionalities
            if mainMenu.visibility or settingsMenu.visibility:
                if pressed[pygame.K_TAB] or pressed[pygame.K_DOWN]:
                    mainMenu.cycle("down") if mainMenu.visibility else settingsMenu.cycle("down")
                elif pressed[pygame.K_UP]:
                    mainMenu.cycle("up") if mainMenu.visibility else settingsMenu.cycle("up")
                elif pressed[pygame.K_SPACE] or pressed[pygame.K_RETURN]:
                    mainMenu.list_menu_items[mainMenu.current_round].do_action() if mainMenu.visibility \
                        else settingsMenu.list_menu_items[settingsMenu.current_round].do_action()
        if run:
            if event.type == timer_event:
                default_text_box.text = text_array[i]
                if i < (len(text_array) - 1):
                    i += 1
    clock.tick(60)
    pygame.display.update()
