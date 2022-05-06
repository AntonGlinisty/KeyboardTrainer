import pygame
import Globals as glob

def BordersDrawer(surface, surf_inf_cX, surf_inp_cX, surf_text_cX, surf_inf_cY, surf_inp_cY, surf_text_cY):

    """
    Аргументы:
    :param surface: Поверхность, на которой будут отображаться границы других пов-тей
    :param surf_inf_cX: Ширина поверхности статистики
    :param surf_inp_cX: Ширина поверхности ввода
    :param surf_text_cX: Ширина поверхности текста
    :param surf_inf_cY: Высота поверхности статистики
    :param surf_inp_cY: Высота поверхности ввода
    :param surf_text_cY: Высота поверхности текста

    Описание: Функция рисует линии границы пов-тей(для статистики, ввода, текста и клавиатуры)
    """

    cordY = surf_inf_cY + surf_inp_cY
    LinesDrawer(surface, glob.BLACK, 0, 0, 0, surf_inf_cY, glob.left_line_size)
    LinesDrawer(surface, glob.BLACK, surf_inf_cX, 0, surf_inf_cX, surf_inf_cY, glob.right_line_size)
    LinesDrawer(surface, glob.BLACK, 0, glob.up_line_size // 2, surf_inf_cX, glob.up_line_size // 2, glob.up_line_size)
    LinesDrawer(surface, glob.BLACK, 0, surf_inf_cY - glob.down_line_size // 2 - 1, surf_inf_cX,
                surf_inf_cY - glob.down_line_size // 2 - 1, glob.down_line_size)
    LinesDrawer(surface, glob.RED, 0, surf_inf_cY, 0, cordY, glob.left_line_size)
    LinesDrawer(surface, glob.RED, surf_inf_cX, surf_inf_cY, surf_inp_cX, cordY, glob.right_line_size)
    LinesDrawer(surface, glob.RED, 0, surf_inf_cY + glob.up_line_size // 2, surf_inp_cX,
                surf_inp_cY + glob.up_line_size // 2, glob.up_line_size)
    LinesDrawer(surface, glob.RED, 0, cordY - glob.down_line_size // 2 - 1, surf_inp_cX,
                cordY - glob.down_line_size // 2 - 1, glob.down_line_size)
    LinesDrawer(surface, glob.BLACK, 0, cordY, 0, cordY + surf_text_cY, glob.left_line_size)
    LinesDrawer(surface, glob.BLACK, surf_text_cX, cordY, surf_text_cX, cordY + surf_text_cY, glob.right_line_size)
    LinesDrawer(surface, glob.BLACK, 0, cordY + glob.up_line_size // 2, surf_text_cX, cordY + glob.up_line_size // 2,
                glob.up_line_size)
    LinesDrawer(surface, glob.BLACK, 0, cordY + surf_text_cY, surf_text_cX, cordY + surf_text_cY, glob.down_line_size)

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
