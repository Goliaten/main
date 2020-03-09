##save
                with open('savefilev2.txt', 'w') as save:
                    for char in team_1:
                        save.write('char')
                        save.write('0' + str(char.ID))
                        save.write(str(char.weapon.ID))
                        save.write(str(char.armor.ID))
                        save.write('---\n')
                    for item in held_items:
                        save.write('item')
                        save.write('0' + str(item.ID))
                        save.write('---\n')
                    for weap in held_weapons:
                        save.write('weap')
                        save.write(str(weap.ID))
                        save.write('---\n')
                    for armo in held_armor:
                        save.write('armo')
                        save.write(str(armo.ID))
                        save.write('---\n')
                    save.write('gold')
                    t_gold_t = stat_len(gold, 4, 1)
                    t_gold = ''
                    for x in t_gold_t:
                        if x == ' ':
                            v = '0'
                        else:
                            v = x
                        t_gold += v
                    save.write(str(t_gold))
                    save.write('---\n')

##load                
            if a == 4:
                with open('savefilev2.txt', 'r') as save:
                    temp_team = []
                    temp_weap = []
                    temp_item = []
                    temp_armo = []
                    line = ' '
                    count = -1
                    while line != '':
                        line = save.read(4)
                        
                        if line == 'char':
                            count += 1
                            print('char')
                            while line != '---\n':
                                line = save.read(4)
                                try:
                                    line = int(line)
                                except:
                                    True
                                
                                for x in global_allies_baseline:
                                    if x.ID == line:
                                        temp_team.append(x)
                                        print('yes char')
                                for x in global_weapons:
                                    if x.ID == line:
                                        x.equip(temp_team[count])
                                        print('yes weapon')
                                for x in global_armor:
                                    if x.ID == line:
                                        x.equip(temp_team[count])
                                        print('yes armor')
                        elif line == 'weap':
                            print('weap')
                            while line != '---\n':
                                line = save.read(4)
                                try:
                                    line = int(line)
                                except:
                                    True
                                    
                                for x in global_weapons:
                                    if x.ID == line:
                                        temp_weap.append(x)
                                        
                        elif line == 'item':
                            print('item')
                            while line != '---\n':
                                line = save.read(4)
                                try:
                                    line = int(line)
                                except:
                                    True
                                    
                                for y in global_items.values():
                                    for x in y:
                                        if x.ID == line:
                                            temp_item.append(x)
                                            
                        elif line == 'armo':
                            print('armo')
                            while line != '---\n':
                                line = save.read(4)
                                try:
                                    line = int(line)
                                except:
                                    True
                                    
                                for x in global_armor:
                                    if x.ID == line:
                                        temp_armo.append(x)
                        elif line == 'gold':
                            while line != '---\n':
                                line = save.read(4)
                                try:
                                    line = int(line)
                                except:
                                    break
                                else:
                                    gold = line
                                
                    team_1 = temp_team
                    held_weapons = temp_weap
                    held_items = temp_item
                    held_armor = temp_armo
                    