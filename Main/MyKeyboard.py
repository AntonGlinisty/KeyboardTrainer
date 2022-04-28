import pygame


def LineDrawer(surface, surface_xcord, surface_ycord, surf_xcord, surf_ycord, BLACK, kwc, khc, surf_info_cordy,
               surf_input_cordy, surf_text_cordy):

    """func draws lines for keyboard frame"""

    for linenumb in range(4):
        pygame.draw.line(surface, BLACK, [0, surface_ycord - (surf_ycord // khc) * (linenumb + 1)],
                         [surface_xcord, surface_ycord - (surf_ycord // khc) * (linenumb + 1)], 1)
    for linenumb in range(13):
        pygame.draw.line(surface, BLACK, [surf_xcord // kwc * (linenumb + 1), surface_ycord - surf_ycord],
                         [surf_xcord // kwc * (linenumb + 1), surface_ycord - surf_ycord // 5 * 4], 1)
    for linenumb in range(13):
        pygame.draw.line(surface, BLACK, [surf_xcord // kwc * 0.5 + surf_xcord // kwc * (linenumb + 1),
                    surface_ycord - surf_ycord // khc * 4], [surf_xcord // kwc * 0.5 + surf_xcord // kwc *
                                                             (linenumb + 1), surface_ycord - surf_ycord // khc * 3], 1)
    for linenumb in range(12):
        pygame.draw.line(surface, BLACK, [surf_xcord // kwc + surf_xcord // kwc * (linenumb + 1),
                    surface_ycord - surf_ycord // khc * 3], [surf_xcord // kwc + surf_xcord // kwc * (linenumb + 1),
                                                                        surface_ycord - surf_ycord // khc * 2], 1)
    for linenumb in range(11):
        pygame.draw.line(surface, BLACK, [surf_xcord // kwc * 1.5 + surf_xcord // kwc * (linenumb + 1),
                        surface_ycord - surf_ycord // khc * 2], [surf_xcord // kwc * 1.5 + surf_xcord // kwc *
                                                                 (linenumb + 1), surface_ycord - surf_ycord // khc * 1], 1)
    pygame.draw.line(surface, BLACK, [surf_xcord // kwc * 5, surface_ycord - surf_ycord // khc],
                     [surf_xcord // kwc * 5,surface_ycord])
    pygame.draw.line(surface, BLACK, [surf_xcord // kwc * 10, surface_ycord - surf_ycord // khc],
                     [surf_xcord // kwc * 10, surface_ycord])
    for linenumb in range(2):
        pygame.draw.line(surface, BLACK, [surf_xcord // 3 // 3 * (linenumb + 1), surface_ycord - surf_ycord // 5],
                         [surf_xcord // 3 // 3 * (linenumb + 1), surface_ycord], 1)
        pygame.draw.line(surface, BLACK, [surface_xcord - surf_xcord // 9 * (linenumb + 1), surface_ycord - surf_ycord // 5],
                         [surface_xcord - surf_xcord // 3 // 3 * (linenumb + 1), surface_ycord], 1)
    pygame.draw.rect(surface, BLACK, (0, surf_info_cordy + surf_input_cordy + surf_text_cordy,
                                      surf_xcord, surf_ycord), 3)

def DictOfSymbols(BLACK):

    """func returns a dict with keyboard letters in values"""

    L1 = pygame.font.SysFont('arial', 25)
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
        'text93': L1.render('Tab', True, (BLACK)),
        'text94': L1.render('Caps Lock', True, (BLACK)),
        'text95': L1.render('Shift', True, (BLACK)),
        'text96': L1.render('Ctrl', True, (BLACK)),
        'text97': L1.render('Alt', True, (BLACK)),
        'text98': L1.render('AltGr', True, (BLACK)),
        'text99': L1.render('Ctrl', True, (BLACK)),
        'text100': L1.render('Shift', True, (BLACK)),
        'text101': L1.render('Enter', True, (BLACK)),
        'text102': L1.render('Back', True, (BLACK)),
        'text103': L1.render('|', True, (BLACK)), 'text104': L1.render('\\', True, (BLACK)),
        'text105': L1.render('Space', True, (BLACK)),
    }
    return dict

def RusSymbolsDrawer(dict, surf_xcord, surface_ycord, surf_ycord, indent1, indent2, kwc, khc, surface):

    """func draws letters in right places on the keyboard"""

    for letnumb in range(12):
        surface.blit(dict['text' + str((letnumb + 1) * 2 - 1)], (surf_xcord // kwc * 0.5 + surf_xcord // kwc *
                                            (letnumb + 1) + indent1, surface_ycord - surf_ycord // khc * 4 + indent1))
        surface.blit(dict['text' + str((letnumb + 1) * 2)], (surf_xcord // kwc * 1.5 + surf_xcord // kwc *
                                       (letnumb + 1) - indent2, surface_ycord - surf_ycord // khc * 3 - indent2 * 2))
    for letnumb in range(11):
        surface.blit(dict['text' + str((12 + letnumb + 1) * 2 - 1)], (surf_xcord // kwc * 1 + surf_xcord // kwc *
                                            (letnumb + 1) + indent1, surface_ycord - surf_ycord // khc * 3 + indent1))
        surface.blit(dict['text' + str((12 + letnumb + 1) * 2)], (surf_xcord // kwc * 2 + surf_xcord // kwc *
                                        (letnumb + 1) - indent2, surface_ycord - surf_ycord // khc * 2 - indent2 * 2))
    for letnumb in range(10):
        surface.blit(dict['text' + str((23 + letnumb + 1) * 2 - 1)], (surf_xcord // kwc * 1.5 + surf_xcord //
                                        kwc * (letnumb + 1) + indent1, surface_ycord - surf_ycord // khc * 2 + indent1))
        surface.blit(dict['text' + str((23 + letnumb + 1) * 2)], (surf_xcord // kwc * 2.5 + surf_xcord //
                                    kwc * (letnumb + 1) - indent2, surface_ycord - surf_ycord // khc * 1 - indent2 * 2))
    for letnumb in range(13):
        surface.blit(dict['text' + str((33 + letnumb + 1) * 2 - 1)], (surf_xcord // kwc * (-1) + surf_xcord //
                                        kwc * (letnumb + 1) + indent1, surface_ycord - surf_ycord // khc * 5 + indent1))
        surface.blit(dict['text' + str((33 + letnumb + 1) * 2)], (surf_xcord // kwc * 0 + surf_xcord //
                                    kwc * (letnumb + 1) - indent2, surface_ycord - surf_ycord // khc * 4 - indent2 * 2))
    surface.blit(dict['text' + str(93)], (surf_xcord / 100 * 3.5, surface_ycord - surf_ycord // khc * 4 + 18))
    surface.blit(dict['text' + str(94)], (surf_xcord / 60 * 1.1, surface_ycord - surf_ycord // khc * 3 + 18))
    surface.blit(dict['text' + str(95)], (surf_xcord / 18 * 1.1, surface_ycord - surf_ycord // khc * 2 + 18))
    surface.blit(dict['text' + str(96)], (surf_xcord / 25, surface_ycord - surf_ycord // khc * 1 + 15))
    surface.blit(dict['text' + str(97)], (surf_xcord / 30 * 7.9, surface_ycord - surf_ycord // khc * 1 + 15))
    surface.blit(dict['text' + str(98)], (surf_xcord / 30 * 20.9, surface_ycord - surf_ycord // khc * 1 + 15))
    surface.blit(dict['text' + str(99)], (surf_xcord // 30 * 27.8, surface_ycord - surf_ycord // khc * 1 + 15))
    surface.blit(dict['text' + str(100)], (surf_xcord // kwc * 13.4, surface_ycord - surf_ycord // khc * 2 + 18))
    surface.blit(dict['text' + str(101)], (surf_xcord // kwc * 13.6, surface_ycord - surf_ycord // khc * 3 + 18))
    surface.blit(dict['text' + str(102)], (surf_xcord // kwc * 13.6, surface_ycord - surf_ycord // khc * 5 + 18))
    surface.blit(dict['text' + str(103)], (surf_xcord // kwc * 13.5 + indent1, surface_ycord - surf_ycord //
                                           khc * 4 + indent1))
    surface.blit(dict['text' + str(104)], (surf_xcord - indent2, surface_ycord - surf_ycord // khc * 3 - indent2 * 2))
    surface.blit(dict['text' + str(105)], (surf_xcord / kwc * 6.9, surface_ycord - surf_ycord // khc * 1 + 15))

def KeyboardDrawer(surface, surface_xcord, surface_ycord, surf_xcord, surf_ycord, BLACK, indent1, indent2,
                   keys_width_counter, keys_height_counter, surf_info_cordy, surf_input_cordy, surf_text_cordy):

    """func draws all the keyboard completely"""

    LineDrawer(surface, surface_xcord, surface_ycord, surf_xcord, surf_ycord, BLACK,
               keys_width_counter, keys_height_counter, surf_info_cordy, surf_input_cordy, surf_text_cordy)
    dict = DictOfSymbols(BLACK)
    RusSymbolsDrawer(dict, surf_xcord, surface_ycord, surf_ycord, indent1, indent2,
                     keys_width_counter, keys_height_counter, surface)