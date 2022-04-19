import pygame

def DictOfCords(surface_ycord, surf_xcord, surf_ycord):
    dict = {
        'Q': (surf_xcord // 15 * 0.5 + surf_xcord // 15 * 1, surface_ycord - surf_ycord // 5 * 4,
              surf_xcord // 15, surf_ycord // 5),
        'q': (surf_xcord // 15 * 0.5 + surf_xcord // 15 * 1, surface_ycord - surf_ycord // 5 * 4,
              surf_xcord // 15, surf_ycord // 5),
        'W': (surf_xcord // 15 * 0.5 + surf_xcord // 15 * 2, surface_ycord - surf_ycord // 5 * 4,
              surf_xcord // 15, surf_ycord // 5),
        'w': (surf_xcord // 15 * 0.5 + surf_xcord // 15 * 2, surface_ycord - surf_ycord // 5 * 4,
              surf_xcord // 15, surf_ycord // 5),
        'E': (surf_xcord // 15 * 0.5 + surf_xcord // 15 * 3, surface_ycord - surf_ycord // 5 * 4,
              surf_xcord // 15, surf_ycord // 5),
        'e': (surf_xcord // 15 * 0.5 + surf_xcord // 15 * 3, surface_ycord - surf_ycord // 5 * 4,
              surf_xcord // 15, surf_ycord // 5),
        'R': (surf_xcord // 15 * 0.5 + surf_xcord // 15 * 4, surface_ycord - surf_ycord // 5 * 4,
              surf_xcord // 15, surf_ycord // 5),
        'r': (surf_xcord // 15 * 0.5 + surf_xcord // 15 * 4, surface_ycord - surf_ycord // 5 * 4,
              surf_xcord // 15, surf_ycord // 5),
        'T': (surf_xcord // 15 * 0.5 + surf_xcord // 15 * 5, surface_ycord - surf_ycord // 5 * 4,
              surf_xcord // 15, surf_ycord // 5),
        't': (surf_xcord // 15 * 0.5 + surf_xcord // 15 * 5, surface_ycord - surf_ycord // 5 * 4,
              surf_xcord // 15, surf_ycord // 5),
        'Y': (surf_xcord // 15 * 0.5 + surf_xcord // 15 * 6, surface_ycord - surf_ycord // 5 * 4,
              surf_xcord // 15, surf_ycord // 5),
        'y': (surf_xcord // 15 * 0.5 + surf_xcord // 15 * 6, surface_ycord - surf_ycord // 5 * 4,
              surf_xcord // 15, surf_ycord // 5),
        'U': (surf_xcord // 15 * 0.5 + surf_xcord // 15 * 7, surface_ycord - surf_ycord // 5 * 4,
              surf_xcord // 15, surf_ycord // 5),
        'u': (surf_xcord // 15 * 0.5 + surf_xcord // 15 * 7, surface_ycord - surf_ycord // 5 * 4,
              surf_xcord // 15, surf_ycord // 5),
        'I': (surf_xcord // 15 * 0.5 + surf_xcord // 15 * 8, surface_ycord - surf_ycord // 5 * 4,
              surf_xcord // 15, surf_ycord // 5),
        'i': (surf_xcord // 15 * 0.5 + surf_xcord // 15 * 8, surface_ycord - surf_ycord // 5 * 4,
              surf_xcord // 15, surf_ycord // 5),
        'O': (surf_xcord // 15 * 0.5 + surf_xcord // 15 * 9, surface_ycord - surf_ycord // 5 * 4,
              surf_xcord // 15, surf_ycord // 5),
        'o': (surf_xcord // 15 * 0.5 + surf_xcord // 15 * 9, surface_ycord - surf_ycord // 5 * 4,
              surf_xcord // 15, surf_ycord // 5),
        'P': (surf_xcord // 15 * 0.5 + surf_xcord // 15 * 10, surface_ycord - surf_ycord // 5 * 4,
              surf_xcord // 15, surf_ycord // 5),
        'p': (surf_xcord // 15 * 0.5 + surf_xcord // 15 * 10, surface_ycord - surf_ycord // 5 * 4,
              surf_xcord // 15, surf_ycord // 5),
        '{': (surf_xcord // 15 * 0.5 + surf_xcord // 15 * 11, surface_ycord - surf_ycord // 5 * 4,
              surf_xcord // 15, surf_ycord // 5),
        '[': (surf_xcord // 15 * 0.5 + surf_xcord // 15 * 11, surface_ycord - surf_ycord // 5 * 4,
              surf_xcord // 15, surf_ycord // 5),
        '}': (surf_xcord // 15 * 0.5 + surf_xcord // 15 * 12, surface_ycord - surf_ycord // 5 * 4,
              surf_xcord // 15, surf_ycord // 5),
        ']': (surf_xcord // 15 * 0.5 + surf_xcord // 15 * 12, surface_ycord - surf_ycord // 5 * 4,
              surf_xcord // 15, surf_ycord // 5),
        'A': (surf_xcord // 15 * 1 + surf_xcord // 15 * 1, surface_ycord - surf_ycord // 5 * 3,
              surf_xcord // 15, surf_ycord // 5),
        'a': (surf_xcord // 15 * 1 + surf_xcord // 15 * 1, surface_ycord - surf_ycord // 5 * 3,
              surf_xcord // 15, surf_ycord // 5),
        'S': (surf_xcord // 15 * 1 + surf_xcord // 15 * 2, surface_ycord - surf_ycord // 5 * 3,
              surf_xcord // 15, surf_ycord // 5),
        's': (surf_xcord // 15 * 1 + surf_xcord // 15 * 2, surface_ycord - surf_ycord // 5 * 3,
              surf_xcord // 15, surf_ycord // 5),
        'D': (surf_xcord // 15 * 1 + surf_xcord // 15 * 3, surface_ycord - surf_ycord // 5 * 3,
              surf_xcord // 15, surf_ycord // 5),
        'd': (surf_xcord // 15 * 1 + surf_xcord // 15 * 3, surface_ycord - surf_ycord // 5 * 3,
              surf_xcord // 15, surf_ycord // 5),
        'F': (surf_xcord // 15 * 1 + surf_xcord // 15 * 4, surface_ycord - surf_ycord // 5 * 3,
              surf_xcord // 15, surf_ycord // 5),
        'f': (surf_xcord // 15 * 1 + surf_xcord // 15 * 4, surface_ycord - surf_ycord // 5 * 3,
              surf_xcord // 15, surf_ycord // 5),
        'G': (surf_xcord // 15 * 1 + surf_xcord // 15 * 5, surface_ycord - surf_ycord // 5 * 3,
              surf_xcord // 15, surf_ycord // 5),
        'g': (surf_xcord // 15 * 1 + surf_xcord // 15 * 5, surface_ycord - surf_ycord // 5 * 3,
              surf_xcord // 15, surf_ycord // 5),
        'H': (surf_xcord // 15 * 1 + surf_xcord // 15 * 6, surface_ycord - surf_ycord // 5 * 3,
              surf_xcord // 15, surf_ycord // 5),
        'h': (surf_xcord // 15 * 1 + surf_xcord // 15 * 6, surface_ycord - surf_ycord // 5 * 3,
              surf_xcord // 15, surf_ycord // 5),
        'J': (surf_xcord // 15 * 1 + surf_xcord // 15 * 7, surface_ycord - surf_ycord // 5 * 3,
              surf_xcord // 15, surf_ycord // 5),
        'j': (surf_xcord // 15 * 1 + surf_xcord // 15 * 7, surface_ycord - surf_ycord // 5 * 3,
              surf_xcord // 15, surf_ycord // 5),
        'K': (surf_xcord // 15 * 1 + surf_xcord // 15 * 8, surface_ycord - surf_ycord // 5 * 3,
              surf_xcord // 15, surf_ycord // 5),
        'k': (surf_xcord // 15 * 1 + surf_xcord // 15 * 8, surface_ycord - surf_ycord // 5 * 3,
              surf_xcord // 15, surf_ycord // 5),
        'L': (surf_xcord // 15 * 1 + surf_xcord // 15 * 9, surface_ycord - surf_ycord // 5 * 3,
              surf_xcord // 15, surf_ycord // 5),
        'l': (surf_xcord // 15 * 1 + surf_xcord // 15 * 9, surface_ycord - surf_ycord // 5 * 3,
              surf_xcord // 15, surf_ycord // 5),
        ':': (surf_xcord // 15 * 1 + surf_xcord // 15 * 10, surface_ycord - surf_ycord // 5 * 3,
              surf_xcord // 15, surf_ycord // 5),
        ';': (surf_xcord // 15 * 1 + surf_xcord // 15 * 10, surface_ycord - surf_ycord // 5 * 3,
              surf_xcord // 15, surf_ycord // 5),
        '"': (surf_xcord // 15 * 1 + surf_xcord // 15 * 11, surface_ycord - surf_ycord // 5 * 3,
              surf_xcord // 15, surf_ycord // 5),
        "'": (surf_xcord // 15 * 1 + surf_xcord // 15 * 11, surface_ycord - surf_ycord // 5 * 3,
              surf_xcord // 15, surf_ycord // 5),
        'Z': (surf_xcord // 15 * 1.5 + surf_xcord // 15 * 1, surface_ycord - surf_ycord // 5 * 2,
              surf_xcord // 15, surf_ycord // 5),
        'z': (surf_xcord // 15 * 1.5 + surf_xcord // 15 * 1, surface_ycord - surf_ycord // 5 * 2,
              surf_xcord // 15, surf_ycord // 5),
        'X': (surf_xcord // 15 * 1.5 + surf_xcord // 15 * 2, surface_ycord - surf_ycord // 5 * 2,
              surf_xcord // 15, surf_ycord // 5),
        'x': (surf_xcord // 15 * 1.5 + surf_xcord // 15 * 2, surface_ycord - surf_ycord // 5 * 2,
              surf_xcord // 15, surf_ycord // 5),
        'C': (surf_xcord // 15 * 1.5 + surf_xcord // 15 * 3, surface_ycord - surf_ycord // 5 * 2,
              surf_xcord // 15, surf_ycord // 5),
        'c': (surf_xcord // 15 * 1.5 + surf_xcord // 15 * 3, surface_ycord - surf_ycord // 5 * 2,
              surf_xcord // 15, surf_ycord // 5),
        'V': (surf_xcord // 15 * 1.5 + surf_xcord // 15 * 4, surface_ycord - surf_ycord // 5 * 2,
              surf_xcord // 15, surf_ycord // 5),
        'v': (surf_xcord // 15 * 1.5 + surf_xcord // 15 * 4, surface_ycord - surf_ycord // 5 * 2,
              surf_xcord // 15, surf_ycord // 5),
        'B': (surf_xcord // 15 * 1.5 + surf_xcord // 15 * 5, surface_ycord - surf_ycord // 5 * 2,
              surf_xcord // 15, surf_ycord // 5),
        'b': (surf_xcord // 15 * 1.5 + surf_xcord // 15 * 5, surface_ycord - surf_ycord // 5 * 2,
              surf_xcord // 15, surf_ycord // 5),
        'N': (surf_xcord // 15 * 1.5 + surf_xcord // 15 * 6, surface_ycord - surf_ycord // 5 * 2,
              surf_xcord // 15, surf_ycord // 5),
        'n': (surf_xcord // 15 * 1.5 + surf_xcord // 15 * 6, surface_ycord - surf_ycord // 5 * 2,
              surf_xcord // 15, surf_ycord // 5),
        'M': (surf_xcord // 15 * 1.5 + surf_xcord // 15 * 7, surface_ycord - surf_ycord // 5 * 2,
              surf_xcord // 15, surf_ycord // 5),
        'm': (surf_xcord // 15 * 1.5 + surf_xcord // 15 * 7, surface_ycord - surf_ycord // 5 * 2,
              surf_xcord // 15, surf_ycord // 5),
        '<': (surf_xcord // 15 * 1.5 + surf_xcord // 15 * 8, surface_ycord - surf_ycord // 5 * 2,
              surf_xcord // 15, surf_ycord // 5),
        ',': (surf_xcord // 15 * 1.5 + surf_xcord // 15 * 8, surface_ycord - surf_ycord // 5 * 2,
              surf_xcord // 15, surf_ycord // 5),
        '>': (surf_xcord // 15 * 1.5 + surf_xcord // 15 * 9, surface_ycord - surf_ycord // 5 * 2,
              surf_xcord // 15, surf_ycord // 5),
        '.': (surf_xcord // 15 * 1.5 + surf_xcord // 15 * 9, surface_ycord - surf_ycord // 5 * 2,
              surf_xcord // 15, surf_ycord // 5),
        '?': (surf_xcord // 15 * 1.5 + surf_xcord // 15 * 10, surface_ycord - surf_ycord // 5 * 2,
              surf_xcord // 15, surf_ycord // 5),
        '/': (surf_xcord // 15 * 1.5 + surf_xcord // 15 * 10, surface_ycord - surf_ycord // 5 * 2,
              surf_xcord // 15, surf_ycord // 5),
        '~': (surf_xcord // 15 * (-1) + surf_xcord // 15 * 1, surface_ycord - surf_ycord // 5 * 5,
              surf_xcord // 15, surf_ycord // 5),
        '`': (surf_xcord // 15 * (-1) + surf_xcord // 15 * 1, surface_ycord - surf_ycord // 5 * 5,
              surf_xcord // 15, surf_ycord // 5),
        '!': (surf_xcord // 15 * (-1) + surf_xcord // 15 * 2, surface_ycord - surf_ycord // 5 * 5,
              surf_xcord // 15, surf_ycord // 5),
        '1': (surf_xcord // 15 * (-1) + surf_xcord // 15 * 2, surface_ycord - surf_ycord // 5 * 5,
              surf_xcord // 15, surf_ycord // 5),
        '@': (surf_xcord // 15 * (-1) + surf_xcord // 15 * 3, surface_ycord - surf_ycord // 5 * 5,
              surf_xcord // 15, surf_ycord // 5),
        '2': (surf_xcord // 15 * (-1) + surf_xcord // 15 * 3, surface_ycord - surf_ycord // 5 * 5,
              surf_xcord // 15, surf_ycord // 5),
        '#': (surf_xcord // 15 * (-1) + surf_xcord // 15 * 4, surface_ycord - surf_ycord // 5 * 5,
              surf_xcord // 15, surf_ycord // 5),
        '3': (surf_xcord // 15 * (-1) + surf_xcord // 15 * 4, surface_ycord - surf_ycord // 5 * 5,
              surf_xcord // 15, surf_ycord // 5),
        '$': (surf_xcord // 15 * (-1) + surf_xcord // 15 * 5, surface_ycord - surf_ycord // 5 * 5,
              surf_xcord // 15, surf_ycord // 5),
        '4': (surf_xcord // 15 * (-1) + surf_xcord // 15 * 5, surface_ycord - surf_ycord // 5 * 5,
              surf_xcord // 15, surf_ycord // 5),
        '%': (surf_xcord // 15 * (-1) + surf_xcord // 15 * 6, surface_ycord - surf_ycord // 5 * 5,
              surf_xcord // 15, surf_ycord // 5),
        '5': (surf_xcord // 15 * (-1) + surf_xcord // 15 * 6, surface_ycord - surf_ycord // 5 * 5,
              surf_xcord // 15, surf_ycord // 5),
        '^': (surf_xcord // 15 * (-1) + surf_xcord // 15 * 7, surface_ycord - surf_ycord // 5 * 5,
              surf_xcord // 15, surf_ycord // 5),
        '6': (surf_xcord // 15 * (-1) + surf_xcord // 15 * 7, surface_ycord - surf_ycord // 5 * 5,
              surf_xcord // 15, surf_ycord // 5),
        '&': (surf_xcord // 15 * (-1) + surf_xcord // 15 * 8, surface_ycord - surf_ycord // 5 * 5,
              surf_xcord // 15, surf_ycord // 5),
        '7': (surf_xcord // 15 * (-1) + surf_xcord // 15 * 8, surface_ycord - surf_ycord // 5 * 5,
              surf_xcord // 15, surf_ycord // 5),
        '*': (surf_xcord // 15 * (-1) + surf_xcord // 15 * 9, surface_ycord - surf_ycord // 5 * 5,
              surf_xcord // 15, surf_ycord // 5),
        '8': (surf_xcord // 15 * (-1) + surf_xcord // 15 * 9, surface_ycord - surf_ycord // 5 * 5,
              surf_xcord // 15, surf_ycord // 5),
        '(': (surf_xcord // 15 * (-1) + surf_xcord // 15 * 10, surface_ycord - surf_ycord // 5 * 5,
              surf_xcord // 15, surf_ycord // 5),
        '9': (surf_xcord // 15 * (-1) + surf_xcord // 15 * 10, surface_ycord - surf_ycord // 5 * 5,
              surf_xcord // 15, surf_ycord // 5),
        ')': (surf_xcord // 15 * (-1) + surf_xcord // 15 * 11, surface_ycord - surf_ycord // 5 * 5,
              surf_xcord // 15, surf_ycord // 5),
        '0': (surf_xcord // 15 * (-1) + surf_xcord // 15 * 11, surface_ycord - surf_ycord // 5 * 5,
              surf_xcord // 15, surf_ycord // 5),
        '_': (surf_xcord // 15 * (-1) + surf_xcord // 15 * 12, surface_ycord - surf_ycord // 5 * 5,
              surf_xcord // 15, surf_ycord // 5),
        '-': (surf_xcord // 15 * (-1) + surf_xcord // 15 * 12, surface_ycord - surf_ycord // 5 * 5,
              surf_xcord // 15, surf_ycord // 5),
        '+': (surf_xcord // 15 * (-1) + surf_xcord // 15 * 13, surface_ycord - surf_ycord // 5 * 5,
              surf_xcord // 15, surf_ycord // 5),
        '=': (surf_xcord // 15 * (-1) + surf_xcord // 15 * 13, surface_ycord - surf_ycord // 5 * 5,
              surf_xcord // 15, surf_ycord // 5),
        '|': (surf_xcord // 15 * 0.5 + surf_xcord // 15 * 13, surface_ycord - surf_ycord // 5 * 4,
              surf_xcord // 15 * 1.5, surf_ycord // 5),
        '\\': (surf_xcord // 15 * 0.5 + surf_xcord // 15 * 13, surface_ycord - surf_ycord // 5 * 4,
               surf_xcord // 15 * 1.5, surf_ycord // 5),
        'Enter': (surf_xcord // 15 * 13, surface_ycord - surf_ycord // 5 * 3, surf_xcord // 15 * 2, surf_ycord // 5),
        'Space': (surf_xcord // 3, surface_ycord - surf_ycord // 5 * 1, surf_xcord // 3, surf_ycord // 5),
        'LCtrl': (0, surface_ycord - surf_ycord // 5 * 1, surf_xcord // 9, surf_ycord // 5),
        'LShift': (0, surface_ycord - surf_ycord // 5 * 2, surf_xcord // 15 * 2.5, surf_ycord // 5),
        'Caps Lock': (0, surface_ycord - surf_ycord // 5 * 3, surf_xcord // 15 * 2, surf_ycord // 5),
        'Tab': (0, surface_ycord - surf_ycord // 5 * 4, surf_xcord // 15 * 1.5, surf_ycord // 5),
        'Alt': (surf_xcord // 9 * 2, surface_ycord - surf_ycord // 5 * 1, surf_xcord // 9, surf_ycord // 5),
        'AltGr': (surf_xcord // 9 * 6, surface_ycord - surf_ycord // 5 * 1, surf_xcord // 9, surf_ycord // 5),
        'RCtrl': (surf_xcord // 9 * 8, surface_ycord - surf_ycord // 5 * 1, surf_xcord // 9, surf_ycord // 5),
        'RShift': (surf_xcord // 15 * 12.5, surface_ycord - surf_ycord // 5 * 2, surf_xcord // 6, surf_ycord // 5),
        'Backspace': (surf_xcord // 15 * 13, surface_ycord - surf_ycord // 5 * 5, surf_xcord // 15 * 2, surf_ycord // 5)

    }
    return dict

def KeyboardPainter(tuple, color, surface):
    pygame.draw.rect(surface, color, tuple)