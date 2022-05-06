from KeyboardPainter import CordsGet
mistakes = condition_counter = lines_counter = letter_counter = word_counter = counter1 = counter2 = width = 0
sf_spawn = surf_xcord = surf_info_cordx = surf_input_cordx = surf_text_cordx = surf_text_cordy = indent4 = 0
def_l_size = lnumb_ind_hr = ctrl_mult = bdl_sl_mult = l_nm_indf = mult_LW = l_fact = slsh_dev = 1
cps_mult = sft_mult = 1.1
lnumb_ind_UP = l_nm_inds = 1.5
let_nmb_cf = indmult_f = l_nm_indt = lnumb_ind_MD = 2
stats_lines_count = st_time_koef = l_s_dev = ver_l_countLW = mult_DN = strt_x_d1 = dct_ind = 2
lnumb_ind_DN = l_nm_indft = 2.5
stats_area_ind_c = txt_area_ind_c = surf_area_ind_c = strt_y_m1 = l_nm_indfi = mult_MD = 3
up_line_size = down_line_size = 3
l_nm_indsi = tab_mult = 3.5
left_line_size = hor_l_count = st_mist_ind = mult_UP = 4
alt_line_mult = ctrl_line_dev = mult_SK = khc = indent1 = txt_ind_koef = strt_y_d1 = set_ev_d = 5
stats_area_ind_s = txt_area_ind_s = surf_area_ind_s = 6
st_mist_koef = right_line_size = 7
alt_line_dev = strt_x_d2 = 9
st_ltry_txt_mX = maxbrht = ctrl_line_mult = th_line_cou = 10
sec_line_cou = ver_l_countDN = strt_y_m2 = 11
fst_line_cou = ver_l_countMD = 12
fth_line_cou = ver_l_countUP = 13
ent_mult = bck_mult = 13.6
st_ltry_txt_kY = indent3 = kwc = l4_x_ind = wds_ind1 = 15
st_ltry_txt_kX = indent2 = ex_text_size = wds_ind2 = sft_dev = 18
ctrl_dev = strt_x_d3 = 25
seconds_in_min = surf_info_cordy = surf_input_cordy = 60
tab_dev = mon_size = l3_x_ind_dev = l4_x_ind_dev = 100
res2_y = surface_cordy = surface_ycord = 700
res2_x = surface_cordx = surface_xcord = 1035
kong3_y_dev = kong3_y_devs = 70 / 46
mon4_y_dev = mon3_y_devs = 70 / 48
mon3_y_dev = choores_y = mon1_y_devs = 70 / 8
marker8 = False
running = marker1 = marker2 = marker3 = marker4 = marker5 = marker6 = marker7 = True
color = {'color0': (0, 200, 0), 'color1': (20, 160, 0), 'color2': (40, 120, 0), 'color3': (80, 80, 0),
         'color4': (100, 40, 0), 'color5': (125, 0, 0), 'color6': (150, 0, 0), 'color7': (175, 0, 0),
         'color8': (200, 0, 0), 'color9': (225, 0, 0), 'color10': (255, 0, 0)}
space_numb, db_backsl_numb, str_line_numb, back_numb, enter_numb, r_shft_numb, r_ctrl_numb, altgr_numb, alt_numb, \
l_ctrl_numb, l_shft_numb, caps_numb, tab_numb = [i for i in range(105, 92, -1)]
micros_in_seconds = 1000000
st_ltry_kX = 30
stats1_txt_size = 20
st_ltry_mX = 21.5
st_ltry_kY = 17
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 230, 0)
RED = (255, 0, 0)
filewithtext = 'text1'
condition = 'correct'
key_mod_d1 = 4096
key_mod_d2 = 12289
key_mod_u1 = 4097
key_mod_u2 = 12288
un_chec = 1000
dict_of_s_s = 25
FPS = cps_dev = 60
string_scroller = 85
wds_dev1 = 30
alt_mult = 7.9
altg_mult = 21.3
rctrl_mult = 28.3
rsft_mult = 13.4
str_mult = 13.5
spc_mult = 6.9
ind4dev = 45
mon_x_dev = 21 / 17
kong_x_dev = 21 / 2
chootxt_x = 21 / 17.1
choores_x = 21 / 1.4
mon2_y_dev = 70 / 28
chootxt_y = 70 / 4
kong1_y_dev = 70 / 13
kong4_y_dev = 70 / 29.5
set_ev_u = 55
kong_dev = 14 / 2.5
mon_dev = 14 / 3
l3_x_ind = 17
mon1_y_dev1 = 14 / 3
kong1_y_devs = 70 / 13
kong2_y_devs = 70 * 29.5
kong_x_devs = 14 / 2.5
res1_x = 900
res1_y = 600
res3_x = 1125
res3_y = 750
scrol1 = 70
scrol2 = 85
scrol3 = 90
l2_size = 40
l1_dev = 75
l1_ind = 12
surf_ycord = 300

def dictofcords(surf_xcord, surf_ycord, surface_ycord):
    cords = (surf_xcord, surf_ycord, surface_ycord)
    dictofcords = {
        'Q': CordsGet(1.5, 4, cords, 1),  'q': CordsGet(1.5, 4, cords, 1),  'W': CordsGet(2.5, 4, cords, 1),
        'w': CordsGet(2.5, 4, cords, 1),  'E': CordsGet(3.5, 4, cords, 1),  'e': CordsGet(3.5, 4, cords, 1),
        'R': CordsGet(4.5, 4, cords, 1),  'r': CordsGet(4.5, 4, cords, 1),  'T': CordsGet(5.5, 4, cords, 1),
        't': CordsGet(5.5, 4, cords, 1),  'Y': CordsGet(6.5, 4, cords, 1),  'y': CordsGet(6.5, 4, cords, 1),
        'U': CordsGet(7.5, 4, cords, 1),  'u': CordsGet(7.5, 4, cords, 1),  'I': CordsGet(8.5, 4, cords, 1),
        'i': CordsGet(8.5, 4, cords, 1),  'O': CordsGet(9.5, 4, cords, 1),  'o': CordsGet(9.5, 4, cords, 1),
        'P': CordsGet(10.5, 4, cords, 1), 'p': CordsGet(10.5, 4, cords, 1), '{': CordsGet(11.5, 4, cords, 1),
        '[': CordsGet(11.5, 4, cords, 1), '}': CordsGet(12.5, 4, cords, 1), ']': CordsGet(12.5, 4, cords, 1),
        'A': CordsGet(2, 3, cords, 1),    'a': CordsGet(2, 3, cords, 1),    'S': CordsGet(3, 3, cords, 1),
        's': CordsGet(3, 3, cords, 1),    'D': CordsGet(4, 3, cords, 1),    'd': CordsGet(4, 3, cords, 1),
        'F': CordsGet(5, 3, cords, 1),    'f': CordsGet(5, 3, cords, 1),    'G': CordsGet(6, 3, cords, 1),
        'g': CordsGet(6, 3, cords, 1),    'H': CordsGet(7, 3, cords, 1),    'h': CordsGet(7, 3, cords, 1),
        'J': CordsGet(8, 3, cords, 1),    'j': CordsGet(8, 3, cords, 1),    'K': CordsGet(9, 3, cords, 1),
        'k': CordsGet(9, 3, cords, 1),    'L': CordsGet(10, 3, cords, 1),   'l': CordsGet(10, 3, cords, 1),
        ':': CordsGet(11, 3, cords, 1),   ';': CordsGet(11, 3, cords, 1),   '"': CordsGet(12, 3, cords, 1),
        "'": CordsGet(12, 3, cords, 1),   'Z': CordsGet(2.5, 2, cords, 1),  'z': CordsGet(2.5, 2, cords, 1),
        'X': CordsGet(3.5, 2, cords, 1),  'x': CordsGet(3.5, 2, cords, 1),  'C': CordsGet(4.5, 2, cords, 1),
        'c': CordsGet(4.5, 2, cords, 1),  'V': CordsGet(5.5, 2, cords, 1),  'v': CordsGet(5.5, 2, cords, 1),
        'B': CordsGet(6.5, 2, cords, 1),  'b': CordsGet(6.5, 2, cords, 1),  'N': CordsGet(7.5, 2, cords, 1),
        'n': CordsGet(7.5, 2, cords, 1),  'M': CordsGet(8.5, 2, cords, 1),  'm': CordsGet(8.5, 2, cords, 1),
        '<': CordsGet(9.5, 2, cords, 1),  ',': CordsGet(9.5, 2, cords, 1),  '>': CordsGet(10.5, 2, cords, 1),
        '.': CordsGet(10.5, 2, cords, 1), '?': CordsGet(11.5, 2, cords, 1), '/': CordsGet(11.5, 2, cords, 1),
        '~': CordsGet(0, 5, cords, 1),    '`': CordsGet(0, 5, cords, 1),    '!': CordsGet(1, 5, cords, 1),
        '1': CordsGet(1, 5, cords, 1),    '@': CordsGet(2, 5, cords, 1),    '2': CordsGet(2, 5, cords, 1),
        '#': CordsGet(3, 5, cords, 1),    '3': CordsGet(3, 5, cords, 1),    '$': CordsGet(4, 5, cords, 1),
        '4': CordsGet(4, 5, cords, 1),    '%': CordsGet(5, 5, cords, 1),    '5': CordsGet(5, 5, cords, 1),
        '^': CordsGet(6, 5, cords, 1),    '6': CordsGet(6, 5, cords, 1),    '&': CordsGet(7, 5, cords, 1),
        '7': CordsGet(7, 5, cords, 1),    '*': CordsGet(8, 5, cords, 1),    '8': CordsGet(8, 5, cords, 1),
        '(': CordsGet(9, 5, cords, 1),    '9': CordsGet(9, 5, cords, 1),    ')': CordsGet(10, 5, cords, 1),
        '0': CordsGet(10, 5, cords, 1),   '_': CordsGet(11, 5, cords, 1),   '-': CordsGet(11, 5, cords, 1),
        '+': CordsGet(12, 5, cords, 1),   '=': CordsGet(12, 5, cords, 1),
        '|': CordsGet(13.5, 4, cords, 1.6), '\\': CordsGet(13.5, 4, cords, 1.6),
        'Enter': CordsGet(13, 3, cords, 2), 'Space': CordsGet(5, 1, cords, 5),
        'LCtrl': CordsGet(0, 1, cords, 15 / 9), 'LShift': CordsGet(0, 2, cords, 2.5),
        'Caps Lock': CordsGet(0, 3, cords, 2), 'Tab': CordsGet(0, 4, cords, 1.5),
        'Alt': CordsGet(30 / 9, 1, cords, 15 / 9), 'AltGr': CordsGet(10, 1, cords, 15 / 9),
        'RCtrl': CordsGet(40 / 3, 1, cords, 15 / 9), 'RShift': CordsGet(12.5, 2, cords, 15 / 5),
        'Backspace': CordsGet(13, 5, cords, 15 / 2),
    }
    return dictofcords
