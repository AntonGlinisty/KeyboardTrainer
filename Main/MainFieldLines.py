import pygame

def BordersDrawer(surface, BLACK, surf_info_cordx, surf_input_cordx, surf_text_cordx, surf_info_cordy,
                  surf_input_cordy, surf_text_cordy, left_line_size, right_line_size, up_line_size, down_line_size, RED):
    pygame.draw.line(surface, BLACK, [0, 0], [0, surf_info_cordy], left_line_size)
    pygame.draw.line(surface, BLACK, [surf_info_cordx, 0],
                     [surf_info_cordx, surf_info_cordy], right_line_size)
    pygame.draw.line(surface, BLACK, [0, 0 + up_line_size // 2], [surf_info_cordx, 0 + up_line_size // 2],
                     up_line_size)
    pygame.draw.line(surface, BLACK, [0, surf_info_cordy - down_line_size // 2 - 1],
                     [surf_info_cordx, surf_info_cordy - down_line_size // 2 - 1], down_line_size)
    pygame.draw.line(surface, RED, [0, surf_info_cordy], [0, surf_info_cordy + surf_input_cordy], left_line_size)
    pygame.draw.line(surface, RED, [surf_input_cordx, surf_info_cordy],
                     [surf_input_cordx, surf_info_cordy + surf_input_cordy], right_line_size)
    pygame.draw.line(surface, RED, [0, surf_info_cordy + up_line_size // 2],
                     [surf_input_cordx, surf_input_cordy + up_line_size // 2], up_line_size)
    pygame.draw.line(surface, RED, [0, surf_info_cordy + surf_input_cordy - down_line_size // 2 - 1],
                     [surf_input_cordx, surf_info_cordy + surf_input_cordy - down_line_size // 2 - 1], down_line_size)
    pygame.draw.line(surface, BLACK, [0, surf_info_cordy + surf_input_cordy],
                     [0, surf_info_cordy + surf_input_cordy + surf_text_cordy], left_line_size)
    pygame.draw.line(surface, BLACK, [surf_text_cordx, surf_info_cordy + surf_input_cordy],
                     [surf_text_cordx, surf_info_cordy + surf_input_cordy + surf_text_cordy], right_line_size)
    pygame.draw.line(surface, BLACK, [0, surf_info_cordy + surf_input_cordy + up_line_size // 2],
                     [surf_text_cordx, surf_info_cordy + surf_input_cordy + up_line_size // 2], up_line_size)
    pygame.draw.line(surface, BLACK, [0, surf_info_cordy + surf_input_cordy + surf_text_cordy],
                     [surf_text_cordx, surf_info_cordy + surf_input_cordy + surf_text_cordy],
                     down_line_size)