import pygame

def DictOfCords(surface_ycord, surf_xcord, surf_ycord):

    """func returns a dict with buttons coordinates in values"""

    cords = (surf_xcord, surf_ycord, surface_ycord)
    dict = {
        'Q': CordsGet(0.5, 1, 4, cords, 1),  'q': CordsGet(0.5, 1, 4, cords, 1),  'W': CordsGet(0.5, 2, 4, cords, 1),
        'w': CordsGet(0.5, 2, 4, cords, 1),  'E': CordsGet(0.5, 3, 4, cords, 1),  'e': CordsGet(0.5, 3, 4, cords, 1),
        'R': CordsGet(0.5, 4, 4, cords, 1),  'r': CordsGet(0.5, 4, 4, cords, 1),  'T': CordsGet(0.5, 5, 4, cords, 1),
        't': CordsGet(0.5, 5, 4, cords, 1),  'Y': CordsGet(0.5, 6, 4, cords, 1),  'y': CordsGet(0.5, 6, 4, cords, 1),
        'U': CordsGet(0.5, 7, 4, cords, 1),  'u': CordsGet(0.5, 7, 4, cords, 1),  'I': CordsGet(0.5, 8, 4, cords, 1),
        'i': CordsGet(0.5, 8, 4, cords, 1),  'O': CordsGet(0.5, 9, 4, cords, 1),  'o': CordsGet(0.5, 9, 4, cords, 1),
        'P': CordsGet(0.5, 10, 4, cords, 1), 'p': CordsGet(0.5, 10, 4, cords, 1), '{': CordsGet(0.5, 11, 4, cords, 1),
        '[': CordsGet(0.5, 11, 4, cords, 1), '}': CordsGet(0.5, 12, 4, cords, 1), ']': CordsGet(0.5, 12, 4, cords, 1),
        'A': CordsGet(1, 1, 3, cords, 1),    'a': CordsGet(1, 1, 3, cords, 1),    'S': CordsGet(1, 2, 3, cords, 1),
        's': CordsGet(1, 2, 3, cords, 1),    'D': CordsGet(1, 3, 3, cords, 1),    'd': CordsGet(1, 3, 3, cords, 1),
        'F': CordsGet(1, 4, 3, cords, 1),    'f': CordsGet(1, 4, 3, cords, 1),    'G': CordsGet(1, 5, 3, cords, 1),
        'g': CordsGet(1, 5, 3, cords, 1),    'H': CordsGet(1, 6, 3, cords, 1),    'h': CordsGet(1, 6, 3, cords, 1),
        'J': CordsGet(1, 7, 3, cords, 1),    'j': CordsGet(1, 7, 3, cords, 1),    'K': CordsGet(1, 8, 3, cords, 1),
        'k': CordsGet(1, 8, 3, cords, 1),    'L': CordsGet(1, 9, 3, cords, 1),    'l': CordsGet(1, 9, 3, cords, 1),
        ':': CordsGet(1, 10, 3, cords, 1),   ';': CordsGet(1, 10, 3, cords, 1),   '"': CordsGet(1, 11, 3, cords, 1),
        "'": CordsGet(1, 11, 3, cords, 1),   'Z': CordsGet(1.5, 1, 2, cords, 1),  'z': CordsGet(1.5, 1, 2, cords, 1),
        'X': CordsGet(1.5, 2, 2, cords, 1),  'x': CordsGet(1.5, 2, 2, cords, 1),  'C': CordsGet(1.5, 3, 2, cords, 1),
        'c': CordsGet(1.5, 3, 2, cords, 1),  'V': CordsGet(1.5, 4, 2, cords, 1),  'v': CordsGet(1.5, 4, 2, cords, 1),
        'B': CordsGet(1.5, 5, 2, cords, 1),  'b': CordsGet(1.5, 5, 2, cords, 1),  'N': CordsGet(1.5, 6, 2, cords, 1),
        'n': CordsGet(1.5, 6, 2, cords, 1),  'M': CordsGet(1.5, 7, 2, cords, 1),  'm': CordsGet(1.5, 7, 2, cords, 1),
        '<': CordsGet(1.5, 8, 2, cords, 1),  ',': CordsGet(1.5, 8, 2, cords, 1),  '>': CordsGet(1.5, 9, 2, cords, 1),
        '.': CordsGet(1.5, 9, 2, cords, 1),  '?': CordsGet(1.5, 10, 2, cords, 1), '/': CordsGet(1.5, 10, 2, cords, 1),
        '~': CordsGet(-1, 1, 5, cords, 1),   '`': CordsGet(-1, 1, 5, cords, 1),   '!': CordsGet(-1, 2, 5, cords, 1),
        '1': CordsGet(-1, 2, 5, cords, 1),   '@': CordsGet(-1, 3, 5, cords, 1),   '2': CordsGet(-1, 3, 5, cords, 1),
        '#': CordsGet(-1, 4, 5, cords, 1),   '3': CordsGet(-1, 4, 5, cords, 1),   '$': CordsGet(-1, 5, 5, cords, 1),
        '4': CordsGet(-1, 5, 5, cords, 1),   '%': CordsGet(-1, 6, 5, cords, 1),   '5': CordsGet(-1, 6, 5, cords, 1),
        '^': CordsGet(-1, 7, 5, cords, 1),   '6': CordsGet(-1, 7, 5, cords, 1),   '&': CordsGet(-1, 8, 5, cords, 1),
        '7': CordsGet(-1, 8, 5, cords, 1),   '*': CordsGet(-1, 9, 5, cords, 1),   '8': CordsGet(-1, 9, 5, cords, 1),
        '(': CordsGet(-1, 10, 5, cords, 1),  '9': CordsGet(-1, 10, 5, cords, 1),  ')': CordsGet(-1, 11, 5, cords, 1),
        '0': CordsGet(-1, 11, 5, cords, 1),  '_': CordsGet(-1, 12, 5, cords, 1),  '-': CordsGet(-1, 12, 5, cords, 1),
        '+': CordsGet(-1, 13, 5, cords, 1),  '=': CordsGet(-1, 13, 5, cords, 1),
        '|': CordsGet(0.5, 13, 4, cords, 1.5), '\\': CordsGet(0.5, 13, 4, cords, 1.5),
        'Enter': CordsGet(0, 13, 3, cords, 2), 'Space': CordsGet(0, 5, 1, cords, 5),
        'LCtrl': CordsGet(0, 0, 1, cords, 15 / 9), 'LShift': CordsGet(0, 0, 2, cords, 2.5),
        'Caps Lock': CordsGet(0, 0, 3, cords, 2), 'Tab': CordsGet(0, 0, 4, cords, 1.5),
        'Alt': CordsGet(0, 30 / 9, 1, cords, 15 / 9), 'AltGr': CordsGet(0, 10, 1, cords, 15 / 9),
        'RCtrl': CordsGet(0, 40 / 3, 1, cords, 15 / 9), 'RShift': CordsGet(0, 12.5, 2, cords, 15 / 6),
        'Backspace': CordsGet(0, 13, 5, cords, 15 / 2),
    }
    return dict

def KeyboardPainter(tuple, color, surface):

    """func paints the right button in the right color"""

    pygame.draw.rect(surface, color, tuple)

def CordsGet(surf_xc_kf1, surf_xc_kf2, surf_yc_kf, cords, wid_dev):

    """func returns buttons coordinates"""

    return (cords[0] // 15 * surf_xc_kf1 + cords[0] // 15 * surf_xc_kf2, cords[2] - cords[1] // 5 *
            surf_yc_kf, cords[0] / 15 * wid_dev, cords[1] // 5),

