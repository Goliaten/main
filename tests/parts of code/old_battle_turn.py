        while True:
            print()
            print("what do you want to do?")
            print("1.Attack 2.Use item 3.Flee")
            a = input("choose a number: ")
            
            try:              #error checking
                a = int(a)
            except:
                print('Wrong input')
                continue
            else:
                if a < 0 or a > 3:
                    print('Choice out of range')
                    continue
            
            if a == 1:
                print()
                print('Prepare for attack')

                for x in team_1:                                                                         #player choosing target
                    if x == False:                         #if player is nonexistent choose another one
                        continue
                    if x.hp <= 0:                       #if player is dead choose another one
                        continue
                    print('Who does ' + x.name + ' attack? ')
                    team_target(2)                              #choosing target
                    p = team_2[o]                                           #defining p for class comment in deal_dmg
                    dmg = x.deal_dmg()
                    team_2[o].take_dmg(dmg)

                    e = fight_end_check()                                                       #breaking infinite while if hp<=0
                    if e == 'end':
                        print()
                        break
                if e == 'end':
                    break

            elif a == 2:
                print()
                z = 0
                while True:
                    
                    print('Available items:')
                    y = 0
                    for x in held_items:
                        print(str(y) + '. ' + x.stat_name + ' ' + x.fnc_name + ' ' + str(x.x))                     #printing held items
                        y += 1
                    
                    o = input('Choose (type "ex" to quit):')
                    
                    try:                             #error checking
                        o = int(o)
                    except:
                        if o == 'ex':
                            z = 1
                            break
                        else:
                            print('Wrong input')
                            print()
                            continue
                    else:
                        y -= 1
                        if o < 0 or o > y:
                            print('Choice out of range')
                            print()
                            continue
                    
                    held_items[o].use_item()
                    break
                if z == 1:                        #if typed 'ex' exit from inv choosing by doing whole turn loop again
                    continue
                
            elif a == 3:
                print("You fleed from battle")
                pause()
                print()
                break
            
            for x in team_2:
                if x == False:                #if fighter is nonexistend choose another
                    continue
                if x.hp <= 0:                      #if fighter is dead choose another one
                    continue
                o = random.randint(0,len(team_1)-1)                                                  #enemy choosing random target
                while team_1[o] == False or team_1[o].hp <= 0:
                    o = random.randint(0,len(team_1)-1)                                 #enemy choosing random target again if chose empty fighter place or fighter dead
                p = team_1[o]
                dmg = x.deal_dmg()
                team_1[o].take_dmg(dmg)
                
                
            e = fight_end_check()                  #checking if fight ended
            if e == 'end':
                break
            else:
                EoT_summ()                       #if not printing summary
                stat_print()
#
