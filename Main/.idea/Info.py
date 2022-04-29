import pygame

from datetime import datetime

def Info(time, surface, WHITE, surf_info_cordx, surf_info_cordy, word_counter, condition_counter, indent1,
         indent4, mistakes, marker4, a, BLACK, surface_xcord):

    """func displays all statistics in the corresponding area"""

    pygame.draw.rect(surface, WHITE, [0 + 3, 3, surf_info_cordx - 6, surf_info_cordy - 6])
    L1 = pygame.font.SysFont('calibri', 20)
    if marker4:
        f = open('stats.txt', 'r+')
        for lines in f:
            if len(a) >= 3:
                break
            if len(a) < 2:
                a.append(lines[:-1])
            elif len(a) == 2:
                a.append(lines)
        f.close()
        marker4 = False
    text5 = L1.render('Last try results : ', True, (BLACK))
    surface.blit(text5, (surface_xcord // 18 * 10, indent1 + 15))
    for l_cou in range(len(a)):
        text = L1.render(a[l_cou], True, (BLACK))
        surface.blit(text, (surface_xcord // 30 * 21.5, indent1 + l_cou * 17))

    text1 = L1.render('Time : ' + str(datetime.now() - time), True, (BLACK))
    surface.blit(text1, (0 + indent4 // 2, indent1))
    if (datetime.now() - time).seconds == 0:
        WPM = 0
        LPM = 0
    else:
        WPM = (word_counter / (datetime.now() - time).seconds * 60)
        LPM = (condition_counter / ((datetime.now() - time).microseconds / 1000000 +
                                    (datetime.now() - time).seconds)) * 60
    text2 = L1.render('Words per minute : ' + str(float("{0:.3f}".format(WPM))), True, (BLACK))
    surface.blit(text2, (0 + indent4 // 2, indent1 * 7))
    text3 = L1.render('Symbols per minute : ' + str(float("{0:.3f}".format(LPM))), True, (BLACK))
    surface.blit(text3, (surf_info_cordx // 4 + indent4, indent1))
    text4 = L1.render('Mistakes : ' + str(mistakes), True, (BLACK))
    surface.blit(text4, (surf_info_cordx // 4 + indent4, indent1 * 7))
    f = open('stats.txt', 'w+')
    f.write('Words per minute : ' + str(float("{0:.3f}".format(WPM))) + '\n')
    f.write('Symbols per minute : ' + str(float("{0:.3f}".format(LPM))) + '\n')
    f.write('Mistakes : ' + str(mistakes))
    f.close()
    return a, marker4