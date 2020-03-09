def fight(ally, enem):
    global team_1, team_2, o, p, all_fghtr, turn
    team_1 = ally
    team_2 = enem
    all_fghtr = team_1 + team_2
    turn = 0
    
    for x in all_fghtr:                    #heal for next battle
        if x == False:
            continue
        x.heal_up()

    for x in team_1:
        x.team = 'allies'
    for x in team_2:
        x.team = 'monsters'
    global held_items
    
    z = 0
    while z == 0:
        turn += 1
        for x in all_fghtr:
            while True:
                if x == False:
                    break
                if x.hp <= 0:
                    break
                if x.team == 'allies':
                    print(x.name + ' turn')
                    print("1.Attack 2.Use item 3.Flee")
                    a = input("choose a number: ")
                    
                    try:              #error checking
                        a = int(a)
                    except:
                        print('Wrong input')
                        continue
                    else:
                        if a <= 0 or a > 3:
                            print('Choice out of range')
                            continue
                    
                    if a == 1:
                        print('Who does ' + x.name + ' attack? ')
                        team_target(2)                              #choosing target
                        p = team_2[o]                                           #defining p for class comment in deal_dmg
                        dmg = x.deal_dmg()
                        team_2[o].take_dmg(dmg)
                        e = fight_end_check()
                        break
                    elif a == 2:
                        print('Available items:')
                        y = -1
                        for x in held_items:
                            y += 1
                            print(str(y) + '. ' + x.stat_name + ' ' + x.fnc_name + ' ' + str(x.x))
                        
                        o = input('Choose (type "ex" to quit):')
                            
                        try:                             #error checking
                            o = int(o)
                        except:
                            if o == 'ex':
                                z = 1
                                continue
                            else:
                                print('Wrong input')
                                print()
                                continue
                        else:
                            if o < 0 or o > y:
                                print('Choice out of range')
                                print()
                                continue
                        held_items[o].use_item()
                        break
                    elif a == 3:
                        print('You fleed from battle')
                        print()
                        z = 1
                        pause()
                        break
                elif x.team == 'monsters':
                    o = randint(0,len(team_1)-1)                                                  #enemy choosing random target
                    while team_1[o] == False or team_1[o].hp <= 0:
                        o = random.randint(0,len(team_1)-1)                                 #enemy choosing random target again if chose empty fighter place or fighter dead
                    p = team_1[o]
                    dmg = x.deal_dmg()
                    team_1[o].take_dmg(dmg)
                    e = fight_end_check()
                    break
            if e == 'end':
                z = 1
                break
        if z == 1:
            break
        EoT_summ()
        stat_print()
