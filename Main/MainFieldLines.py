import pygame

def BordersDrawer(surface, BLACK, surf_inf_cX, surf_inp_cX, surf_text_cX, surf_inf_cY, surf_inp_cY, surf_text_cY,
                  l_l_size, r_l_size, u_l_size, d_l_size, RED):

    """func draws the boundaries of areas on the screen"""

    cordY = surf_inf_cY + surf_inp_cY
    LinesDrawer(surface, BLACK, 0, 0, 0, surf_inf_cY, l_l_size)
    LinesDrawer(surface, BLACK, surf_inf_cX, 0, surf_inf_cX, surf_inf_cY, r_l_size)
    LinesDrawer(surface, BLACK, 0, u_l_size // 2, surf_inf_cX, u_l_size // 2, u_l_size)
    LinesDrawer(surface, BLACK, 0, surf_inf_cY - d_l_size // 2 - 1, surf_inf_cX,
                surf_inf_cY - d_l_size // 2 - 1, d_l_size)
    LinesDrawer(surface, RED, 0, surf_inf_cY, 0, cordY, l_l_size)
    LinesDrawer(surface, RED, surf_inf_cX, surf_inf_cY, surf_inp_cX, cordY, r_l_size)
    LinesDrawer(surface, RED, 0, surf_inf_cY + u_l_size // 2, surf_inp_cX, surf_inp_cY + u_l_size // 2, u_l_size)
    LinesDrawer(surface, RED, 0, cordY - d_l_size // 2 - 1, surf_inp_cX, cordY - d_l_size // 2 - 1, d_l_size)
    LinesDrawer(surface, BLACK, 0, cordY, 0, cordY + surf_text_cY, l_l_size)
    LinesDrawer(surface, BLACK, surf_text_cX, cordY, surf_text_cX, cordY + surf_text_cY, r_l_size)
    LinesDrawer(surface, BLACK, 0, cordY + u_l_size // 2, surf_text_cX, cordY + u_l_size // 2, u_l_size)
    LinesDrawer(surface, BLACK, 0, cordY + surf_text_cY, surf_text_cX, cordY + surf_text_cY, d_l_size)

def LinesDrawer(surface, color, l_cordX, l_cordY, r_cordX, r_cordY, size):

    """func draws lines"""

    pygame.draw.line(surface, color, [l_cordX, l_cordY], [r_cordX, r_cordY], size)
