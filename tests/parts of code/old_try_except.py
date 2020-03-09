#even older version has print() instead of menu_print() and pause()

a = input('Type')
try:              #error checking
    a = int(a)
except:
    if a == 'ex':
        break
    menu_print(['Wrong input'], 1)
    pause()
    continue
else:
    if a < 1 or a > 6:
        menu_print(['Choice out of range'], 1)
        pause()
        continue
