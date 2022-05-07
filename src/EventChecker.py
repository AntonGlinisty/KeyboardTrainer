import Globals as glob
import pygame
import os

def ResolutionChanger(event):

    """
    Аргументы:
    :param event: Событие мыши

    Описание: Функция меняет разрешение экрана при нажатии пользователем на соответствующую картинку
    """

    if (glob.surface_cordx / glob.kong_x_dev < event.pos[
        0] < glob.surface_cordx / glob.kong_x_dev + glob.surface_cordy / glob.kong_x_devs
            and glob.surface_cordy / glob.kong1_y_devs < event.pos[
                1] < glob.surface_cordy / glob.kong1_y_devs + glob.surface_cordy /
            glob.kong_x_devs and glob.marker1 == False):
        glob.surface_xcord = glob.res1_x
        glob.surface_ycord = glob.res1_y
        glob.string_scroller = glob.scrol1
    if (glob.surface_cordx / glob.kong_x_dev < event.pos[
        0] < glob.surface_cordx / glob.kong_x_dev + glob.surface_cordy / glob.kong_x_devs
            and glob.surface_cordy / glob.kong2_y_devs < event.pos[
                1] < glob.surface_cordy / glob.kong2_y_devs + glob.surface_cordy /
            glob.kong_x_devs and glob.marker1 == False):
        glob.surface_xcord = glob.res2_x
        glob.surface_ycord = glob.res2_y
        glob.string_scroller = glob.scrol2
    if (glob.surface_cordx / glob.kong_x_dev < event.pos[
        0] < glob.surface_cordx / glob.kong_x_dev + glob.surface_cordy / glob.kong_x_devs
            and glob.surface_cordy / glob.kong3_y_devs < event.pos[
                1] < glob.surface_cordy / glob.kong3_y_devs + glob.surface_cordy /
            glob.kong_x_devs and glob.marker1 == False):
        glob.surface_xcord = glob.res3_x
        glob.surface_ycord = glob.res3_y
        glob.string_scroller = glob.scrol3

def TextChanger(event):

    """
    Аргументы:
    :param event: Событие мыши

    Описание: Функция меняет текст при нажатии пользователем на соответствующую картинку
    """

    if (glob.surface_cordx / glob.mon_x_dev < event.pos[
        0] < glob.surface_cordx / glob.mon_x_dev + glob.surface_cordy / glob.mon1_y_dev1
            and glob.surface_cordy / glob.mon1_y_devs < event.pos[
                1] < glob.surface_cordy / glob.mon1_y_devs + glob.surface_cordy /
            glob.mon1_y_dev1 and glob.marker1 == False):
        glob.filewithtext = 'text1'
    if (glob.surface_cordx / glob.mon_x_dev < event.pos[
        0] < glob.surface_cordx / glob.mon_x_dev + glob.surface_cordy / glob.mon1_y_dev1
            and glob.surface_cordy / glob.mon2_y_dev < event.pos[
                1] < glob.surface_cordy / glob.mon2_y_dev + glob.surface_cordy /
            glob.mon1_y_dev1 and glob.marker1 == False):
        glob.filewithtext = 'text2'
    if (glob.surface_cordx / glob.mon_x_dev < event.pos[
        0] < glob.surface_cordx / glob.mon_x_dev + glob.surface_cordy / glob.mon1_y_dev1
            and glob.surface_cordy / glob.mon3_y_devs < event.pos[
                1] < glob.surface_cordy / glob.mon3_y_devs + glob.surface_cordy /
            glob.mon1_y_dev1 and glob.marker1 == False):
        glob.filewithtext = 'text3'

def SettingsChecker(surface, event, settings, fon, text, futur, mon2, mon3, mon4, kong1, kong3, kong4, text10, text11):

    """
    Аргументы: Картинки, отвечающие за смену текста, разрешения экрана, фон окна настроек

    Описание: Функция отслеживает нажатие пользователем иконки настроек
    """

    if glob.set_ev_d < event.pos[1] < glob.set_ev_u and glob.set_ev_d < event.pos[0] < glob.set_ev_u:
        if glob.marker1:
            surface.blit(futur, (glob.sf_spawn, glob.sf_spawn))
            surface.blit(mon2, (glob.surface_cordx / glob.mon_x_dev, glob.surface_cordy / glob.mon2_y_dev))
            surface.blit(mon3, (glob.surface_cordx / glob.mon_x_dev, glob.surface_cordy / glob.mon3_y_dev))
            surface.blit(mon4, (glob.surface_cordx / glob.mon_x_dev, glob.surface_cordy / glob.mon4_y_dev))
            surface.blit(text10, (glob.surface_cordx / glob.chootxt_x, glob.surface_cordy / glob.chootxt_y))
            surface.blit(kong1, (glob.surface_cordx / glob.kong_x_dev, glob.surface_cordy / glob.kong1_y_dev))
            surface.blit(kong4, (glob.surface_cordx / glob.kong_x_dev, glob.surface_cordy / glob.kong4_y_dev))
            surface.blit(kong3, (glob.surface_cordx / glob.kong_x_dev, glob.surface_cordy / glob.kong3_y_dev))
            surface.blit(text11, (glob.surface_cordx / glob.choores_x, glob.surface_cordy / glob.choores_y))
            glob.marker1 = False
        else:
            surface.blit(fon, (glob.sf_spawn, glob.sf_spawn))
            surface.blit(text,
                         (glob.surface_cordx // glob.strt_x_d3 * glob.strt_y_m2, glob.surface_cordy // glob.strt_x_d1))
            glob.marker1 = True
        surface.blit(settings, (glob.set_ev_d, glob.set_ev_d))

def StartChecker(event):

    """
   Аргументы:
   :param event: Событие мыши

   Описание: Функция отслеживает нажатие пользователем иконки старта и запускает тренажер
   """

    if ((event.pos[0] - glob.surface_cordx // glob.strt_x_d1) * (event.pos[0] - glob.surface_cordx // glob.strt_x_d1) +
        (event.pos[1] - glob.surface_cordy // glob.strt_x_d1) * (event.pos[1] - glob.surface_cordy // glob.strt_x_d1) <
        (glob.surface_cordx // glob.strt_x_d2 * glob.surface_cordx // glob.strt_x_d2)) and event.pos[
        1] < glob.surface_cordy // \
            glob.strt_y_d1 * glob.strt_y_m1 and glob.marker1 == True:
        glob.running = False
        glob.marker6 = False

def PicsInitializer(surface, img_folder):

    """
    Аргументы:
    :param surface: Основная поверхность
    :param img_folder: Папка с изображениями
    :return: Поверхности картинок, отвечающих за смену текста и разрешения, фоны

    Описание: Функция генерирует поверхности фонов главного меню, картинок, отвечающих за смену текста и разрешения,
    картинку настроек, отрисовывает их на главной поверхности и возвращает
    """

    fon = pygame.image.load(os.path.join(img_folder, 'fon2.jpg'))
    fon = pygame.transform.scale(fon, (glob.surface_cordx, glob.surface_cordy))
    surface.blit(fon, (glob.sf_spawn, glob.sf_spawn))
    L1 = pygame.font.SysFont('calibri', glob.surface_cordx // glob.l1_dev + glob.l1_ind)
    text = L1.render('KLICK HERE', True, (glob.BLACK))
    surface.blit(text, (glob.surface_cordx // glob.strt_x_d3 * glob.strt_y_m2, glob.surface_cordy // glob.l_s_dev))
    settings = pygame.image.load(os.path.join(img_folder, 'pngwing.com.png'))
    settings = pygame.transform.scale(settings, (glob.set_ev_u - glob.set_ev_d, glob.set_ev_u - glob.set_ev_d))
    surface.blit(settings, (glob.set_ev_d, glob.set_ev_d))
    futur = pygame.image.load(os.path.join(img_folder, 'palms.jpg!d'))
    futur = pygame.transform.scale(futur, (glob.surface_cordx, glob.surface_cordy))
    mon2 = pygame.image.load(os.path.join(img_folder, 'mon2.png'))
    mon2 = pygame.transform.scale(mon2, (glob.surface_cordy / glob.mon_dev, glob.surface_cordy / glob.mon_dev))
    mon3 = pygame.image.load(os.path.join(img_folder, 'mon3.png'))
    mon3 = pygame.transform.scale(mon3, (glob.surface_cordy / glob.mon_dev, glob.surface_cordy / glob.mon_dev))
    mon4 = pygame.image.load(os.path.join(img_folder, 'mon4.png'))
    mon4 = pygame.transform.scale(mon4, (glob.surface_cordy / glob.mon_dev, glob.surface_cordy / glob.mon_dev))
    L3 = pygame.font.SysFont('calibri', glob.l3_x_ind + glob.surface_cordx // glob.l3_x_ind_dev)
    L4 = pygame.font.SysFont('calibri', glob.l4_x_ind + glob.surface_cordx // glob.l4_x_ind_dev)
    text10 = L3.render('Choose text:', True, (glob.BLACK))
    text11 = L4.render('Choose resolution:', True, (glob.BLACK))
    kong1 = pygame.image.load(os.path.join(img_folder, 'kong1.png'))
    kong1 = pygame.transform.scale(kong1, (glob.surface_cordy / glob.kong_dev, glob.surface_cordy / glob.kong_dev))
    kong4 = pygame.image.load(os.path.join(img_folder, 'kong4.png'))
    kong4 = pygame.transform.scale(kong4, (glob.surface_cordy / glob.kong_dev, glob.surface_cordy / glob.kong_dev))
    kong3 = pygame.image.load(os.path.join(img_folder, 'kong3.png'))
    kong3 = pygame.transform.scale(kong3, (glob.surface_cordy / glob.kong_dev, glob.surface_cordy / glob.kong_dev))
    return settings, kong1, kong3, kong4, mon2, mon3, mon4, fon, futur, text, text10, text11

def SurfsInit():

    """
    Описание: Функция инициализирует вспомогательные поверхности (для ввода, текста, статистики) и их размеры в
    соответствии с выбранным пользователем разрешением экрана
    """
    glob.surf_xcord = glob.surface_xcord
    glob.surf_info_cordx = glob.surface_xcord
    glob.surf_input_cordx = glob.surface_xcord
    glob.surf_text_cordx = glob.surface_xcord
    glob.surf_text_cordy = glob.surface_ycord - glob.surf_input_cordy - glob.surf_info_cordy - glob.surf_ycord
    surface = pygame.display.set_mode((glob.surface_xcord, glob.surface_ycord))
    surf_info = pygame.Surface((glob.surf_info_cordx, glob.surf_ycord))
    surf_input = pygame.Surface((glob.surf_input_cordx, glob.surf_input_cordy))
    surf_text = pygame.Surface((glob.surf_text_cordx, glob.surf_text_cordy))
    surf = pygame.Surface((glob.surf_xcord, glob.surf_ycord))
    surf_info.fill(glob.WHITE)
    surf_input.fill(glob.WHITE)
    surf_text.fill(glob.WHITE)
    surf.fill(glob.WHITE)
    glob.running = True
    surface.blit(surf, (0, glob.surface_ycord - glob.surf_ycord))
    surface.blit(surf_info, (0, 0))
    surface.blit(surf_input, (0, glob.surf_info_cordy))
    surface.blit(surf_text, (0, glob.surf_input_cordy + glob.surf_info_cordy))
    glob.indent4 = glob.surf_input_cordx / glob.ind4dev
    return surface, surf_info, surf_input, surf_text, surf