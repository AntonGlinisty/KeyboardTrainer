import pygame
import Globals as glob
from MyKeyboard import KeyboardDrawer


def KeyboardPainter(tuple, color, surface):

    """
    Аргументы:
    :param tuple: Кортеж из координат и размеров клавиши
    :param color: Цвет, в который нужно покрасить клавишу
    :param surface: Поверхность, на которой клавиши будут отображаться

    Описание: Функция красит нужную клавишу в нужный цвет
    """

    pygame.draw.rect(surface, color, tuple)

def CordsGet(surf_xc_kf, surf_yc_kf, cords, wid_dev):

    """
    Аргументы:
    :param surf_xc_kf: Множитель отступа по координате X относительно левого края клавиатуры
    :param surf_yc_kf: Множитель отступа по координате Y относительно верхнего края клавиатуры
    :param cords: Кортеж из размеров поверхностей, относительно которых вычисляются координаты и размеры клавиш
    :param wid_dev: Множитель ширины клавиши
    :return: Кортеж, в котором на первой позиции координата X верхнего левого угла клавиши, на второй - координата Y,
    на третьей ширина клавиши, на четвертой - высота. Все координаты и размеры зависят от переданных размеров пов-тей.

    Описание: Функция возвращает упакованный кортеж всех необходимых параметров для передачи в функцию KeyboardPainter
    """

    surf_xcord = cords[0]
    surf_ycord = cords[1]
    surface_ycord = cords[2]
    return (surf_xcord / glob.kwc * surf_xc_kf, surface_ycord - surf_ycord / glob.khc * surf_yc_kf,
            surf_xcord / glob.kwc * wid_dev, surf_ycord / glob.khc),

def AllKeysPainter(dictofcords, hot_dict, surface):

    """
    Аргументы:
    :param dictofcords: Словарь со значениями - координатами клавиш
    :param hot_dict: Словарь, ключами которого являются названия клавиш, при нажатии на которые пользователь ошибался,
    а значениями - количество ошибок
    :param surface: Основная поверхность

    Описание: Функция рисует hetmap - клавиатуру
    """

    for letter in dictofcords.keys():
        if letter not in hot_dict.keys():
            KeyboardPainter(dictofcords[letter], glob.color['color0'], surface)
    for key, value in hot_dict.items():
        for i in range(0, glob.maxbrht):
            if value == i:
                KeyboardPainter(dictofcords[key], glob.color['color' + str(i)], surface)
        if value >= glob.maxbrht:
            KeyboardPainter(dictofcords[key], glob.color['color' + str(glob.maxbrht)], surface)
    KeyboardDrawer(surface)

def ConditionChanger(condition, dictofcords, listofpassed, letter, surface, hot_dict, list):
    """
    Аргументы:
    :param condition: Состояние ввода
    :param dictofcords: Словарь со значениями - координатами клавиш
    :param listofpassed: Список уже напечатанных символов
    :param letter: Буква, которую предстоит напечатать
    :param surface: Основная поверхность
    :param hot_dict: Словарь, ключами которого являются названия клавиш, при нажатии на которые пользователь ошибался,
    а значениями - количество ошибок
    :param list: Список всех символом текста

    Описание: Функция отслеживает состояние воода и, в зависимости от него, изменяет счетчики(ошибок, правильно
    напечатанных символов, ...)
    """
    if condition == 'correct':
        glob.condition_counter += 1
        if glob.marker1 == False:
            glob.marker1 = True
        if glob.marker2 == False:
            glob.marker2 = True
        if glob.counter1 == len(list[glob.counter2]) - 1 or letter == 'Enter':
            glob.word_counter += 1
            glob.lines_counter += len(list[glob.counter2])
            glob.counter1 = -1
            glob.counter2 += 1
            glob.marker2 = False
        else:
            glob.counter1 += 1
        KeyboardPainter(dictofcords[listofpassed[len(listofpassed) - glob.dct_ind]], glob.WHITE, surface)
        KeyboardPainter(dictofcords[letter], glob.WHITE, surface)
    if condition == 'mistake':
        hot_dict[letter] += 1
        glob.mistakes += 1
        KeyboardPainter(dictofcords[listofpassed[len(listofpassed) - glob.dct_ind]], glob.WHITE, surface)
        KeyboardPainter(dictofcords[letter], glob.RED, surface)
        glob.marker1 = False
    return hot_dict