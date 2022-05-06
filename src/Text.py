import pygame
import Globals as glob


def ListOfSymbols(text):

    """
    Аргументы:
    :param text: Название файла с текстом
    :return: Список всех символов текста

    Описание: Функция читает текст из файла и формирует список из всех его символов
    """

    list = []
    with open(text + '.txt', 'r+', encoding='utf_8') as file:
        for line in file.readlines():
            list += line.split(' ')
            list[len(list) - 1] = list[len(list) - 1][:-1]
            list.append('Enter')
    list = list[:-1]
    return list

def TextViewer(list, surface, word_counter, string_scroller, textsize):

    """
    Аргументы:
    :param list: Список всех символов текста
    :param surface: Поверхность, на которой будет отображаться текст
    :param word_counter: Количество уже написанных пользователем слов
    :param string_scroller: Максимальное количество символов в строке
    :param textsize: Размер выводимого текста

    Описание: Функция отображает заданное количество строк текста для печати в соответствующей области
    """

    pygame.draw.rect(surface, glob.WHITE, [0 + glob.txt_area_ind_c, glob.surf_info_cordy + glob.surf_input_cordy +
            glob.txt_area_ind_c, glob.surf_text_cordx - glob.txt_area_ind_s, glob.surf_text_cordy - glob.txt_area_ind_s])
    L1 = pygame.font.SysFont('verdana', textsize)
    width = 0
    for line_counter in range(5):
        length = 0
        for counter in range(word_counter, len(list)):
            if length >= string_scroller:
                width = 0
                break
            length += len(list[word_counter])
            for letter in list[word_counter]:
                text1 = L1.render(letter, True, (glob.BLACK))
                surface.blit(text1, (width + glob.indent1, glob.surf_info_cordy + glob.surf_input_cordy +
                                     glob.surf_text_cordy / glob.txt_ind_koef * line_counter + glob.txt_ind_koef))
                width += text1.get_width()
            text1 = L1.render(' ', True, (glob.BLACK))
            surface.blit(text1, (width + glob.indent1, glob.surf_info_cordy + glob.surf_input_cordy +
                                 glob.surf_text_cordy / glob.txt_ind_koef * line_counter + glob.txt_ind_koef))
            width += text1.get_width()
            word_counter += 1
