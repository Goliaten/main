err_c = 0
m = 1
def in_err_ch(o, length): #input_error_check
    global m, err_c
    if err_c == 0:
        m = 1
    try:
        o = int(o)
    except:
        err_c = 1
        if o == 'ex':
            m = 1
            return o, 2
        elif o == 'next':
            return o, 3
        elif o == 'back':
            return o, 4
        menu_print(['Wrong input'], 1)
        pause()
        return o, 1
    else:
        if o < 0 or o > length:
            err_c = 1
            menu_print(['Choice out of range'], 1)
            pause()
            return o, 1
        m = 1
        err_c = 0
        return o, 0


while True:
    temp_menu = []
    for x in range(0, 54):
        x = str(x)
        temp_menu.append(x)
    menu_print(temp_menu, 0, 2)
    
    a = input('Choose:')

    a, z = in_err_ch(a, len(temp_menu))

    if z == 1:
        continue
    elif z == 2:
        break
    elif z == 3:
        m += 1
        continue
    elif z == 4:
        m -= 1
        continue
    