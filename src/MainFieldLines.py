import pygame
from Globals import *

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
    LinesDrawer(surface, BLACK, 0, 0, 0, surf_inf_cY, left_line_size)
    LinesDrawer(surface, BLACK, surf_inf_cX, 0, surf_inf_cX, surf_inf_cY, right_line_size)
    LinesDrawer(surface, BLACK, 0, up_line_size // 2, surf_inf_cX, up_line_size // 2, up_line_size)
    LinesDrawer(surface, BLACK, 0, surf_inf_cY - down_line_size // 2 - 1, surf_inf_cX,
                surf_inf_cY - down_line_size // 2 - 1, down_line_size)
    LinesDrawer(surface, RED, 0, surf_inf_cY, 0, cordY, left_line_size)
    LinesDrawer(surface, RED, surf_inf_cX, surf_inf_cY, surf_inp_cX, cordY, right_line_size)
    LinesDrawer(surface, RED, 0, surf_inf_cY + up_line_size // 2, surf_inp_cX, surf_inp_cY + up_line_size // 2,
                up_line_size)
    LinesDrawer(surface, RED, 0, cordY - down_line_size // 2 - 1, surf_inp_cX, cordY - down_line_size // 2 - 1,
                down_line_size)
    LinesDrawer(surface, BLACK, 0, cordY, 0, cordY + surf_text_cY, left_line_size)
    LinesDrawer(surface, BLACK, surf_text_cX, cordY, surf_text_cX, cordY + surf_text_cY, right_line_size)
    LinesDrawer(surface, BLACK, 0, cordY + up_line_size // 2, surf_text_cX, cordY + up_line_size // 2, up_line_size)
    LinesDrawer(surface, BLACK, 0, cordY + surf_text_cY, surf_text_cX, cordY + surf_text_cY, down_line_size)

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
