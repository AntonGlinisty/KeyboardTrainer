import pygame
import Globals as glob

def DictOfCords(surface_ycord, surf_xcord, surf_ycord):

    """
    Аргументы: Размеры поверхностей

    Описание: Функция возвращает словарь, ключами которого являются символы английской раскладки, а значениями -
    кортежи координат и размеров, соответствующих клавиш на клавиатуре, для последующей покраски этих клавиш
    """

    cords = (surf_xcord, surf_ycord, surface_ycord)
    dict = {
        'Q': CordsGet(1.5, 4, cords, 1),  'q': CordsGet(1.5, 4, cords, 1),  'W': CordsGet(2.5, 4, cords, 1),
        'w': CordsGet(2.5, 4, cords, 1),  'E': CordsGet(3.5, 4, cords, 1),  'e': CordsGet(3.5, 4, cords, 1),
        'R': CordsGet(4.5, 4, cords, 1),  'r': CordsGet(4.5, 4, cords, 1),  'T': CordsGet(5.5, 4, cords, 1),
        't': CordsGet(5.5, 4, cords, 1),  'Y': CordsGet(6.5, 4, cords, 1),  'y': CordsGet(6.5, 4, cords, 1),
        'U': CordsGet(7.5, 4, cords, 1),  'u': CordsGet(7.5, 4, cords, 1),  'I': CordsGet(8.5, 4, cords, 1),
        'i': CordsGet(8.5, 4, cords, 1),  'O': CordsGet(9.5, 4, cords, 1),  'o': CordsGet(9.5, 4, cords, 1),
        'P': CordsGet(10.5, 4, cords, 1), 'p': CordsGet(10.5, 4, cords, 1), '{': CordsGet(11.5, 4, cords, 1),
        '[': CordsGet(11.5, 4, cords, 1), '}': CordsGet(12.5, 4, cords, 1), ']': CordsGet(12.5, 4, cords, 1),
        'A': CordsGet(2, 3, cords, 1),    'a': CordsGet(2, 3, cords, 1),    'S': CordsGet(3, 3, cords, 1),
        's': CordsGet(3, 3, cords, 1),    'D': CordsGet(4, 3, cords, 1),    'd': CordsGet(4, 3, cords, 1),
        'F': CordsGet(5, 3, cords, 1),    'f': CordsGet(5, 3, cords, 1),    'G': CordsGet(6, 3, cords, 1),
        'g': CordsGet(6, 3, cords, 1),    'H': CordsGet(7, 3, cords, 1),    'h': CordsGet(7, 3, cords, 1),
        'J': CordsGet(8, 3, cords, 1),    'j': CordsGet(8, 3, cords, 1),    'K': CordsGet(9, 3, cords, 1),
        'k': CordsGet(9, 3, cords, 1),    'L': CordsGet(10, 3, cords, 1),   'l': CordsGet(10, 3, cords, 1),
        ':': CordsGet(11, 3, cords, 1),   ';': CordsGet(11, 3, cords, 1),   '"': CordsGet(12, 3, cords, 1),
        "'": CordsGet(12, 3, cords, 1),   'Z': CordsGet(2.5, 2, cords, 1),  'z': CordsGet(2.5, 2, cords, 1),
        'X': CordsGet(3.5, 2, cords, 1),  'x': CordsGet(3.5, 2, cords, 1),  'C': CordsGet(4.5, 2, cords, 1),
        'c': CordsGet(4.5, 2, cords, 1),  'V': CordsGet(5.5, 2, cords, 1),  'v': CordsGet(5.5, 2, cords, 1),
        'B': CordsGet(6.5, 2, cords, 1),  'b': CordsGet(6.5, 2, cords, 1),  'N': CordsGet(7.5, 2, cords, 1),
        'n': CordsGet(7.5, 2, cords, 1),  'M': CordsGet(8.5, 2, cords, 1),  'm': CordsGet(8.5, 2, cords, 1),
        '<': CordsGet(9.5, 2, cords, 1),  ',': CordsGet(9.5, 2, cords, 1),  '>': CordsGet(10.5, 2, cords, 1),
        '.': CordsGet(10.5, 2, cords, 1), '?': CordsGet(11.5, 2, cords, 1), '/': CordsGet(11.5, 2, cords, 1),
        '~': CordsGet(0, 5, cords, 1),    '`': CordsGet(0, 5, cords, 1),    '!': CordsGet(1, 5, cords, 1),
        '1': CordsGet(1, 5, cords, 1),    '@': CordsGet(2, 5, cords, 1),    '2': CordsGet(2, 5, cords, 1),
        '#': CordsGet(3, 5, cords, 1),    '3': CordsGet(3, 5, cords, 1),    '$': CordsGet(4, 5, cords, 1),
        '4': CordsGet(4, 5, cords, 1),    '%': CordsGet(5, 5, cords, 1),    '5': CordsGet(5, 5, cords, 1),
        '^': CordsGet(6, 5, cords, 1),    '6': CordsGet(6, 5, cords, 1),    '&': CordsGet(7, 5, cords, 1),
        '7': CordsGet(7, 5, cords, 1),    '*': CordsGet(8, 5, cords, 1),    '8': CordsGet(8, 5, cords, 1),
        '(': CordsGet(9, 5, cords, 1),    '9': CordsGet(9, 5, cords, 1),    ')': CordsGet(10, 5, cords, 1),
        '0': CordsGet(10, 5, cords, 1),   '_': CordsGet(11, 5, cords, 1),   '-': CordsGet(11, 5, cords, 1),
        '+': CordsGet(12, 5, cords, 1),   '=': CordsGet(12, 5, cords, 1),
        '|': CordsGet(13.5, 4, cords, 1.6), '\\': CordsGet(13.5, 4, cords, 1.6),
        'Enter': CordsGet(13, 3, cords, 2), 'Space': CordsGet(5, 1, cords, 5),
        'LCtrl': CordsGet(0, 1, cords, 15 / 9), 'LShift': CordsGet(0, 2, cords, 2.5),
        'Caps Lock': CordsGet(0, 3, cords, 2), 'Tab': CordsGet(0, 4, cords, 1.5),
        'Alt': CordsGet(30 / 9, 1, cords, 15 / 9), 'AltGr': CordsGet(10, 1, cords, 15 / 9),
        'RCtrl': CordsGet(40 / 3, 1, cords, 15 / 9), 'RShift': CordsGet(12.5, 2, cords, 15 / 5),
        'Backspace': CordsGet(13, 5, cords, 15 / 2),
    }
    return dict

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

