import pygame
import Globals as glob
from datetime import datetime

def Info(time, surface, word_counter, condition_counter, mistakes, timelist):

    """
    Аргументы:
    :param time: Время от начала запуска
    :param surface: Поверхность, на которой отображается статитика
    :param word_counter: Количество набранных слов
    :param condition_counter: Количество правильно набранных символов
    :param mistakes: Количество неправильно набранных символов
    :param timelist: Список, в который записываются результаты предыдущей попытки
    :return: Модифицированный список, параметр доступа

    Описание: Функция выводит на экран актуальную статистику попытки, а также статистику прошлой попытки
    """

    pygame.draw.rect(surface, glob.WHITE, [glob.stats_area_ind_c, glob.stats_area_ind_c,
                            glob.surf_info_cordx - glob.stats_area_ind_s, glob.surf_info_cordy - glob.stats_area_ind_s])
    L1 = pygame.font.SysFont('calibri', glob.stats1_txt_size)
    if glob.marker4:
        TimeList(timelist, glob.stats_lines_count)
        glob.marker4 = False
    text5 = L1.render('Last try results : ', True, (glob.BLACK))
    surface.blit(text5, (glob.surface_xcord // glob.st_ltry_txt_kX * glob.st_ltry_txt_mX, glob.indent1 +
                         glob.st_ltry_txt_kY))
    for l_cou in range(len(timelist)):
        text = L1.render(timelist[l_cou], True, (glob.BLACK))
        surface.blit(text, (glob.surface_xcord // glob.st_ltry_kX * glob.st_ltry_mX, glob.indent1 + l_cou *
                            glob.st_ltry_kY))
    text1 = L1.render('Time : ' + str(datetime.now() - time), True, (glob.BLACK))
    surface.blit(text1, (glob.indent4 // glob.st_time_koef, glob.indent1))
    if (datetime.now() - time).seconds == 0:
        WPM = LPM = 0
    else:
        WPM = (word_counter / (datetime.now() - time).seconds * glob.seconds_in_min)
        LPM = (condition_counter / ((datetime.now() - time).microseconds / glob.micros_in_seconds +
                                    (datetime.now() - time).seconds)) * glob.seconds_in_min
    text2 = L1.render('Words per minute : ' + str(float("{0:.3f}".format(WPM))), True, (glob.BLACK))
    surface.blit(text2, (glob.indent4 // glob.st_time_koef, glob.indent1 * glob.st_mist_koef))
    text3 = L1.render('Symbols per minute : ' + str(float("{0:.3f}".format(LPM))), True, (glob.BLACK))
    surface.blit(text3, (glob.surf_info_cordx // glob.st_mist_ind + glob.indent4, glob.indent1))
    text4 = L1.render('Mistakes : ' + str(mistakes), True, (glob.BLACK))
    surface.blit(text4, (glob.surf_info_cordx // glob.st_mist_ind + glob.indent4, glob.indent1 * glob.st_mist_koef))
    StatsKeeper(WPM, LPM, mistakes)
    return timelist

def TimeList(timelist, number):

    """
    Аргументы:
    :param timelist: Список, в который записываются результаты предыдущей попытки
    :param number: Количество полей со статистикой, необходимое для получения
    :return: Модифицированный список

    Описание: Функция получает статистику предыдущей пыпытки из файла
    """

    f = open('stats.txt', 'r+')
    for lines in f:
        if len(timelist) > number:
            break
        if len(timelist) < number:
            timelist.append(lines[:-1])
        elif len(timelist) == number:
            timelist.append(lines)
    f.close()
    return timelist

def StatsKeeper(WPM, LPM, mistakes):

    """
    Аргументы:
    :param WPM: Words per minute - количество слов в минуту
    :param LPM: Letters per minute - количество символов в минуту
    :param mistakes: Количество ошибок

    Описание: Функция записывает статистику попытки в файл
    """

    f = open('stats.txt', 'w+')
    f.write('Words per minute : ' + str(float("{0:.3f}".format(WPM))) + '\n')
    f.write('Symbols per minute : ' + str(float("{0:.3f}".format(LPM))) + '\n')
    f.write('Mistakes : ' + str(mistakes))
    f.close()