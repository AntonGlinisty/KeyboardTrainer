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
from Globals import *

pygame.init()
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
surface = pygame.display.set_mode((surface_cordx, surface_cordy))
clock = pygame.time.Clock()
start_time = datetime.now()
fon = pygame.image.load(os.path.join(img_folder, 'fon2.jpg'))
fon = pygame.transform.scale(fon, (surface_cordx, surface_cordy))
surface.blit(fon, (sf_spawn, sf_spawn))
L1 = pygame.font.SysFont('calibri', surface_cordx // l1_dev + l1_ind)
text = L1.render('KLICK HERE', True, (BLACK))
surface.blit(text, (surface_cordx // strt_x_d3 * strt_y_m2, surface_cordy // l_s_dev))
L2 = pygame.font.SysFont('calibri', l2_size)
text1 = L2.render('Text1', True, (RED))
text2 = L2.render('Text2', True, (RED))
text3 = L2.render('Text3', True, (RED))
settings = pygame.image.load(os.path.join(img_folder, 'pngwing.com.png'))
settings = pygame.transform.scale(settings, (set_ev_u - set_ev_d, set_ev_u - set_ev_d))
surface.blit(settings, (set_ev_d, set_ev_d))
futur = pygame.image.load(os.path.join(img_folder, 'palms.jpg!d'))
futur = pygame.transform.scale(futur, (surface_cordx, surface_cordy))
mon1 = pygame.image.load(os.path.join(img_folder, 'mon1.png'))
mon1 = pygame.transform.scale(mon1, (mon_size, mon_size))
mon2 = pygame.image.load(os.path.join(img_folder, 'mon2.png'))
mon2 = pygame.transform.scale(mon2, (surface_cordy / mon_size_dev, surface_cordy / mon_size_dev))
mon3 = pygame.image.load(os.path.join(img_folder, 'mon3.png'))
mon3 = pygame.transform.scale(mon3, (surface_cordy / mon_size_dev, surface_cordy / mon_size_dev))
mon4 = pygame.image.load(os.path.join(img_folder, 'mon4.png'))
mon4 = pygame.transform.scale(mon4, (surface_cordy / mon_size_dev, surface_cordy / mon_size_dev))
L3 = pygame.font.SysFont('calibri', l3_x_ind + surface_cordx // l3_x_ind_dev)
L4 = pygame.font.SysFont('calibri', l4_x_ind + surface_cordx // l4_x_ind_dev)
text10 = L3.render('Choose text:', True, (BLACK))
text11 = L4.render('Choose resolution:', True, (BLACK))
kong1 = pygame.image.load(os.path.join(img_folder, 'kong1.png'))
kong1 = pygame.transform.scale(kong1, (surface_cordy / kong_size_dev, surface_cordy / kong_size_dev))
kong4 = pygame.image.load(os.path.join(img_folder, 'kong4.png'))
kong4 = pygame.transform.scale(kong4, (surface_cordy / kong_size_dev, surface_cordy / kong_size_dev))
kong3 = pygame.image.load(os.path.join(img_folder, 'kong3.png'))
kong3 = pygame.transform.scale(kong3, (surface_cordy / kong_size_dev, surface_cordy / kong_size_dev))

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ((event.pos[0] - surface_cordx // strt_x_d1)*(event.pos[0] - surface_cordx // strt_x_d1) +
                (event.pos[1] - surface_cordy // strt_x_d1)*(event.pos[1] - surface_cordy // strt_x_d1) <
                (surface_cordx // strt_x_d2 * surface_cordx // strt_x_d2)) and event.pos[1] < surface_cordy // \
                    strt_y_d1 * strt_y_m1 and marker1 == True:
                running = False
                marker6 = False
            if set_ev_d < event.pos[1] < set_ev_u and set_ev_d < event.pos[0] < set_ev_u:
                if marker1:
                    surface.blit(futur, (sf_spawn, sf_spawn))
                    surface.blit(mon2, (surface_cordx / mon_x_dev, surface_cordy / mon2_y_dev))
                    surface.blit(mon3, (surface_cordx / mon_x_dev, surface_cordy / mon3_y_dev))
                    surface.blit(mon4, (surface_cordx / mon_x_dev, surface_cordy / mon4_y_dev))
                    surface.blit(text10, (surface_cordx / chootxt_x, surface_cordy / chootxt_y))
                    surface.blit(kong1, (surface_cordx / kong_x_dev, surface_cordy / kong1_y_dev))
                    surface.blit(kong4, (surface_cordx / kong_x_dev, surface_cordy / kong4_y_dev))
                    surface.blit(kong3, (surface_cordx / kong_x_dev, surface_cordy / kong3_y_dev))
                    surface.blit(text11, (surface_cordx / choores_x, surface_cordy / choores_y))
                    marker1 = False
                else:
                    surface.blit(fon, (sf_spawn, sf_spawn))
                    surface.blit(text, (surface_cordx // strt_x_d3 * strt_y_m2, surface_cordy // strt_x_d1))
                    marker1 = True
                surface.blit(settings, (set_ev_d, set_ev_d))
            if (surface_cordx / mon_x_dev1 < event.pos[0] < surface_cordx / mon_x_dev1 + surface_cordy / mon1_y_dev1
                    and surface_cordy / mon1_y_devs < event.pos[1] < surface_cordy / mon1_y_devs + surface_cordy /
                    mon1_y_dev1 and marker1 == False):
                filewithtext = 'text1'
            if (surface_cordx / mon_x_dev1 < event.pos[0] < surface_cordx / mon_x_dev1 + surface_cordy / mon1_y_dev1
                    and surface_cordy / mon2_y_devs < event.pos[1] < surface_cordy / mon2_y_devs + surface_cordy /
                    mon1_y_dev1 and marker1 == False):
                filewithtext = 'text2'
            if (surface_cordx / mon_x_dev1 < event.pos[0] < surface_cordx / mon_x_dev1 + surface_cordy / mon1_y_dev1
                    and surface_cordy / mon3_y_devs < event.pos[1] < surface_cordy / mon3_y_devs + surface_cordy /
                    mon1_y_dev1 and marker1 == False):
                filewithtext = 'text3'
            if (surface_cordx / kong_x_dev1 < event.pos[0] < surface_cordx / kong_x_dev1 + surface_cordy / kong_x_devs
                    and surface_cordy / kong1_y_devs < event.pos[1] < surface_cordy / kong1_y_devs + surface_cordy /
                    kong_x_devs and marker1 == False):
                surface_xcord = res1_x
                surface_ycord = res1_y
                string_scroller = scrol1
            if (surface_cordx / kong_x_dev1 < event.pos[0] < surface_cordx / kong_x_dev1 + surface_cordy / kong_x_devs
                    and surface_cordy / kong2_y_devs < event.pos[1] < surface_cordy / kong2_y_devs + surface_cordy /
                    kong_x_devs and marker1 == False):
                surface_xcord = res2_x
                surface_ycord = res2_y
                string_scroller = scrol2
            if (surface_cordx / kong_x_dev1 < event.pos[0] < surface_cordx / kong_x_dev1 + surface_cordy / kong_x_devs
                    and surface_cordy / kong3_y_devs < event.pos[1] < surface_cordy / kong3_y_devs + surface_cordy /
                    kong_x_devs and marker1 == False):
                surface_xcord = res3_x
                surface_ycord = res3_y
                string_scroller = scrol3
    pygame.display.update()

surf_xcord = surface_xcord
surf_info_cordx = surface_xcord
surf_input_cordx = surface_xcord
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
indent4 = surf_input_cordx / ind4dev

if marker6 == False:

    KeyboardDrawer(surface, surface_xcord, surface_ycord, surf_xcord, surf_ycord, surf_info_cordy,
                   surf_input_cordy, surf_text_cordy)
    BordersDrawer(surface, surf_info_cordx, surf_input_cordx, surf_text_cordx, surf_info_cordy, surf_input_cordy,
                  surf_text_cordy)
    list = ListOfSymbols(filewithtext)

    TextViewer(list, surface, surf_text_cordx, surf_info_cordy, surf_input_cordy, surf_text_cordy, 0,
               string_scroller, ex_text_size)
    dictofcords = DictOfCords(surface_ycord, surf_xcord, surf_ycord)
    listofpassed = []

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
        if len(listofpassed) == 0:
            listofpassed.append(letter)
        if listofpassed[len(listofpassed) - 1] != letter:
            listofpassed.append(letter)
        if letter not in hot_dict:
            hot_dict[letter] = 0
        if marker1:
            KeyboardPainter(dictofcords[listofpassed[len(listofpassed) - dct_ind]], WHITE, surface)
            KeyboardPainter(dictofcords[letter], GREEN, surface)
            marker1 = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                marker7 = False
                running = False
            if event.type == pygame.KEYDOWN:
                condition = PrinterSearcher(event, letter)
                width, listoftw = PersonInput(width, event, surface, listoftw, condition, surf_info_cordy, ex_text_size)
                if condition == 'correct':
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
                    KeyboardPainter(dictofcords[listofpassed[len(listofpassed) - dct_ind]], WHITE, surface)
                    KeyboardPainter(dictofcords[letter], WHITE, surface)
                if condition == 'mistake':
                    hot_dict[letter] += 1
                    mistakes += 1
                    KeyboardPainter(dictofcords[listofpassed[len(listofpassed) - dct_ind]], WHITE, surface)
                    KeyboardPainter(dictofcords[letter], RED, surface)
                    marker1 = False
        if lines_counter >= string_scroller:
            lines_counter = 0
            TextViewer(list, surface, surf_text_cordx, surf_info_cordy, surf_input_cordy, surf_text_cordy, word_counter,
                       string_scroller, ex_text_size)
            pygame.draw.rect(surface, WHITE, (0 + surf_area_ind_c, surf_info_cordy + surf_area_ind_c,
                                              surf_input_cordx - surf_area_ind_s, surf_input_cordy - surf_area_ind_s))
            width = 0
        timelist, marker4 = Info(start_time, surface, surf_info_cordx, surf_info_cordy, word_counter,
                                 condition_counter, indent4, mistakes, marker4, timelist, surface_xcord)
        KeyboardDrawer(surface, surface_xcord, surface_ycord, surf_xcord, surf_ycord, surf_info_cordy,
                       surf_input_cordy, surf_text_cordy)
        pygame.display.update()
    sorted_tuples = sorted(hot_dict.items(), key=lambda item: item[1])
    sorted_dict = {k: v for k, v in sorted_tuples[::-1] if v > 0}
    print('Heatmap dict : ', sorted_dict)

running = True
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
            for letter in dictofcords.keys():
                if letter not in hot_dict.keys():
                    KeyboardPainter(dictofcords[letter], color['color0'], surface)
            for key, value in hot_dict.items():
                for i in range(0, maxbrht):
                    if value == i:
                        KeyboardPainter(dictofcords[key], color['color' + str(i)], surface)
                if value >= maxbrht:
                    KeyboardPainter(dictofcords[key], color['color' + str(maxbrht)], surface)
            KeyboardDrawer(surface, surface_xcord, surface_ycord, surf_xcord, surf_ycord, surf_info_cordy,
                           surf_input_cordy, surf_text_cordy)
            marker8 = False
        clock.tick(FPS)
        pygame.display.update()