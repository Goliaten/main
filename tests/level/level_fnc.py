def stat_len(x, y=1, c=0):
    x = str(x)
    while len(x) < y and c == 0:
        x += ' '
    while len(x) < y and c == 1:
        x = ' ' + x
    return x


a = 101     #max level
z = input('1=v1 2=v2 3=expmod')
z = int(z)
if z == 1:
    with open('level_fncv1.txt', 'w') as file:
        file.write('lvl  lvlexp totalexp  (needed)\n')
        l = ''
        v = 0
        for x in range(1, a):
            if x == 1:
                b = 0
            else:
#                 b = 200*(x-1)+100*(x-2)   #option 1    shows level needed for each level from previous
                b = 300*x-400 # shortened formula
                v += b
            l = stat_len(x, 3, 1) + ': ' + stat_len(b, 7) + stat_len(v) + '\n'
            file.write(l)
            
elif z == 2:
    with open('level_fncv2.txt', 'w') as file:
        file.write('lvl  lvlexp total  (needed)\n')
        l = ''
        v = 0
        for x in range(1, a):
            if x == 1:
                b = 0
            else:
                z = b
                b = (200+100*(x-2))*(x-1)    #option 2    shows level needed to get to level from
#                 b = 100*x**2-100*x  #shortened formula
                v = b-z
#                 y = x-1
#                 z = x
#                 v = 200*x     #formula for calculating
                
                
            l = stat_len(x, 3, 1) + ': ' + stat_len(v, 7) + stat_len(b) + '\n'
            file.write(l)
elif z == 3:
    with open('exp_modv1.txt', 'w') as file:   #experience modifier
        

        for y in range(1, a):
            x = 200
            z = int(y/5)
            x -= int(x*(y-1)/100)
            l = stat_len(y, 3, 1) + ': ' + stat_len(x, 7) + '\n'
            file.write(l)


            