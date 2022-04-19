import pygame
import os
from datetime import datetime
from MainFieldLines import BordersDrawer
from MyKeyboard import KeyboardDrawer
from KeyboardPainter import DictOfCords
from KeyboardPainter import KeyboardPainter
from Text import ListOfSymbols
from Text import TextViewer
from Info import Info
from PersonInput import PrinterSearcher
from PersonInput import PersonInput

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 230, 0)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
RED = (255, 0, 0)
color0 = (0, 200, 0)
color1 = (20, 160, 0)
color2 = (40, 120, 0)
color3 = (80, 80, 0)
color4 = (100, 40, 0)
color5 = (125, 0, 0)
color6 = (150, 0, 0)
color7 = (175, 0, 0)
color8 = (200, 0, 0)
color9 = (225, 0, 0)
color10 = (255, 0, 0)

pygame.init()
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')

surface_cordx = 1053
surface_cordy = 700
surface_xcord = 1053
surface_ycord = 700
surface = pygame.display.set_mode((surface_cordx, surface_cordy))

filewithtext = 'text1'
indent1 = 5
indent2 = 18

left_line_size = 4
right_line_size = 7
up_line_size = down_line_size = 3
running = condition = marker1 = marker2 = marker3 = marker4 = marker5 = marker6 = marker7 = True
counter1 = counter2 = mistakes = condition_counter = lines_counter = letter_counter = word_counter = width = 0
timelist = []
clock = pygame.time.Clock()
string_scroller = 85
listoftw = []
start_time = datetime.now()

kwc = 15
khc = 5
hot_dict = {}

fon = pygame.image.load(os.path.join(img_folder, 'fon2.jpg'))
fon = pygame.transform.scale(fon, (surface_cordx, surface_cordy))
surface.blit(fon, (0, 0))

L1 = pygame.font.SysFont('calibri',  8 * surface_cordx // 600 + 12)
text = L1.render('KLICK HERE', True, (BLACK))
surface.blit(text, (surface_cordx // 25 * 11, surface_cordy // 2))
L2 = pygame.font.SysFont('calibri', 40)
text1 = L2.render('Text1', True, (RED))
text2 = L2.render('Text2', True, (RED))
text3 = L2.render('Text3', True, (RED))

settings = pygame.image.load(os.path.join(img_folder, 'pngwing.com.png'))
settings = pygame.transform.scale(settings, (50, 50))
surface.blit(settings, (5, 5))
futur = pygame.image.load(os.path.join(img_folder, 'palms.jpg!d'))
futur = pygame.transform.scale(futur, (surface_cordx, surface_cordy))
mon1 = pygame.image.load(os.path.join(img_folder, 'mon1.png'))
mon1 = pygame.transform.scale(mon1, (100, 100))
mon2 = pygame.image.load(os.path.join(img_folder, 'mon2.png'))
mon2 = pygame.transform.scale(mon2, (surface_cordy / 14 * 3, surface_cordy / 14 * 3))
mon3 = pygame.image.load(os.path.join(img_folder, 'mon3.png'))
mon3 = pygame.transform.scale(mon3, (surface_cordy / 14 * 3, surface_cordy / 14 * 3))
mon4 = pygame.image.load(os.path.join(img_folder, 'mon4.png'))
mon4 = pygame.transform.scale(mon4, (surface_cordy / 14 * 3, surface_cordy / 14 * 3))
L3 = pygame.font.SysFont('calibri', 17 + surface_cordx // 200 * 2)
L4 = pygame.font.SysFont('calibri', 15 + surface_cordx // 200 * 2)
text10 = L3.render('Choose text:', True, (BLACK))
text11 = L4.render('Choose resolution:', True, (BLACK))
kong1 = pygame.image.load(os.path.join(img_folder, 'kong1.png'))
kong1 = pygame.transform.scale(kong1, (surface_cordy / 14 * 2.5, surface_cordy / 14 * 2.5))
kong4 = pygame.image.load(os.path.join(img_folder, 'kong4.png'))
kong4 = pygame.transform.scale(kong4, (surface_cordy / 14 * 2.5, surface_cordy / 14 * 2.5))
kong3 = pygame.image.load(os.path.join(img_folder, 'kong3.png'))
kong3 = pygame.transform.scale(kong3, (surface_cordy / 14 * 2.5, surface_cordy / 14 * 2.5))

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ((event.pos[0] - surface_cordx // 2)*(event.pos[0] - surface_cordx // 2) +
                (event.pos[1] - surface_cordy // 2)*(event.pos[1] - surface_cordy // 2) <
                surface_cordx // 9 * surface_cordx // 9) and event.pos[1] < surface_cordy // 5 * 3 and marker1 == True:
                running = False
                marker6 = False
            if 5 < event.pos[1] < 55 and 5 < event.pos[0] < 55:
                if marker1:
                    surface.blit(futur, (0, 0))
                    surface.blit(mon2, (surface_cordx / 21 * 17, surface_cordy / 70 * 28))
                    surface.blit(mon3, (surface_cordx / 21 * 17, surface_cordy / 70 * 8))
                    surface.blit(mon4, (surface_cordx / 21 * 17, surface_cordy / 70 * 48))
                    surface.blit(text10, (surface_cordx / 21 * 17.1, surface_cordy / 70 * 4))
                    surface.blit(kong1, (surface_cordx / 21 * 2, surface_cordy / 70 * 13))
                    surface.blit(kong4, (surface_cordx / 21 * 2, surface_cordy / 70 * 29.5))
                    surface.blit(kong3, (surface_cordx / 21 * 2, surface_cordy / 70 * 46))
                    surface.blit(text11, (surface_cordx / 21 * 1.4, surface_cordy / 70 * 8))
                    marker1 = False
                else:
                    surface.blit(fon, (0, 0))
                    surface.blit(text, (surface_cordx // 25 * 11, surface_cordy // 2))
                    marker1 = True
                surface.blit(settings, (5, 5))
            if surface_cordx / 21 * 17 < event.pos[0] < surface_cordx / 21 * 17 + surface_cordy / 14 * 3 and \
                    surface_cordy / 70 * 8 < event.pos[1] < surface_cordy / 70 * 8 + surface_cordy / 14 * 3 and \
                    marker1 == False:
                filewithtext = 'text1'
            if surface_cordx / 21 * 17 < event.pos[0] < surface_cordx / 21 * 17 + surface_cordy / 14 * 3 and \
                    surface_cordy / 70 * 28 < event.pos[1] < surface_cordy / 70 * 28 + surface_cordy / 14 * 3 and \
                    marker1 == False:
                filewithtext = 'text2'
            if surface_cordx / 21 * 17 < event.pos[0] < surface_cordx / 21 * 17 + surface_cordy / 14 * 3 and \
                    surface_cordy / 70 * 48 < event.pos[1] < surface_cordy / 70 * 48 + surface_cordy / 14 * 3 and \
                    marker1 == False:
                filewithtext = 'text3'
            if surface_cordx / 21 * 2 < event.pos[0] < surface_cordx / 21 * 2 + surface_cordy / 14 * 2.5 and \
                    surface_cordy / 70 * 13 < event.pos[1] < surface_cordy / 70 * 13 + surface_cordy / 14 * 2.5 and \
                    marker1 == False:
                surface_xcord = 900
                surface_ycord = 600
                string_scroller = 70
            if surface_cordx / 21 * 2 < event.pos[0] < surface_cordx / 21 * 2 + surface_cordy / 14 * 2.5 and \
                    surface_cordy / 70 * 29.5 < event.pos[1] < surface_cordy / 70 * 29.5 + surface_cordy / 14 * 2.5 and \
                    marker1 == False:
                surface_xcord = 1053
                surface_ycord = 700
                string_scroller = 85
            if surface_cordx / 21 * 2 < event.pos[0] < surface_cordx / 21 * 2 + surface_cordy / 14 * 2.5 and \
                    surface_cordy / 70 * 46 < event.pos[1] < surface_cordy / 70 * 46 + surface_cordy / 14 * 2.5 and \
                    marker1 == False:
                surface_xcord = 1125
                surface_ycord = 750
                string_scroller = 90
    pygame.display.update()

surf_xcord = surface_xcord
surf_ycord = 300
surf_info_cordx = surface_xcord
surf_info_cordy = 60
surf_input_cordx = surface_xcord
surf_input_cordy = 60
surf_text_cordx = surface_xcord
surf_text_cordy = surface_ycord - surf_input_cordy - surf_info_cordy - surf_ycord
surface = pygame.display.set_mode((surface_xcord, surface_ycord))
surf_info = pygame.Surface((surf_info_cordx, surf_ycord))
surf_input = pygame.Surface((surf_input_cordx, surf_input_cordy))
surf_text = pygame.Surface((surf_text_cordx, surf_text_cordy))
surf = pygame.Surface((surf_xcord, surf_ycord))
surf_info.fill(WHITE)
surf_input.fill(WHITE)
surf_text.fill(WHITE)
surf.fill(WHITE)
running = True
surface.blit(surf, (0, surface_ycord - surf_ycord))
surface.blit(surf_info, (0, 0))
surface.blit(surf_input, (0, surf_info_cordy))
surface.blit(surf_text, (0, surf_input_cordy + surf_info_cordy))
indent4 = surf_input_cordx / 45

if marker6 == False:

    KeyboardDrawer(surface, surface_xcord, surface_ycord, surf_xcord, surf_ycord, BLACK, indent1, indent2, kwc, khc,
                   surf_info_cordy, surf_input_cordy, surf_text_cordy)
    BordersDrawer(surface, BLACK, surf_info_cordx, surf_input_cordx, surf_text_cordx, surf_info_cordy,
                      surf_input_cordy, surf_text_cordy,left_line_size, right_line_size, up_line_size, down_line_size, RED)
    list = ListOfSymbols(filewithtext)

    TextViewer(list, BLACK, surface, surf_text_cordx, surf_info_cordy, surf_input_cordy, surf_text_cordy, indent1, 0,
               WHITE, string_scroller)

    while running:
        clock.tick(FPS)
        if counter2 == len(list):
            marker7 = False
            running = False
        if marker2:
            if list[counter2] == 'Enter':
                letter = 'Enter'
            else:
                letter = list[counter2][counter1]
        else:
            letter = 'Space'
        if letter not in hot_dict:
            hot_dict[letter] = 0
        if marker1:
            KeyboardPainter(DictOfCords(surface_ycord, surf_xcord, surf_ycord)[letter], GREEN, surface)
            marker1 = False
        KeyboardDrawer(surface, surface_xcord, surface_ycord, surf_xcord, surf_ycord, BLACK, indent1, indent2,
                       kwc, khc, surf_info_cordy, surf_input_cordy, surf_text_cordy)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                marker7 = False
                running = False
            if event.type == pygame.KEYDOWN:
                condition = PrinterSearcher(event, letter)
                width, listoftw = PersonInput(width, event, surface, WHITE, listoftw, BLACK, condition,
                                              indent1, surf_info_cordy)
                if condition == True:
                    condition_counter += 1
                    if marker1 == False:
                        marker1 = True
                    if marker2 == False:
                        marker2 = True
                    if counter1 == len(list[counter2]) - 1 or letter == 'Enter':
                        word_counter += 1
                        lines_counter += len(list[counter2])
                        counter1 = -1
                        counter2 += 1
                        marker2 = False
                    else:
                        counter1 += 1
                    KeyboardPainter(DictOfCords(surface_ycord, surf_xcord, surf_ycord)[letter], WHITE, surface)
                if condition == False:
                    hot_dict[letter] += 1
                    mistakes += 1
                    KeyboardPainter(DictOfCords(surface_ycord, surf_xcord, surf_ycord)[letter], RED, surface)
                    marker1 = False
        if lines_counter >= string_scroller:
            lines_counter = 0
            TextViewer(list, BLACK, surface, surf_text_cordx, surf_info_cordy, surf_input_cordy, surf_text_cordy,
                       indent1, word_counter, WHITE, string_scroller)
            pygame.draw.rect(surface, WHITE, (0 + 3, surf_info_cordy + 3, surf_input_cordx - 6, surf_input_cordy - 6))
            width = 0
        timelist, marker4 = Info(start_time, surface, WHITE, surf_info_cordx, surf_info_cordy, word_counter,
                                 condition_counter, indent1, indent4, mistakes, marker4, timelist, BLACK, surface_xcord)
        pygame.display.update()
    sorted_tuples = sorted(hot_dict.items(), key=lambda item: item[1])
    sorted_dict = {k: v for k, v in sorted_tuples[::-1] if v > 0}
    print('Heatmap dict : ', sorted_dict)


running = True
imp_dict = DictOfCords(surface_ycord, surf_xcord, surf_ycord)
marker8 = True

rock = pygame.image.load(os.path.join(img_folder, 'rock.jpg'))
rock = pygame.transform.scale(rock, (surface_xcord, surf_info_cordy + surf_input_cordy + surf_text_cordy))
surface.blit(rock, (0, 0))

if marker7 == False:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if marker8:
            for letter in imp_dict.keys():
                if letter not in hot_dict.keys():
                    KeyboardPainter(DictOfCords(surface_ycord, surf_xcord, surf_ycord)[letter], color0, surface)
            for key, value in hot_dict.items():
                if value == 0:
                    KeyboardPainter(DictOfCords(surface_ycord, surf_xcord, surf_ycord)[key], color0, surface)
                if value == 1:
                    KeyboardPainter(DictOfCords(surface_ycord, surf_xcord, surf_ycord)[key], color1, surface)
                if value == 2:
                    KeyboardPainter(DictOfCords(surface_ycord, surf_xcord, surf_ycord)[key], color2, surface)
                if value == 3:
                    KeyboardPainter(DictOfCords(surface_ycord, surf_xcord, surf_ycord)[key], color3, surface)
                if value == 4:
                    KeyboardPainter(DictOfCords(surface_ycord, surf_xcord, surf_ycord)[key], color4, surface)
                if value == 5:
                    KeyboardPainter(DictOfCords(surface_ycord, surf_xcord, surf_ycord)[key], color5, surface)
                if value == 6:
                    KeyboardPainter(DictOfCords(surface_ycord, surf_xcord, surf_ycord)[key], color6, surface)
                if value == 7:
                    KeyboardPainter(DictOfCords(surface_ycord, surf_xcord, surf_ycord)[key], color7, surface)
                if value == 8:
                    KeyboardPainter(DictOfCords(surface_ycord, surf_xcord, surf_ycord)[key], color8, surface)
                if value == 9:
                    KeyboardPainter(DictOfCords(surface_ycord, surf_xcord, surf_ycord)[key], color9, surface)
                if value >= 10:
                    KeyboardPainter(DictOfCords(surface_ycord, surf_xcord, surf_ycord)[key], color10, surface)
            KeyboardDrawer(surface, surface_xcord, surface_ycord, surf_xcord, surf_ycord, BLACK, indent1, indent2,
                           kwc, khc, surf_info_cordy, surf_input_cordy, surf_text_cordy)
            marker8 = False
        clock.tick(FPS)
        pygame.display.update()