def stat_len(x, y=1, c=0):
    x = str(x)
    while len(x) < y and c == 0:
        x += ' '
    while len(x) < y and c == 1:
        x = ' ' + x
    return x


Hero = [70, 10] #hp, atk  Hero
Champion = [90, 9]
Assasin = [55, 11]
all_char = Hero, Champion, Assasin  #who will be used for leveling

counter = 0
level = 1   #starting level
max_lvl = 50  #max level

with open('level_progress.txt', 'w') as file:
    
    l = stat_len(level, 3, 1) + '| '
    for char in all_char:
        counter += 1
        l += (stat_len(counter, 2, 1) + ': ' + stat_len(char[0], 3, 1) + ' ' + stat_len(char[1], 3, 1) + '|')
    l += '\n'
    file.write(l)
    
    while level != 50:
        counter = 0
        level += 1
        
        l = stat_len(level, 3, 1) + '| '
        
        for char in all_char:
            
            #------------------------------------
            y = int(char[0]*0.1)   #loop for hp
            if y == 0:      #prevents from gain being 0
                y = 1
            while y > 20:    #limits gain
                y -= 10
            char[0] += y     #adds gain to stat
            
            y = int(char[1]*0.1)  #loop for dmg
            if y == 0:    #prevents from gain being 0
                y = 1
            while y > 3:   #limits gain
                y -= 2
            char[1] += y      #adds gain to stat
            #----------------------------------------
            
            counter += 1                                 
            l += (stat_len(counter, 2, 1) + ': ' + stat_len(char[0], 3, 1) + ' ' + stat_len(char[1], 3, 1) + '|')
        l += '\n'
        file.write(l)
