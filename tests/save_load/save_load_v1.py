##save

                with open('savefile.txt', 'w') as save:
                    for char in team_1:
                        save.write('char\n')
                        save.write(str(char.ID) + '\n')
                        save.write(str(char.weapon.ID) + '\n')
                        save.write(str(char.armor.ID) + '\n')
                        save.write('----\n')
                    for item in held_items:
                        save.write('item\n')
                        save.write(str(item.ID) + '\n')
                        save.write('----\n')
                    for weap in held_weapons:
                        save.write('weap\n')
                        save.write(str(weap.ID) + '\n')
                        save.write('----\n')
                    for armo in held_armor:
                        save.write('armo\n')
                        save.write(str(armo.ID) + '\n')
                        save.write('----\n')
                    save.write('gold\n')
                    save.write(str(gold) + '\n')
                    save.write('----\n')
                    

##load
                with open('savefile.txt', 'r') as save:
                    temp_team = []
                    temp_weap = []
                    temp_item = []
                    temp_armo = []
                    line = ' '
                    count = -1
                    while line != '':
                        line = save.readline()[:-1]
                        
                        if line == 'char':
                            count += 1
                            print('char')
                            while line != '----':
                                line = save.readline()[:-1]
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
                            while line != '----':
                                line = save.readline()[:-1]
                                try:
                                    line = int(line)
                                except:
                                    True
                                    
                                for x in global_weapons:
                                    if x.ID == line:
                                        temp_weap.append(x)
                                        
                        elif line == 'item':
                            print('item')
                            while line != '----':
                                line = save.readline()[:-1]
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
                            while line != '----':
                                line = save.readline()[:-1]
                                try:
                                    line = int(line)
                                except:
                                    True
                                    
                                for x in global_armor:
                                    if x.ID == line:
                                        temp_armo.append(x)
                        elif line == 'gold':
                            while line != '----':
                                line = save.readline()[:-1]
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
                    