import pygame
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

    Описание: Функция рисует линии, разделяющие ряды клавиш
    """

    sz_Y = sf_Y // glob.khc
    sz_X = sf_X // glob.kwc
    for linenumb in range(glob.hor_l_count):
        LinesDrawer(sce, glob.BLACK, 0, sce_Y - sz_Y * (linenumb + glob.lnumb_ind_hr), sce_X,
                    sce_Y - sz_Y * (linenumb + glob.lnumb_ind_hr), glob.def_l_size)
    for linenumb in range(glob.ver_l_countUP):
        LinesDrawer(sce, glob.BLACK, sz_X * (linenumb + glob.lnumb_ind_hr), sce_Y - sf_Y,
                    sz_X * (linenumb + glob.lnumb_ind_hr), sce_Y - sf_Y // glob.khc * glob.mult_UP, glob.def_l_size)
    for linenumb in range(glob.ver_l_countUP):
        LinesDrawer(sce, glob.BLACK, sz_X * (linenumb + glob.lnumb_ind_UP), sce_Y - sz_Y * glob.mult_UP,
                    sz_X * (linenumb + glob.lnumb_ind_UP), sce_Y - sz_Y * glob.mult_MD, glob.def_l_size)
    for linenumb in range(glob.ver_l_countMD):
        LinesDrawer(sce, glob.BLACK, sz_X * (linenumb + glob.lnumb_ind_MD), sce_Y - sz_Y * glob.mult_MD,
                    sz_X * (linenumb + glob.lnumb_ind_MD), sce_Y - sz_Y * glob.mult_DN, glob.def_l_size)
    for linenumb in range(glob.ver_l_countDN):
        LinesDrawer(sce, glob.BLACK, sz_X * (linenumb + glob.lnumb_ind_DN), sce_Y - sz_Y * glob.mult_DN,
                    sz_X * (linenumb + glob.lnumb_ind_DN), sce_Y - sz_Y, glob.def_l_size)
    LinesDrawer(sce, glob.BLACK, sz_X * glob.alt_line_mult, sce_Y - sz_Y, sz_X * glob.alt_line_mult, sce_Y,
                glob.def_l_size)
    LinesDrawer(sce, glob.BLACK, sz_X * glob.ctrl_line_mult, sce_Y - sz_Y, sz_X * glob.ctrl_line_mult, sce_Y,
                glob.def_l_size)
    for linenumb in range(glob.ver_l_countLW):
        LinesDrawer(sce, glob.BLACK, sf_X // glob.alt_line_dev * (linenumb + 1), sce_Y - sf_Y // glob.ctrl_line_dev,
                    sf_X // glob.alt_line_dev * (linenumb + 1), sce_Y, glob.def_l_size)
        LinesDrawer(sce, glob.BLACK, sce_X - sf_X // glob.alt_line_dev * (linenumb + 1), sce_Y - sf_Y //
                    glob.ctrl_line_dev, sce_X - sf_X // glob.alt_line_dev * (linenumb + 1), sce_Y, glob.def_l_size)
    LinesDrawer(sce, glob.BLACK, 0, sf_inf_Y + sf_inp_Y + sf_txt_Y, sf_X, sf_inf_Y + sf_inp_Y + sf_txt_Y,
                glob.down_line_size)

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

def EngSymbolsDrawer(dict, surface):

    """
    Аргументы:
    :param dict: Словарь с поверхностями, отвечающими символам клавиатуры
    :param surface: Основная поверхность

    Описание: Функция рисует символы на клавишах клавиатуры
    """

    consts = (surface, dict)
    for letnumb in range(glob.fst_line_cou):
        Let_Drawer((letnumb + glob.l_nm_indf) * glob.let_nmb_cf - 1, consts, glob.indent1, glob.indent1, glob.kwc,
                   letnumb + glob.l_nm_inds, glob.mult_UP)
        Let_Drawer((letnumb + glob.l_nm_indf) * glob.let_nmb_cf, consts, -glob.indent2, -glob.indent2 * glob.indmult_f,
                   glob.kwc, letnumb + glob.l_nm_indft, glob.mult_MD)
    for letnumb in range(glob.sec_line_cou):
        Let_Drawer((glob.fst_line_cou + letnumb + glob.l_nm_indf) * glob.let_nmb_cf - 1, consts, glob.indent1,
                   glob.indent1, glob.kwc, letnumb + glob.l_nm_indt, glob.mult_MD)
        Let_Drawer((glob.fst_line_cou + letnumb + glob.l_nm_indf) * glob.let_nmb_cf, consts, -glob.indent2,
                   -glob.indent2 * glob.indmult_f, glob.kwc, letnumb + glob.l_nm_indfi, glob.mult_DN)
    for letnumb in range(glob.th_line_cou):
        Let_Drawer((glob.fst_line_cou + glob.sec_line_cou + letnumb + glob.l_nm_indf) * glob.let_nmb_cf - 1, consts,
                   glob.indent1, glob.indent1, glob.kwc, letnumb + glob.l_nm_indft, glob.mult_DN)
        Let_Drawer((glob.fst_line_cou + glob.sec_line_cou + letnumb + glob.l_nm_indf) * glob.let_nmb_cf, consts,
                   -glob.indent2, -glob.indent2 * glob.indmult_f, glob.kwc, letnumb + glob.l_nm_indsi, glob.mult_LW)
    for letnumb in range(glob.fth_line_cou):
        Let_Drawer((glob.fst_line_cou + glob.sec_line_cou + glob.th_line_cou + letnumb + glob.l_nm_indf) *
                   glob.let_nmb_cf - 1, consts, glob.indent1, glob.indent1, glob.kwc, letnumb, glob.mult_SK)
        Let_Drawer((glob.fst_line_cou + glob.sec_line_cou + glob.th_line_cou + letnumb + glob.l_nm_indf) *
            glob.let_nmb_cf, consts, -glob.indent2, -glob.indent2 * 2, glob.kwc, letnumb + glob.l_nm_indf, glob.mult_UP)
    Let_Drawer(glob.tab_numb, consts, 0, glob.wds_ind2, glob.tab_dev, glob.tab_mult, glob.mult_UP)
    Let_Drawer(glob.caps_numb, consts, 0, glob.wds_ind2, glob.cps_dev, glob.cps_mult, glob.mult_MD)
    Let_Drawer(glob.l_shft_numb, consts, 0, glob.wds_ind2, glob.sft_dev, glob.sft_mult, glob.mult_DN)
    Let_Drawer(glob.l_ctrl_numb, consts, 0, glob.wds_ind1, glob.ctrl_dev, glob.ctrl_mult, glob.mult_LW)
    Let_Drawer(glob.alt_numb, consts, 0, glob.wds_ind1, glob.wds_dev1, glob.alt_mult, glob.mult_LW)
    Let_Drawer(glob.altgr_numb, consts, 0, glob.wds_ind1, glob.wds_dev1, glob.altg_mult, glob.mult_LW)
    Let_Drawer(glob.r_ctrl_numb, consts, 0, glob.wds_ind1, glob.wds_dev1, glob.rctrl_mult, glob.mult_LW)
    Let_Drawer(glob.r_shft_numb, consts, 0, glob.wds_ind2, glob.kwc, glob.rsft_mult, glob.mult_DN)
    Let_Drawer(glob.enter_numb, consts, 0, glob.wds_ind2, glob.kwc, glob.ent_mult, glob.mult_MD)
    Let_Drawer(glob.back_numb, consts, 0, glob.wds_ind2, glob.kwc, glob.bck_mult, glob.mult_SK)
    Let_Drawer(glob.str_line_numb, consts, glob.indent1, glob.indent1, glob.kwc, glob.str_mult, glob.mult_UP)
    Let_Drawer(glob.db_backsl_numb, consts, -glob.indent2, -glob.indent2 * glob.indmult_f, glob.slsh_dev,
               glob.bdl_sl_mult, glob.mult_MD)
    Let_Drawer(glob.space_numb, consts, 0, glob.wds_ind1, glob.kwc, glob.spc_mult, glob.mult_LW)

def KeyboardDrawer(surface):

    """
    Аргументы: Основная поверхность

    Описание: Функция полностью рисует клавиатуру в соответствующей области
    """

    FrameDrawer(surface, glob.surface_xcord, glob.surface_ycord, glob.surf_xcord, glob.surf_ycord, glob.surf_info_cordy,
                glob.surf_input_cordy, glob.surf_text_cordy)
    dict = DictOfSymbols()
    EngSymbolsDrawer(dict, surface)

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

    surface, dict = consts
    dev2 = glob.khc
    surface.blit(dict['text' + str(numb)], (glob.surf_xcord // dev1 * mult1 + indent1,
                                            glob.surface_ycord - glob.surf_ycord // dev2 * mult2 + indent2))

def LinesDrawer(surface, color, l_cordX, l_cordY, r_cordX, r_cordY, size):

    """
    Аргументы:
    :param surface: Поверхность, на которой рисуются линии
    :param color: Цвет линий
    :param l_cordX: Координата X левого конца линии
    :param l_cordY: Координата Y левого конца линии
    :param r_cordX: Координата X правого конца линии
    :param r_cordY: Координата Y правого конца линии
    :param size: Размер линии

    Описание: Функция рисует линию по заданным параметрам
    """

    pygame.draw.line(surface, color, [l_cordX, l_cordY], [r_cordX, r_cordY], size)