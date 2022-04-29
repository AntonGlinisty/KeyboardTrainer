import pygame

def ListOfSymbols(text):

    """func reads the text from a file"""

    list = []
    with open(text + '.txt', 'r+', encoding='utf_8') as file:
        for line in file.readlines():
            list += line.split(' ')
            list[len(list) - 1] = list[len(list) - 1][:-1]
            list.append('Enter')
    list = list[:-1]
    return list

def TextViewer(list, BLACK, surface, surf_text_cordx, surf_info_cordy, surf_input_cordy,
               surf_text_cordy, indent1, word_counter, WHITE, string_scroller, textsize):

    """func puts part of the text on the screen"""

    pygame.draw.rect(surface, WHITE, [0 + 3, surf_info_cordy + surf_input_cordy + 3,
                                      surf_text_cordx - 6, surf_text_cordy - 6])
    L1 = pygame.font.SysFont('verdana', textsize)
    width = 0
    for line_counter in range(5):
        length = 0
        for counter in range(word_counter, len(list)):
            if length >= string_scroller:
                width = 0
                break
            length += len(list[word_counter])
            for letter in list[word_counter]:
                text1 = L1.render(letter, True, (BLACK))
                surface.blit(text1, (width + indent1, surf_info_cordy + surf_input_cordy +
                                     surf_text_cordy / 5 * line_counter + 5))
                width += text1.get_width()
            text1 = L1.render(' ', True, (BLACK))
            surface.blit(text1, (width + indent1, surf_info_cordy + surf_input_cordy +
                                 surf_text_cordy / 5 * line_counter + 5))
            width += text1.get_width()
            word_counter += 1
