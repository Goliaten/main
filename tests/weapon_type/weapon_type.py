def stat_len(x, y, c=0):      #x is value to be lengthened, y is length, c is option choosing
    if c == 0:           #adds ' ' to the end
        x = str(x)
        while len(x) < y:
            x += ' '
        return x
    if c == 1:          #adds ' ' to the beginning
        x = str(x)
        while len(x) < y:
            x = ' ' + x
        return x


# y = 5
# x = 0.1*(y-5)+1
# z = (0.3*y)**1.1
# for y in range(0, 15):
#     x = 0.1*(y-5)+1
#     z = (0.3*y)**1.1
#     x = y*x
#     z = y+z
#     print (y, ': ', x, z)

v=60  #max armor
z=120   #max dmg
e = '---'   #used in header writing
# a = int(input('1=blunt 2=sharp 3=pierce 4=none'))

with open('blunt.txt', 'w') as f:
    t = e
    for x in range(0, v):
        t += stat_len(x, 4, 1)
    t += '\n'
    f.write(t)
    for x in range(0, z):
        for y in range(0, v):
            if y == 0:
                t = stat_len(str(x),4,1)
            blunt_red = int(x*0.2)
            blunt_bon = int(x*0.4)
            if blunt_bon > y:
                blunt_bon = y
            atk_dmg = x + blunt_bon - blunt_red - y
            if atk_dmg <= 0:
                atk_dmg = ' '
            t += ' ' + stat_len(atk_dmg,3,1)
        t += '\n'
        f.write(t)

with open('sharp.txt', 'w') as f:
    t = e
    for x in range(0, v):
        t += stat_len(x, 4, 1)
    t += '\n'
    f.write(t)
    for x in range(0, z):
        for y in range(0, v):
            if y == 0:
                t = stat_len(str(x),4,1)
            sharp_bon = int(x*0.2)
            sharp_red = int(x*0.4)
            if sharp_red > y:
                sharp_red = y
            atk_dmg = x + sharp_bon - sharp_red - y
            if atk_dmg <= 0:
                atk_dmg = ' '
            t += ' ' + stat_len(atk_dmg,3,1)
        t += '\n'
        f.write(t)

with open('pierce.txt', 'w') as f:
    t = e
    for x in range(0, v):
        t += stat_len(x, 4, 1)
    t += '\n'
    f.write(t)
    for x in range(0, z):
        for y in range(0, v):
            if y == 0:
                t = stat_len(str(x),4,1)
            pierce_bonus = int(x*0.1)
            if pierce_bonus > y:
                pierce_bonus = y
            atk_dmg = x + pierce_bonus - y
            if atk_dmg <= 0:
                atk_dmg = ' '
            t += ' ' + stat_len(atk_dmg,3,1)
        t += '\n'
        f.write(t)

with open('none.txt', 'w') as f:
    t = e
    for x in range(0, v):
        t += stat_len(x, 4, 1)
    t += '\n'
    f.write(t)
    for x in range(0, z):
        for y in range(0, v):
            if y == 0:
                t = stat_len(str(x),4,1)
            atk_dmg = x - y
            if atk_dmg <= 0:
                atk_dmg = ' '
            t += ' ' + stat_len(atk_dmg,3,1)
        t += '\n'
        f.write(t)