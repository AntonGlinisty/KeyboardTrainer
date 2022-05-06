import pygame
import os
from datetime import datetime
from MainFieldLines import BordersDrawer
from MyKeyboard import KeyboardDrawer
from KeyboardPainter import KeyboardPainter
from Text import ListOfSymbols
from Text import TextViewer
from Info import Info
from PersonInput import PrinterSearcher
from PersonInput import PersonInput
from KeyboardPainter import AllKeysPainter
from KeyboardPainter import ConditionChanger
import EventChecker
import Globals as glob

timelist = []
listoftw = []
hot_dict = {}
pygame.init()
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
surface = pygame.display.set_mode((glob.surface_cordx, glob.surface_cordy))
clock = pygame.time.Clock()
start_time = datetime.now()
settings, kong1, kong3, kong4, mon2, mon3, mon4, fon, futur, text, text10, text11 = \
    EventChecker.PicsInitializer(surface, img_folder)

while glob.running:
    clock.tick(glob.FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            glob.running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            EventChecker.StartChecker(event)
            EventChecker.SettingsChecker(surface, event, settings, fon, text, futur, mon2, mon3, mon4, kong1, kong3,
                                         kong4, text10, text11)
            EventChecker.TextChanger(event)
            EventChecker.ResolutionChanger(event)
    pygame.display.update()

surface, surf_info, surf_input, surf_text, surf = EventChecker.SurfsInit()

if glob.marker6 == False:

    KeyboardDrawer(surface)
    BordersDrawer(surface, glob.surf_info_cordx, glob.surf_input_cordx, glob.surf_text_cordx, glob.surf_info_cordy,
                  glob.surf_input_cordy, glob.surf_text_cordy)
    list = ListOfSymbols(glob.filewithtext)
    TextViewer(list, surface,  0, glob.string_scroller, glob.ex_text_size)
    dictofcords = glob.dictofcords(glob.surf_xcord, glob.surf_ycord, glob.surface_ycord)
    listofpassed = []

    while glob.running:
        clock.tick(glob.FPS)
        if glob.counter2 == len(list):
            glob.marker7 = False
            glob.running = False
        if glob.marker2:
            if list[glob.counter2] == 'Enter':
                letter = 'Enter'
            else:
                letter = list[glob.counter2][glob.counter1]
        else:
            letter = 'Space'
        if len(listofpassed) == 0:
            listofpassed.append(letter)
        if listofpassed[len(listofpassed) - 1] != letter:
            listofpassed.append(letter)
        if letter not in hot_dict:
            hot_dict[letter] = 0
        if glob.marker1:
            KeyboardPainter(dictofcords[listofpassed[len(listofpassed) - glob.dct_ind]], glob.WHITE, surface)
            KeyboardPainter(dictofcords[letter], glob.GREEN, surface)
            glob.marker1 = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                glob.marker7 = False
                glob.running = False
            if event.type == pygame.KEYDOWN:
                condition = PrinterSearcher(event, letter)
                listoftw = PersonInput(event, surface, listoftw, condition)
                hot_dict = ConditionChanger(condition, dictofcords, listofpassed, letter, surface, hot_dict, list)
        if glob.lines_counter >= glob.string_scroller:
            lines_counter = 0
            TextViewer(list, surface, glob.word_counter, glob.string_scroller, glob.ex_text_size)
            pygame.draw.rect(surface, glob.WHITE, (glob.surf_area_ind_c, glob.surf_info_cordy + glob.surf_area_ind_c,
                            glob.surf_input_cordx - glob.surf_area_ind_s, glob.surf_input_cordy - glob.surf_area_ind_s))
            glob.width = 0
        timelist = Info(start_time, surface, glob.word_counter, glob.condition_counter, glob.mistakes,
                                      timelist)
        KeyboardDrawer(surface)
        pygame.display.update()
    sorted_tuples = sorted(hot_dict.items(), key=lambda item: item[1])
    sorted_dict = {k: v for k, v in sorted_tuples[::-1] if v > 0}
    print('Heatmap dict : ', sorted_dict)

glob.running = True
glob.marker8 = True
rock = pygame.image.load(os.path.join(img_folder, 'rock.jpg'))
rock = pygame.transform.scale(rock, (glob.surface_xcord, glob.surf_info_cordy + glob.surf_input_cordy +
                                     glob.surf_text_cordy))
surface.blit(rock, (0, 0))

if glob.marker7 == False:
    while glob.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                glob.running = False
        if glob.marker8:
            AllKeysPainter(dictofcords, hot_dict, surface)
            glob.marker8 = False
        clock.tick(glob.FPS)
        pygame.display.update()