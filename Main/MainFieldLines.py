import pygame
import Globals as glob

def BordersDrawer(surface, surf_inf_cX, surf_inp_cX, surf_text_cX, surf_inf_cY, surf_inp_cY, surf_text_cY,
                  l_l_size, r_l_size, u_l_size, d_l_size):

    """
    Аргументы:
    :param surface: Поверхность, на которой будут отображаться границы других пов-тей
    :param surf_inf_cX: Ширина поверхности статистики
    :param surf_inp_cX: Ширина поверхности ввода
    :param surf_text_cX: Ширина поверхности текста
    :param surf_inf_cY: Высота поверхности статистики
    :param surf_inp_cY: Высота поверхности ввода
    :param surf_text_cY: Высота поверхности текста
    :param l_l_size: Размер левых линий
    :param r_l_size: Размер правых линий
    :param u_l_size: Размер верхних линий
    :param d_l_size: Размер нижних линий

    Описание: Функция рисует линии границы пов-тей(для статистики, ввода, текста и клавиатуры)
    """

    cordY = surf_inf_cY + surf_inp_cY
    LinesDrawer(surface, glob.BLACK, 0, 0, 0, surf_inf_cY, l_l_size)
    LinesDrawer(surface, glob.BLACK, surf_inf_cX, 0, surf_inf_cX, surf_inf_cY, r_l_size)
    LinesDrawer(surface, glob.BLACK, 0, u_l_size // 2, surf_inf_cX, u_l_size // 2, u_l_size)
    LinesDrawer(surface, glob.BLACK, 0, surf_inf_cY - d_l_size // 2 - 1, surf_inf_cX,
                surf_inf_cY - d_l_size // 2 - 1, d_l_size)
    LinesDrawer(surface, glob.RED, 0, surf_inf_cY, 0, cordY, l_l_size)
    LinesDrawer(surface, glob.RED, surf_inf_cX, surf_inf_cY, surf_inp_cX, cordY, r_l_size)
    LinesDrawer(surface, glob.RED, 0, surf_inf_cY + u_l_size // 2, surf_inp_cX, surf_inp_cY + u_l_size // 2, u_l_size)
    LinesDrawer(surface, glob.RED, 0, cordY - d_l_size // 2 - 1, surf_inp_cX, cordY - d_l_size // 2 - 1, d_l_size)
    LinesDrawer(surface, glob.BLACK, 0, cordY, 0, cordY + surf_text_cY, l_l_size)
    LinesDrawer(surface, glob.BLACK, surf_text_cX, cordY, surf_text_cX, cordY + surf_text_cY, r_l_size)
    LinesDrawer(surface, glob.BLACK, 0, cordY + u_l_size // 2, surf_text_cX, cordY + u_l_size // 2, u_l_size)
    LinesDrawer(surface, glob.BLACK, 0, cordY + surf_text_cY, surf_text_cX, cordY + surf_text_cY, d_l_size)

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
