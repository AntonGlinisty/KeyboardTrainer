import pygame
from MainFieldLines import LinesDrawer
import Globals as glob


def FrameDrawer(sce, sce_X, sce_Y, sf_X, sf_Y, sf_inf_Y, sf_inp_Y, sf_txt_Y):

    """
    Аргументы:
    :param sce: Поверхность, на которой будут рисоваться линии
    :param sce_X: Ширина этой пов-ти
    :param sce_Y: Ее высота
    :param sf_X: Ширина пов-ти, на которой изображена клавиатура
    :param sf_Y: Высота пов-ти, на которой изображена клавиатура
    :param sf_inf_Y: Высота поверхности со статистикой
    :param sf_inp_Y: Высота поверхности ввода
    :param sf_txt_Y: Высота пов-ти текста

    Описание: Функция рисует линии - границы поверхностей
    """

    sz_Y = sf_Y // glob.khc
    sz_X = sf_X // glob.kwc
    for linenumb in range(4):
        LinesDrawer(sce, glob.BLACK, 0, sce_Y - sz_Y * (linenumb + 1), sce_X, sce_Y - sz_Y * (linenumb + 1), 1)
    for linenumb in range(13):
        LinesDrawer(sce, glob.BLACK, sz_X * (linenumb + 1), sce_Y - sf_Y, sz_X * (linenumb + 1),
                    sce_Y - sf_Y // 5 * 4, 1)
    for linenumb in range(13):
        LinesDrawer(sce, glob.BLACK, sz_X * (linenumb + 1.5), sce_Y - sz_Y * 4, sz_X * (linenumb + 1.5),
                    sce_Y - sz_Y * 3, 1)
    for linenumb in range(12):
        LinesDrawer(sce, glob.BLACK, sz_X * (linenumb + 2), sce_Y - sz_Y * 3,  sz_X * (linenumb + 2),
                    sce_Y - sz_Y * 2, 1)
    for linenumb in range(11):
        LinesDrawer(sce, glob.BLACK, sz_X * (linenumb + 2.5), sce_Y - sz_Y * 2, sz_X * (linenumb + 2.5),
                    sce_Y - sz_Y, 1)
    LinesDrawer(sce, glob.BLACK, sz_X * 5, sce_Y - sz_Y, sz_X * 5, sce_Y, 1)
    LinesDrawer(sce, glob.BLACK, sz_X * 10, sce_Y - sz_Y, sz_X * 10, sce_Y, 1)
    for linenumb in range(2):
        LinesDrawer(sce, glob.BLACK, sf_X // 9 * (linenumb + 1), sce_Y - sf_Y // 5, sf_X // 9 * (linenumb + 1),
                    sce_Y, 1)
        LinesDrawer(sce, glob.BLACK, sce_X - sf_X // 9 * (linenumb + 1), sce_Y - sf_Y // 5,
                    sce_X - sf_X // 9 * (linenumb + 1), sce_Y, 1)
    LinesDrawer(sce, glob.BLACK, 0, sf_inf_Y + sf_inp_Y + sf_txt_Y, sf_X, sf_inf_Y + sf_inp_Y + sf_txt_Y, 3)

def DictOfSymbols():

    """
    Описание: Функция возвращает словарь, значениями в котором являются певерхности, отвечающие символам клавиатуры
    """

    L1 = pygame.font.SysFont('arial', glob.dict_of_s_s)
    dict = {
        'text1': L1.render('Q', True, (glob.BLACK)), 'text2': L1.render('q', True, (glob.BLACK)),
        'text3': L1.render('W', True, (glob.BLACK)), 'text4': L1.render('w', True, (glob.BLACK)),
        'text5': L1.render('E', True, (glob.BLACK)), 'text6': L1.render('e', True, (glob.BLACK)),
        'text7': L1.render('R', True, (glob.BLACK)), 'text8': L1.render('r', True, (glob.BLACK)),
        'text9': L1.render('T', True, (glob.BLACK)), 'text10': L1.render('t', True, (glob.BLACK)),
        'text11': L1.render('Y', True, (glob.BLACK)), 'text12': L1.render('y', True, (glob.BLACK)),
        'text13': L1.render('U', True, (glob.BLACK)), 'text14': L1.render('u', True, (glob.BLACK)),
        'text15': L1.render('I', True, (glob.BLACK)), 'text16': L1.render('i', True, (glob.BLACK)),
        'text17': L1.render('O', True, (glob.BLACK)), 'text18': L1.render('o', True, (glob.BLACK)),
        'text19': L1.render('P', True, (glob.BLACK)), 'text20': L1.render('p', True, (glob.BLACK)),
        'text21': L1.render('{', True, (glob.BLACK)), 'text22': L1.render('[', True, (glob.BLACK)),
        'text23': L1.render('}', True, (glob.BLACK)), 'text24': L1.render(']', True, (glob.BLACK)),
        'text25': L1.render('A', True, (glob.BLACK)), 'text26': L1.render('a', True, (glob.BLACK)),
        'text27': L1.render('S', True, (glob.BLACK)), 'text28': L1.render('s', True, (glob.BLACK)),
        'text29': L1.render('D', True, (glob.BLACK)), 'text30': L1.render('d', True, (glob.BLACK)),
        'text31': L1.render('F', True, (glob.BLACK)), 'text32': L1.render('f', True, (glob.BLACK)),
        'text33': L1.render('G', True, (glob.BLACK)), 'text34': L1.render('g', True, (glob.BLACK)),
        'text35': L1.render('H', True, (glob.BLACK)), 'text36': L1.render('h', True, (glob.BLACK)),
        'text37': L1.render('J', True, (glob.BLACK)), 'text38': L1.render('j', True, (glob.BLACK)),
        'text39': L1.render('K', True, (glob.BLACK)), 'text40': L1.render('k', True, (glob.BLACK)),
        'text41': L1.render('L', True, (glob.BLACK)), 'text42': L1.render('l', True, (glob.BLACK)),
        'text43': L1.render(':', True, (glob.BLACK)), 'text44': L1.render(';', True, (glob.BLACK)),
        'text45': L1.render('"', True, (glob.BLACK)), 'text46': L1.render("'", True, (glob.BLACK)),
        'text47': L1.render('Z', True, (glob.BLACK)), 'text48': L1.render('z', True, (glob.BLACK)),
        'text49': L1.render('X', True, (glob.BLACK)), 'text50': L1.render('x', True, (glob.BLACK)),
        'text51': L1.render('C', True, (glob.BLACK)), 'text52': L1.render('c', True, (glob.BLACK)),
        'text53': L1.render('V', True, (glob.BLACK)), 'text54': L1.render('v', True, (glob.BLACK)),
        'text55': L1.render('B', True, (glob.BLACK)), 'text56': L1.render('b', True, (glob.BLACK)),
        'text57': L1.render('N', True, (glob.BLACK)), 'text58': L1.render('n', True, (glob.BLACK)),
        'text59': L1.render('M', True, (glob.BLACK)), 'text60': L1.render('m', True, (glob.BLACK)),
        'text61': L1.render('<', True, (glob.BLACK)), 'text62': L1.render(',', True, (glob.BLACK)),
        'text63': L1.render('>', True, (glob.BLACK)), 'text64': L1.render('.', True, (glob.BLACK)),
        'text65': L1.render('?', True, (glob.BLACK)), 'text66': L1.render('/', True, (glob.BLACK)),
        'text67': L1.render('~', True, (glob.BLACK)), 'text68': L1.render('`', True, (glob.BLACK)),
        'text69': L1.render('!', True, (glob.BLACK)), 'text70': L1.render('1', True, (glob.BLACK)),
        'text71': L1.render('@', True, (glob.BLACK)), 'text72': L1.render('2', True, (glob.BLACK)),
        'text73': L1.render('#', True, (glob.BLACK)), 'text74': L1.render('3', True, (glob.BLACK)),
        'text75': L1.render('$', True, (glob.BLACK)), 'text76': L1.render('4', True, (glob.BLACK)),
        'text77': L1.render('%', True, (glob.BLACK)), 'text78': L1.render('5', True, (glob.BLACK)),
        'text79': L1.render('^', True, (glob.BLACK)), 'text80': L1.render('6', True, (glob.BLACK)),
        'text81': L1.render('&', True, (glob.BLACK)), 'text82': L1.render('7', True, (glob.BLACK)),
        'text83': L1.render('*', True, (glob.BLACK)), 'text84': L1.render('8', True, (glob.BLACK)),
        'text85': L1.render('(', True, (glob.BLACK)), 'text86': L1.render('9', True, (glob.BLACK)),
        'text87': L1.render(')', True, (glob.BLACK)), 'text88': L1.render('0', True, (glob.BLACK)),
        'text89': L1.render('_', True, (glob.BLACK)), 'text90': L1.render('-', True, (glob.BLACK)),
        'text91': L1.render('+', True, (glob.BLACK)), 'text92': L1.render('=', True, (glob.BLACK)),
        'text93': L1.render('Tab', True, (glob.BLACK)), 'text94': L1.render('Caps Lock', True, (glob.BLACK)),
        'text95': L1.render('Shift', True, (glob.BLACK)), 'text96': L1.render('Ctrl', True, (glob.BLACK)),
        'text97': L1.render('Alt', True, (glob.BLACK)), 'text98': L1.render('AltGr', True, (glob.BLACK)),
        'text99': L1.render('Ctrl', True, (glob.BLACK)), 'text100': L1.render('Shift', True, (glob.BLACK)),
        'text101': L1.render('Enter', True, (glob.BLACK)), 'text102': L1.render('Back', True, (glob.BLACK)),
        'text103': L1.render('|', True, (glob.BLACK)), 'text104': L1.render('\\', True, (glob.BLACK)),
        'text105': L1.render('Space', True, (glob.BLACK)),
    }
    return dict

def EngSymbolsDrawer(dict, surf_xcord, surface_ycord, surf_ycord, surface):

    """
    Аргументы:
    :param dict: Словарь с поверхностями, отвечающими символам клавиатуры
    :param surf_xcord: Ширина повехности клавиатуры
    :param surface_ycord: Высота экрана
    :param surf_ycord: Высота повехности клавиатуры
    :param surface: Основная поверхность

    Описание: Функция рисует символы на клавишах клавиатуры
    """

    consts = (surface, surf_xcord, surf_ycord, surface_ycord, dict, glob.khc)
    for letnumb in range(glob.fst_line_cou):
        Let_Drawer((letnumb + 1) * 2 - 1, consts, glob.indent1, glob.indent1, glob.kwc, letnumb + 1.5, 4)
        Let_Drawer((letnumb + 1) * 2, consts, -glob.indent2, -glob.indent2 * 2, glob.kwc, letnumb + 2.5, 3)
    for letnumb in range(glob.sec_line_cou):
        Let_Drawer((glob.fst_line_cou + letnumb + 1) * 2 - 1, consts, glob.indent1, glob.indent1, glob.kwc, letnumb + 2, 3)
        Let_Drawer((glob.fst_line_cou + letnumb + 1) * 2, consts, -glob.indent2, -glob.indent2 * 2, glob.kwc, letnumb + 3, 2)
    for letnumb in range(glob.th_line_cou):
        Let_Drawer((glob.fst_line_cou + glob.sec_line_cou + letnumb + 1) * 2 - 1, consts, glob.indent1, glob.indent1,
                   glob.kwc, letnumb + 2.5, 2)
        Let_Drawer((glob.fst_line_cou + glob.sec_line_cou + letnumb + 1) * 2, consts, -glob.indent2, -glob.indent2 * 2,
                   glob.kwc, letnumb + 3.5, 1)
    for letnumb in range(glob.fth_line_cou):
        Let_Drawer((glob.fst_line_cou + glob.sec_line_cou + glob.th_line_cou + letnumb + 1) * 2 - 1, consts,
                   glob.indent1, glob.indent1, glob.kwc, letnumb, 5)
        Let_Drawer((glob.fst_line_cou + glob.sec_line_cou + glob.th_line_cou + letnumb + 1) * 2, consts, -glob.indent2,
                   -glob.indent2 * 2, glob.kwc, letnumb + 1, 4)
    Let_Drawer(93, consts, 0, 18, 100, 3.5, 4)
    Let_Drawer(94, consts, 0, 18, 60, 1.1, 3)
    Let_Drawer(95, consts, 0, 18, 18, 1.1, 2)
    Let_Drawer(96, consts, 0, 15, 25, 1, 1)
    Let_Drawer(97, consts, 0, 15, 30, 7.9, 1)
    Let_Drawer(98, consts, 0, 15, 30, 21.3, 1)
    Let_Drawer(99, consts, 0, 15, 30, 28.3, 1)
    Let_Drawer(100, consts, 0, 18, glob.kwc, 13.4, 2)
    Let_Drawer(101, consts, 0, 18, glob.kwc, 13.6, 3)
    Let_Drawer(102, consts, 0, 18, glob.kwc, 13.6, 5)
    Let_Drawer(103, consts, glob.indent1, glob.indent1, glob.kwc, 13.5, 4)
    Let_Drawer(104, consts, -glob.indent2, -glob.indent2 * 2, 1, 1, 3)
    Let_Drawer(105, consts, 0, 15, glob.kwc, 6.9, 1)

def KeyboardDrawer(surface, surface_xcord, surface_ycord, surf_xcord, surf_ycord, surf_info_cordy, surf_input_cordy,
                   surf_text_cordy):

    """
    Аргументы: Размеры поверхностей

    Описание: Функция полностью рисует клавиатуру в соответствующей области
    """

    FrameDrawer(surface, surface_xcord, surface_ycord, surf_xcord, surf_ycord, surf_info_cordy, surf_input_cordy,
                surf_text_cordy)
    dict = DictOfSymbols()
    EngSymbolsDrawer(dict, surf_xcord, surface_ycord, surf_ycord, surface)

def Let_Drawer(numb, consts, indent1, indent2, dev1, mult1, mult2):

    """
    Аргументы:
    :param numb: Порядковый номер символа
    :param consts: Кортеж констант(размеры пов-тей, количество клавиш по вертикали, ...)
    :param indent1: Отступ от границы клавиши по координате X
    :param indent2: Отступ от границы клавиши по координате Y
    :param dev1: Множитель отступа по координате X относительно левого края клавиатуры

    Описание: Функция рисует символы, отображаемые на клавишах клавиатуры
    """

    surface = consts[0]
    surf_xcord = consts[1]
    surf_ycord = consts[2]
    surface_ycord = consts[3]
    dict = consts[4]
    dev2 = consts[5]
    surface.blit(dict['text' + str(numb)], (surf_xcord // dev1 * mult1 + indent1,
                                            surface_ycord - surf_ycord // dev2 * mult2 + indent2))
