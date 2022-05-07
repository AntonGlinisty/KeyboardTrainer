import pygame
import Globals as glob

def PrinterSearcher(event, letter):

    """
    Аргументы:
    :param event: Вводимый пользователем символ
    :param letter: Символ, который предстоит напечатать
    :return: Состояние ввода

    Описание: Функция проверяет правильность введенного пользователем символа
    """

    if event.key not in [pygame.K_LSHIFT, pygame.K_RSHIFT, pygame.K_TAB, pygame.K_CAPSLOCK, pygame.K_LCTRL,
            pygame.K_RCTRL, pygame.K_LALT, pygame.K_RALT, pygame.K_PRINTSCREEN] and ord(event.unicode) > glob.un_chec:
        return 'mistake'
    if pygame.key.get_mods() == glob.key_mod_u1 or pygame.key.get_mods() == glob.key_mod_u2:
        if BigLetChecker(event, letter) or BigSymbChecker(event, letter):
            return 'correct'
        elif event.key in [pygame.K_LSHIFT, pygame.K_RSHIFT, pygame.K_TAB, pygame.K_CAPSLOCK, pygame.K_LCTRL,
                           pygame.K_RCTRL, pygame.K_LALT, pygame.K_RALT]:
            return 'unknown'
        else:
            return 'mistake'
    if pygame.key.get_mods() == glob.key_mod_d1 or pygame.key.get_mods() == glob.key_mod_d2:
        if SmallLetChecker(event, letter) or SmallSymbChecker(event, letter):
            return 'correct'
        elif event.key in [pygame.K_LSHIFT, pygame.K_RSHIFT, pygame.K_TAB, pygame.K_CAPSLOCK, pygame.K_LCTRL,
                           pygame.K_RCTRL, pygame.K_LALT, pygame.K_RALT]:
            return 'unknown'
        else:
            return 'mistake'

def BigLetChecker(event, letter):

    """
    Аргументы:
    :param event: Вводимый пользователем символ
    :param letter: Символ, который предстоит напечатать
    :return: Состояние проверки

    Описание: Функция проверяет на правильность ввода заглавные буквы
    """

    if (event.key == pygame.K_q and letter == 'Q' or event.key == pygame.K_w and letter == 'W' or
            event.key == pygame.K_e and letter == 'E' or event.key == pygame.K_r and letter == 'R' or
            event.key == pygame.K_t and letter == 'T' or event.key == pygame.K_y and letter == 'Y' or
            event.key == pygame.K_u and letter == 'U' or event.key == pygame.K_i and letter == 'I' or
            event.key == pygame.K_o and letter == 'O' or event.key == pygame.K_p and letter == 'P' or
            event.key == pygame.K_a and letter == 'A' or event.key == pygame.K_s and letter == 'S' or
            event.key == pygame.K_d and letter == 'D' or event.key == pygame.K_f and letter == 'F' or
            event.key == pygame.K_g and letter == 'G' or event.key == pygame.K_h and letter == 'H' or
            event.key == pygame.K_j and letter == 'J' or event.key == pygame.K_k and letter == 'K' or
            event.key == pygame.K_l and letter == 'L' or event.key == pygame.K_z and letter == 'Z' or
            event.key == pygame.K_x and letter == 'X' or event.key == pygame.K_c and letter == 'C' or
            event.key == pygame.K_v and letter == 'V' or event.key == pygame.K_b and letter == 'B' or
            event.key == pygame.K_n and letter == 'N' or event.key == pygame.K_m and letter == 'M'):
        return True
    else:
        return False

def BigSymbChecker(event, letter):

    """
    Аргументы:
    :param event: Вводимый пользователем символ
    :param letter: Символ, который предстоит напечатать
    :return: Состояние проверки

    Описание: Функция проверяет на правильность ввода "заглавые" символы
    """

    if (event.key == pygame.K_SEMICOLON and letter == ':' or
            event.key == pygame.K_2 and letter == '@' or event.key == pygame.K_3 and letter == '#' or
            event.key == pygame.K_4 and letter == '$' or event.key == pygame.K_5 and letter == '%' or
            event.key == pygame.K_6 and letter == '^' or event.key == pygame.K_7 and letter == '&' or
            event.key == pygame.K_8 and letter == '*' or event.key == pygame.K_9 and letter == '(' or
            event.key == pygame.K_0 and letter == ')' or event.key == pygame.K_1 and letter == '!' or
            event.key == pygame.K_QUOTE and letter == '"' or
            event.key == pygame.K_SLASH and letter == '?' or
            event.key == pygame.K_MINUS and letter == '_' or
            event.key == pygame.K_COMMA and letter == '<' or
            event.key == pygame.K_SPACE and letter == 'Space' or
            event.key == pygame.K_RETURN and letter == 'Enter' or
            event.key == pygame.K_EQUALS and letter == '+' or
            event.key == pygame.K_PERIOD and letter == '>' or
            event.key == pygame.K_BACKSLASH and letter == '|' or
            event.key == pygame.K_BACKQUOTE and letter == '~' or
            event.key == pygame.K_LEFTBRACKET and letter == '{' or
            event.key == pygame.K_RIGHTBRACKET and letter == '}'):
            return True
    else:
        return False

def SmallLetChecker(event, letter):

    """
    Аргументы:
    :param event: Вводимый пользователем символ
    :param letter: Символ, который предстоит напечатать
    :return: Состояние проверки

    Описание: Функция проверяет на правильность ввода строчные буквы
    """

    if (event.key == pygame.K_q and letter == 'q' or event.key == pygame.K_w and letter == 'w' or
            event.key == pygame.K_e and letter == 'e' or event.key == pygame.K_r and letter == 'r' or
            event.key == pygame.K_t and letter == 't' or event.key == pygame.K_y and letter == 'y' or
            event.key == pygame.K_u and letter == 'u' or event.key == pygame.K_i and letter == 'i' or
            event.key == pygame.K_o and letter == 'o' or event.key == pygame.K_p and letter == 'p' or
            event.key == pygame.K_a and letter == 'a' or event.key == pygame.K_s and letter == 's' or
            event.key == pygame.K_d and letter == 'd' or event.key == pygame.K_f and letter == 'f' or
            event.key == pygame.K_g and letter == 'g' or event.key == pygame.K_h and letter == 'h' or
            event.key == pygame.K_j and letter == 'j' or event.key == pygame.K_k and letter == 'k' or
            event.key == pygame.K_l and letter == 'l' or event.key == pygame.K_z and letter == 'z' or
            event.key == pygame.K_x and letter == 'x' or event.key == pygame.K_c and letter == 'c' or
            event.key == pygame.K_v and letter == 'v' or event.key == pygame.K_b and letter == 'b' or
            event.key == pygame.K_n and letter == 'n' or event.key == pygame.K_m and letter == 'm'):
        return True
    else:
        return False

def SmallSymbChecker(event, letter):

    """
    Аргументы:
    :param event: Вводимый пользователем символ
    :param letter: Символ, который предстоит напечатать
    :return: Состояние проверки

    Описание: Функция проверяет на правильность ввода "строчные" символы
    """

    if (event.key == pygame.K_SEMICOLON and letter == ';' or
            event.key == pygame.K_2 and letter == '2' or event.key == pygame.K_3 and letter == '3' or
            event.key == pygame.K_4 and letter == '4' or event.key == pygame.K_5 and letter == '5' or
            event.key == pygame.K_6 and letter == '6' or event.key == pygame.K_7 and letter == '7' or
            event.key == pygame.K_8 and letter == '8' or event.key == pygame.K_9 and letter == '9' or
            event.key == pygame.K_0 and letter == '0' or event.key == pygame.K_1 and letter == '1' or
            event.key == pygame.K_MINUS and letter == '-' or
            event.key == pygame.K_QUOTE and letter == "'" or
            event.key == pygame.K_SPACE and letter == 'Space' or
            event.key == pygame.K_SLASH and letter == '/' or
            event.key == pygame.K_COMMA and letter == ',' or
            event.key == pygame.K_EQUALS and letter == '=' or
            event.key == pygame.K_PERIOD and letter == '.' or
            event.key == pygame.K_RETURN and letter == 'Enter' or
            event.key == pygame.K_BACKQUOTE and letter == '`' or
            event.key == pygame.K_BACKSLASH and letter == '\\' or
            event.key == pygame.K_LEFTBRACKET and letter == '[' or
            event.key == pygame.K_RIGHTBRACKET and letter == ']'):
            return True
    else:
        return False

def PersonInput(event, surface, listoftw, condition):

    """
    Аргументы:
    :param event: Вводимый пользователем символ
    :param surface: Поверхность, на которой будет печататься текст
    :param listoftw: Список размеров уже напечатанных букв для дальнейшего отступа
    :param condition: Состояние воода ('correct', 'mistake')

    Описание: Функция печатает пользовательский ввод в соответствующей области
    """

    if condition == 'correct':
        if condition == 'unknown' or condition == 'correct':
            letter = event.unicode
            L1 = pygame.font.SysFont('verdana', glob.ex_text_size)
            text1 = L1.render(letter, True, (glob.BLACK))
            surface.blit(text1, (glob.width + glob.indent1, glob.surf_info_cordy + glob.indent3))
            glob.width += text1.get_width()
            listoftw.append(text1.get_width())
    return listoftw