import pygame
from MainFieldLines import LinesDrawer
from Globals import *


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

    Описание: Функция рисует линии, разделяющие ряды клавиш
    """

    sz_Y = sf_Y // khc
    sz_X = sf_X // kwc
    for linenumb in range(hor_l_count):
        LinesDrawer(sce, BLACK, 0, sce_Y - sz_Y * (linenumb + lnumb_ind_hr), sce_X,
                    sce_Y - sz_Y * (linenumb + lnumb_ind_hr), def_l_size)
    for linenumb in range(ver_l_countUP):
        LinesDrawer(sce, BLACK, sz_X * (linenumb + lnumb_ind_hr), sce_Y - sf_Y, sz_X * (linenumb + lnumb_ind_hr),
                    sce_Y - sf_Y // khc * mult_UP, def_l_size)
    for linenumb in range(ver_l_countUP):
        LinesDrawer(sce, BLACK, sz_X * (linenumb + lnumb_ind_UP), sce_Y - sz_Y * mult_UP,
                    sz_X * (linenumb + lnumb_ind_UP), sce_Y - sz_Y * mult_MD, def_l_size)
    for linenumb in range(ver_l_countMD):
        LinesDrawer(sce, BLACK, sz_X * (linenumb + lnumb_ind_MD), sce_Y - sz_Y * mult_MD,
                    sz_X * (linenumb + lnumb_ind_MD), sce_Y - sz_Y * mult_DN, def_l_size)
    for linenumb in range(ver_l_countDN):
        LinesDrawer(sce, BLACK, sz_X * (linenumb + lnumb_ind_DN), sce_Y - sz_Y * mult_DN,
                    sz_X * (linenumb + lnumb_ind_DN), sce_Y - sz_Y, def_l_size)
    LinesDrawer(sce, BLACK, sz_X * alt_line_mult, sce_Y - sz_Y, sz_X * alt_line_mult, sce_Y, def_l_size)
    LinesDrawer(sce, BLACK, sz_X * ctrl_line_mult, sce_Y - sz_Y, sz_X * ctrl_line_mult, sce_Y, def_l_size)
    for linenumb in range(ver_l_countLW):
        LinesDrawer(sce, BLACK, sf_X // alt_line_dev * (linenumb + 1), sce_Y - sf_Y // ctrl_line_dev,
                    sf_X // alt_line_dev * (linenumb + 1), sce_Y, def_l_size)
        LinesDrawer(sce, BLACK, sce_X - sf_X // alt_line_dev * (linenumb + 1), sce_Y - sf_Y // ctrl_line_dev,
                    sce_X - sf_X // alt_line_dev * (linenumb + 1), sce_Y, def_l_size)
    LinesDrawer(sce, BLACK, 0, sf_inf_Y + sf_inp_Y + sf_txt_Y, sf_X, sf_inf_Y + sf_inp_Y + sf_txt_Y, down_line_size)

def DictOfSymbols():

    """
    Описание: Функция возвращает словарь, значениями в котором являются певерхности, отвечающие символам клавиатуры
    """

    L1 = pygame.font.SysFont('arial', dict_of_s_s)
    dict = {
        'text1': L1.render('Q', True, (BLACK)), 'text2': L1.render('q', True, (BLACK)),
        'text3': L1.render('W', True, (BLACK)), 'text4': L1.render('w', True, (BLACK)),
        'text5': L1.render('E', True, (BLACK)), 'text6': L1.render('e', True, (BLACK)),
        'text7': L1.render('R', True, (BLACK)), 'text8': L1.render('r', True, (BLACK)),
        'text9': L1.render('T', True, (BLACK)), 'text10': L1.render('t', True, (BLACK)),
        'text11': L1.render('Y', True, (BLACK)), 'text12': L1.render('y', True, (BLACK)),
        'text13': L1.render('U', True, (BLACK)), 'text14': L1.render('u', True, (BLACK)),
        'text15': L1.render('I', True, (BLACK)), 'text16': L1.render('i', True, (BLACK)),
        'text17': L1.render('O', True, (BLACK)), 'text18': L1.render('o', True, (BLACK)),
        'text19': L1.render('P', True, (BLACK)), 'text20': L1.render('p', True, (BLACK)),
        'text21': L1.render('{', True, (BLACK)), 'text22': L1.render('[', True, (BLACK)),
        'text23': L1.render('}', True, (BLACK)), 'text24': L1.render(']', True, (BLACK)),
        'text25': L1.render('A', True, (BLACK)), 'text26': L1.render('a', True, (BLACK)),
        'text27': L1.render('S', True, (BLACK)), 'text28': L1.render('s', True, (BLACK)),
        'text29': L1.render('D', True, (BLACK)), 'text30': L1.render('d', True, (BLACK)),
        'text31': L1.render('F', True, (BLACK)), 'text32': L1.render('f', True, (BLACK)),
        'text33': L1.render('G', True, (BLACK)), 'text34': L1.render('g', True, (BLACK)),
        'text35': L1.render('H', True, (BLACK)), 'text36': L1.render('h', True, (BLACK)),
        'text37': L1.render('J', True, (BLACK)), 'text38': L1.render('j', True, (BLACK)),
        'text39': L1.render('K', True, (BLACK)), 'text40': L1.render('k', True, (BLACK)),
        'text41': L1.render('L', True, (BLACK)), 'text42': L1.render('l', True, (BLACK)),
        'text43': L1.render(':', True, (BLACK)), 'text44': L1.render(';', True, (BLACK)),
        'text45': L1.render('"', True, (BLACK)), 'text46': L1.render("'", True, (BLACK)),
        'text47': L1.render('Z', True, (BLACK)), 'text48': L1.render('z', True, (BLACK)),
        'text49': L1.render('X', True, (BLACK)), 'text50': L1.render('x', True, (BLACK)),
        'text51': L1.render('C', True, (BLACK)), 'text52': L1.render('c', True, (BLACK)),
        'text53': L1.render('V', True, (BLACK)), 'text54': L1.render('v', True, (BLACK)),
        'text55': L1.render('B', True, (BLACK)), 'text56': L1.render('b', True, (BLACK)),
        'text57': L1.render('N', True, (BLACK)), 'text58': L1.render('n', True, (BLACK)),
        'text59': L1.render('M', True, (BLACK)), 'text60': L1.render('m', True, (BLACK)),
        'text61': L1.render('<', True, (BLACK)), 'text62': L1.render(',', True, (BLACK)),
        'text63': L1.render('>', True, (BLACK)), 'text64': L1.render('.', True, (BLACK)),
        'text65': L1.render('?', True, (BLACK)), 'text66': L1.render('/', True, (BLACK)),
        'text67': L1.render('~', True, (BLACK)), 'text68': L1.render('`', True, (BLACK)),
        'text69': L1.render('!', True, (BLACK)), 'text70': L1.render('1', True, (BLACK)),
        'text71': L1.render('@', True, (BLACK)), 'text72': L1.render('2', True, (BLACK)),
        'text73': L1.render('#', True, (BLACK)), 'text74': L1.render('3', True, (BLACK)),
        'text75': L1.render('$', True, (BLACK)), 'text76': L1.render('4', True, (BLACK)),
        'text77': L1.render('%', True, (BLACK)), 'text78': L1.render('5', True, (BLACK)),
        'text79': L1.render('^', True, (BLACK)), 'text80': L1.render('6', True, (BLACK)),
        'text81': L1.render('&', True, (BLACK)), 'text82': L1.render('7', True, (BLACK)),
        'text83': L1.render('*', True, (BLACK)), 'text84': L1.render('8', True, (BLACK)),
        'text85': L1.render('(', True, (BLACK)), 'text86': L1.render('9', True, (BLACK)),
        'text87': L1.render(')', True, (BLACK)), 'text88': L1.render('0', True, (BLACK)),
        'text89': L1.render('_', True, (BLACK)), 'text90': L1.render('-', True, (BLACK)),
        'text91': L1.render('+', True, (BLACK)), 'text92': L1.render('=', True, (BLACK)),
        'text93': L1.render('Tab', True, (BLACK)), 'text94': L1.render('Caps Lock', True, (BLACK)),
        'text95': L1.render('Shift', True, (BLACK)), 'text96': L1.render('Ctrl', True, (BLACK)),
        'text97': L1.render('Alt', True, (BLACK)), 'text98': L1.render('AltGr', True, (BLACK)),
        'text99': L1.render('Ctrl', True, (BLACK)), 'text100': L1.render('Shift', True, (BLACK)),
        'text101': L1.render('Enter', True, (BLACK)), 'text102': L1.render('Back', True, (BLACK)),
        'text103': L1.render('|', True, (BLACK)), 'text104': L1.render('\\', True, (BLACK)),
        'text105': L1.render('Space', True, (BLACK)),
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

    consts = (surface, surf_xcord, surf_ycord, surface_ycord, dict, khc)
    for letnumb in range(fst_line_cou):
        Let_Drawer((letnumb + l_nm_indf) * let_nmb_cf - 1, consts, indent1, indent1, kwc, letnumb + l_nm_inds, mult_UP)
        Let_Drawer((letnumb + l_nm_indf) * let_nmb_cf, consts, -indent2, -indent2 * indmult_f, kwc,
                   letnumb + l_nm_indft, mult_MD)
    for letnumb in range(sec_line_cou):
        Let_Drawer((fst_line_cou + letnumb + l_nm_indf) * let_nmb_cf - 1, consts, indent1, indent1, kwc,
                   letnumb + l_nm_indt, mult_MD)
        Let_Drawer((fst_line_cou + letnumb + l_nm_indf) * let_nmb_cf, consts, -indent2, -indent2 * indmult_f, kwc,
                   letnumb + l_nm_indfi, mult_DN)
    for letnumb in range(th_line_cou):
        Let_Drawer((fst_line_cou + sec_line_cou + letnumb + l_nm_indf) * let_nmb_cf - 1, consts, indent1, indent1,
                   kwc, letnumb + l_nm_indft, mult_DN)
        Let_Drawer((fst_line_cou + sec_line_cou + letnumb + l_nm_indf) * let_nmb_cf, consts, -indent2,
                   -indent2 * indmult_f, kwc, letnumb + l_nm_indsi, mult_LW)
    for letnumb in range(fth_line_cou):
        Let_Drawer((fst_line_cou + sec_line_cou + th_line_cou + letnumb + l_nm_indf) * let_nmb_cf - 1, consts,
                   indent1, indent1, kwc, letnumb, mult_SK)
        Let_Drawer((fst_line_cou + sec_line_cou + th_line_cou + letnumb + l_nm_indf) * let_nmb_cf, consts, -indent2,
                   -indent2 * 2, kwc, letnumb + l_nm_indf, mult_UP)
    Let_Drawer(93, consts, 0, wds_ind2, tab_dev, tab_mult, mult_UP)
    Let_Drawer(94, consts, 0, wds_ind2, cps_dev, cps_mult, mult_MD)
    Let_Drawer(95, consts, 0, wds_ind2, sft_dev, sft_mult, mult_DN)
    Let_Drawer(96, consts, 0, wds_ind1, ctrl_dev, ctrl_mult, mult_LW)
    Let_Drawer(97, consts, 0, wds_ind1, wds_dev1, alt_mult, mult_LW)
    Let_Drawer(98, consts, 0, wds_ind1, wds_dev1, altg_mult, mult_LW)
    Let_Drawer(99, consts, 0, wds_ind1, wds_dev1, rctrl_mult, mult_LW)
    Let_Drawer(100, consts, 0, wds_ind2, kwc, rsft_mult, mult_DN)
    Let_Drawer(101, consts, 0, wds_ind2, kwc, ent_mult, mult_MD)
    Let_Drawer(102, consts, 0, wds_ind2, kwc, bck_mult, mult_SK)
    Let_Drawer(103, consts, indent1, indent1, kwc, str_mult, mult_UP)
    Let_Drawer(104, consts, -indent2, -indent2 * indmult_f, slsh_dev, bdl_sl_mult, mult_MD)
    Let_Drawer(105, consts, 0, wds_ind1, kwc, spc_mult, mult_LW)

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
