def shop(items, weapons, armor, red=0):
    sell_red = red    #sell_reduction = percernage value reducing gold acquired from selling
    while True:
        print()
        print('Welcome to the shop')
        print('Current gold:' + str(gold))
        print('What do you want to do here?')
        print('1. Buy items')
        print('2. Sell items')
        print('3. Buy equipment')
        print('4. Sell equipment')
        print('5. Exit shop')
        
        a = input('Choose: ')
        
        try:
            a = int(a)
        except:
            print('Wrong input')
            print()
        else:
            if a < 1 or a > 5:
                print('Choice out of range')
                print()
        
        if a == 1:
            while True:
                print()
                print('Types of items available for sale:')
                y = -1
                d = []
                for x in items:
                    y += 1
                    print(y, '.', x)
                    d.append(x)
                o = input('Choose (type "ex" to quit): ')
                
                try:
                    o = int(o)
                except:
                    if o == 'ex':
                        z = 1
                        break
                    else:
                        print('Wrong input')
                        print()
                else:
                    if o > y or o < 0:
                        print('Choice out of range')
                        print()
                        continue
                    else:
                        z = 0
                        break
            l = o
            while z == 0:
                print()
                print('Which item do you want to buy?')
                y = -1
                v = items[d[l]]
                for x in v:
                    y += 1
                    print(str(y) + '. ' + x.stat_name + ' function:' + x.fnc_name + ' for:' + str(x.x) + ' cost:' + str(x.cost))
                o = input('Choose (type "ex" to quit): ')
                
                try:
                    o = int(o)
                except:
                    if o == 'ex':
                        break
                    else:
                        print('Wrond input')
                        print()
                else:
                    if o > y or o < 0:
                        print('Choice out of range')
                        print()
                        continue
                    else:
                        v[o].buy_item()
            pause()
        
        elif a == 2:
            while True:
                print()
                print('Value of items is reduced by ' + str(sell_red) + '% of basic cost')
                if held_items:
                    print('Your items:')
                    y = -1
                    for x in held_items:
                        y += 1
                        v = int(x.cost - x.cost * sell_red / 100)
                        print(str(y) + '. ' + x.stat_name + ': value:' + stat_len(v, 3, 1) + ' function:' + x.fnc_name + ' for:' + str(x.x))
                    o = input('Choose item for sale(type "ex" to quit): ')
                    try:
                        o = int(o)
                    except:
                        if o == 'ex':
                            break
                        else:
                            print('Wrong input')
                            continue
                    else:
                        if o < 0 or o > y:
                            print('Choice out of range')
                            continue
                    
                    held_items[o].sell_item(sell_red)
                    
                elif not held_items:
                    print("But it doesn't matter right now since you don't hold any item that can be sold")
                    pause()
                    break
        elif a == 3:
            while True:
                print('Equipment for sale:')
                y = -1
                d = []
                for x in global_equipment:
                    y += 1
                    print(str(y) + '. ' + x)
                    d.append(x)
                o = input('Choose (type "ex" to quit): ')
                try:
                    o = int(o)
                except:
                    if o == 'ex':
                        z = 1
                        break
                    else:
                        print('Wrong input')
                        print()
                else:
                    if o > y or o < 0:
                        print('Choice out of range')
                        print()
                        continue
                    else:
                        z = 0
                        break
            if z == 1:
                continue
            l = o
            v = global_equipment[d[l]]
            while z == 0:
                if v == weapons:
                    y = -1
                    for x in v:
                        y += 1
                        print(str(y) + '. ' + x.stat_name + ': cost:' + stat_len(x.cost, 3, 1) + ' damage:' + x.stat_dmg + ' variable:' + str(x.dmg_var))
    
                elif v == armor:
                    y = -1
                    for x in v:
                        y += 1
                        print(str(y) + '. ' + x.stat_name + ': cost:' + stat_len(x.cost, 3, 1) + ' defence:' + x.stat_defence)
                
                o = input('Choose(type "ex" to exit): ')
                try:
                    o = int(o)
                except:
                    if o == 'ex':
                        break
                    else:
                        print('Wrong inpuy')
                        continue
                else:
                    if o < 0 or o > y:
                        print('Choice out of range')
                        continue
                v[o].buy_equipment()
            
            print()
            pause()
        elif a == 4:
            while True:
                print()
                print('Value of equipment is reduced by ' + str(sell_red) + '% of basic cost')
                held_equipment = held_armor + held_weapons
                if held_equipment:
                    y = -1
                    for x in held_equipment:
                        y += 1
                        v = 0
                        if y == 0:
                            print('Held equipment:')
                        value = stat_len(int(x.cost - x.cost * sell_red / 100), 3, 1)
                        if type(x) == Weapon:
                            print(str(y) + '. ' + x.stat_name + ' value:' + value + ' damage:' + x.stat_dmg + '(' + str(x.dmg_var) + ')')
                            v += 1
                        else:
                            print(str(y) + '. ' + x.stat_name + ' value:' + value + ' defence:' + x.stat_defence)
                    
                    o = input('Choose equipment to sell(type "ex" to quit): ')
                    
                    try:
                        o = int(o)
                    except:
                        if o == 'ex':
                            break
                        else:
                            print('Wrong input')
                            continue
                    else:
                        if o < 0 or o > y:
                            print('Choice out of range')
                            continue
                        
                    if type(held_equipment[o]) == Weapon:
                        o -= v
                        held_weapons[o].sell_equipment()
                    else:
                        held_armor[o].sell_equipment()
                if not held_equipment:
                    print("But you don't have anything to sell")
                    break
                
        
        elif a == 5:
            print('You left the shop')
            break
