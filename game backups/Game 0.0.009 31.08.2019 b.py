from random import randint           #for random intiger (duh...)
from copy import deepcopy            #for copying class instances

#z is for while loops(used in error protection) AND another placeholder used in for loop (used first in fight_choose print)
#s is secondary for while loops(also used in error protection)
#o is for returns/data to be used outside of function AND targeting AND choices
#l is secondary/placeholder for choices
#p is secondary for targeting  AND better looking inventory prints(see item.buy_item) AND better looking class t_comm
#X AND Y AND W are for 'for' loops
#y is for counter in for loop
#v is for empty input(not in pause func) AND a placeholder
#c is for choosing which option of function run
#a is for choosing what to do(in wide/main function)
#d is for choosing in dictionaries(see shope>buy items)
#p is for better looking inventory prints(see item.buy_item)

#function zone

#function zone

def pause():
    emptyinput = input("Press anything to continue ")      #function for pausing

def sortid(y):    #ey used in sorting
    return y.ID

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
        

def stat(char, c=0):
    if c == 0:                   #displays statictics
        print(char.stat_name + '- health:' + char.stat_hp + '/' + char.stat_maxhp + ' attack:' + char.atkmin + '-' + char.atkmax + ' total defence:' + char.stat_defence)
    elif c == 1:             #displays statistics with weapons and armor
        x = ''
        if char.weapon == basic and char.armor == basal:
            x = stat_len(x, 18, 1)
            print(char.stat_name + '- health:' + char.stat_hp + '/' + char.stat_maxhp + ' attack:' + char.atkmin + '-' + char.atkmax + ' total defence:' + char.stat_defence + ' armor:' + char.armor.stat_name + x + ' weapon:' + char.weapon.stat_name)
        elif char.weapon != basic and char.armor == basal:
            x = stat_len(x, 18, 1)
            print(char.stat_name + '- health:' + char.stat_hp + '/' + char.stat_maxhp + ' attack:' + char.atkmin + '-' + char.atkmax + ' total defence:' + char.stat_defence + ' armor:' + char.armor.stat_name + x + ' weapon:' + char.weapon.stat_name + ' dmg:' + str(char.weapon.dmg) + ' var:' + str(char.weapon.dmg_var))
        elif char.weapon == basic and char.armor != basal:
            print(char.stat_name + '- health:' + char.stat_hp + '/' + char.stat_maxhp + ' attack:' + char.atkmin + '-' + char.atkmax + ' total defence:' + char.stat_defence + ' armor:' + char.armor.stat_name + ' armor defence:' + char.armor.stat_defence + ' weapon:' + char.weapon.stat_name)
        else:
            print(char.stat_name + '- health:' + char.stat_hp + '/' + char.stat_maxhp + ' attack:' + char.atkmin + '-' + char.atkmax + ' total defence:' + char.stat_defence + ' armor:' + char.armor.stat_name + ' armor defence:' + char.armor.stat_defence + ' weapon:' + char.weapon.stat_name + ' dmg:' + str(char.weapon.dmg) + ' var:' + str(char.weapon.dmg_var))


def EoT_summ():                                      #End of Turn summary
    print()
    print('Turn ' + str(turn) + ' summary:')
    for x in all_fghtr:      #prints what character did in a turn
        if x == False:
            continue
        print(x.t_comm)
        if x.hp <= 0:
            x.t_comm = x.name + ' died'
        else:
            x.t_comm = x.name + ' did not do a thing'

def stat_print(c=0):                # 0=print everyone, 1=print friendly team, 2=print enemy team, 3=print more about friendly team
    print()
    if c==0 or c==1 or c==3:
        for x in team_1:
            if x == False:
                continue
            if c==3:
                stat(x, 1)
            else:
                stat(x)
    if c==0 or c==2:
        for x in team_2:
            if x == False:
                continue
            stat(x)

def team_target(c):        #used for choosing target
    global o          #no returns instead working on global o
    z = 0
    if c==1:               #target is team_1
        while True:
            y = -1
            for x in team_1:
                if x == False:
                    continue
                if x.hp <= 0:         #can't target for attack/buff/debuff/heal deadman (not here at least)
                    y += 1
                    continue
                y += 1
                print(str(y) + '. ' + x.stat_name + ' ' + x.stat_hp + '/' + x.stat_maxhp)            #printing team_1 members with indexes
                
            o = input('Choose: ')
            
            try:                     #error check
                o = int(o)
            except:
                print('Wrong input')
                print()
                continue
            else:
                if o < 0 or o > y:
                    print('Choice out of range')
                    print()
                    continue
                else:
                    if team_1[o].hp <= 0:
                        print(team_1[o].name + ' is already dead')
                        p = input('Do you want to attack a dead body?(type "yes" to confirm) ')
                        if p == 'yes':
                            break
                        else:
                            continue
                    else:
                        break
                    
    if c==2:
        while True:
            y = -1
            for x in team_2:
                if x == False:
                    continue
                if x.hp <= 0:      #can't target for attack/buff/debuff/heal deadman (not here at least)  ######actually you can
                    y += 1
                    continue
                y += 1
                print(str(y) + '. ' + x.stat_name + ' ' + x.stat_hp + '/' + x.stat_maxhp)   #printing team_1 members with indexes
                
            o = input('Choose: ')
            
            try:           #error check
                o = int(o)
            except:
                print('Wrong input')
                print()
                continue
            else:
                if o < 0 or o > y:
                    print("Choice out of range")
                    print()
                    continue
                else:
                    if team_2[o].hp <= 0:
                        print(team_2[o].name + ' is already dead')
                        p = input('Do you want to attack a dead body?(type "yes" to confirm) ')
                        if p == 'yes':
                            break
                        else:
                            continue
                    else:
                        break

def fight_end(c, y=0):            #c is just to choose which side won, y is for gold obtained input
    if c == 1:         #if team_1 won
        if y == 0:                #if gold is not specified
            v = 0
            for x in team_2:         #get gold gained from monster gold_drop
                if x == False:
                    continue
                v += x.g_drop
            stat_print()
            print('You won the fight')       #print some info
            print('You gained ' + str(v) + 'g old')
            global gold
            gold += v     #add gained gold
        elif y != 0:        #if gold was specified
            stat_print()
            print('You won the fight')
            print('You gained ' + str(y) + ' gold')
            gold += y        #gain set amount f gold
    if c == 2:        #if team_2 won
        stat_print()
        print('You lost the fight')
        print('What a shame...')
        print()
        
def fight_end_check(v=0):          #checking if battle ended V is for setting gold gained
    x = 0
    for y in team_1:
        if y == False:
            continue
        x += y.hp       #summing up hp of team_1 fighters
    if x <= 0:     #if it's less or equal than 0
        EoT_summ()    #summarise the turn
        fight_end(2)    #use <- function
        return 'end'    #used for breaking loops
    
    x = 0
    for y in team_2:
        if y == False:
            continue
        x += y.hp       #summng hp of team_2 fighters
    if x <= 0:   #if it's less or equal 0
        EoT_summ()    #summarise turn
        fight_end(1, v)   #use <- function with v for gained g
        return 'end'   #used for breaking loops

def fight(ally, enem, g_gain=0):
    global team_1, team_2, o, p, all_fghtr, turn, held_items, l
    team_1 = ally          #setting teams from input
    team_2 = enem
    all_fghtr = team_1 + team_2   #ading all fighters to a list
    turn = 0
    
    for x in all_fghtr:                    #heal for next battle
        if x == False:
            continue
        x.heal_up()

    for x in team_1:        #setting variable for turn fighting
        x.team = 'allies'
    for x in team_2:
        x.team = 'monsters'
    
    e = ''  #for end check
    z = 0
    s = 0
    while z == 0:
        print()
        turn += 1
        print('Turn: ' + str(turn))
        
        for x in all_fghtr:
            while z == 0:
                if x == False or x.hp <= 0:
                    break
                if x.team == 'allies':
                    print()
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
                        dmg = x.deal_dmg()                              #setting damage
                        team_2[o].take_dmg(dmg)                 #target receiving damage
                        e = fight_end_check(g_gain)      #end check
                        break
                    elif a == 2:
                        print('Available items:')
                        y = -1
                        for w in held_items:
                            y += 1
                            print(str(y) + '. ' + w.stat_name +': function:' + w.fnc_name + ' for:' + str(w.x))
                        
                        l = input('Choose (type "ex" to quit): ')
                            
                        try:                             #error checking
                            l = int(l)
                        except:
                            if l == 'ex':
                                continue
                            else:
                                print('Wrong input')
                                print()
                                continue
                        else:
                            if l < 0 or l > y:
                                print('Choice out of range')
                                print()
                                continue
                                
                        held_items[l].use_item()
                        e = fight_end_check(g_gain)
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
                    e = fight_end_check(g_gain)
                    break
            if e == 'end':
                z = 1
                break
        if z == 1:
            break
        EoT_summ()
        stat_print()

#item function
def heal(x, c=0):
    print("Who do you want to heal? ")
    team_target(1)
    if c == 0:
        y = team_1[o]
    elif c == 1:
        y = team_2[o]
    v = y.hp                                      #for print measures
    y.hp += x
    
    if y.hp > y.maxhp:                     #prevent overheal
        y.hp = y.maxhp
    y.stat_hp = stat_len(y.hp, 3, 1)
    
    l = y.hp                                      #for print measures
    print(y.name + ' has been healed for ' + str(l-v) + ' health up to current ' + str(y.hp) + ' health points')

class Effect:           #consider doing deepcopies of it so multiple instances of the same effects can stack
    def __init__ (self, dur, fnc, x):
        self.dur = dur    #duration
        self.fnc = fnc    #function
        self.x = x        #use in funcion
    def start(self, char, dur=0):
#         self.bturn = turn     #turn that effect had begun
        if dur != 0:
            self.dur = dur
#         self.time = dur
        self.fnc(self.x, char, 1)   #1 being option to begin effect
    def check(self):
#         self.fnc(self.x)         #no secong arg to check for effect(if exists)
#         self.time -= 1     #time left
        if self.time == 0:
            self.end()
    def end(self):
        self.fnc(self.x, char, 2)   #2 being option to cancel effect(weaken/strengthen)
        del active_effects[key]


def atk_upp(x, char, c=0):
    if c == 1:   #start
        char.atk += x
        char.atkmin = stat_len(int(char.atkmin)+x, 2, 1)
        char.atkmax = stat_len(int(char.atkmax)+x, 2, 1)
        
    elif c == 2:   #end
        char.atk -= x
    else:    #checkk
        True

atk_buff = Effect(5, atk_upp, 0)
#_effect_fnc_

active_effects = {}
buff_count = 0

#_item_fnc_
def atk_up(x):            #works only for team_1
    global buff_count
    buff_count += 1        #for creating keys
    key = str(buff_count)  #creating new key
    active_effects[key] = deepcopy(atk_buff)    #making copy of effect+adding it to active_effects
    active_effects[key].x = x       #assigning new x
    active_effects[key].key = key    #giving effect it's place in active effects to manipulate itself
    team_target(1)
    v = team_1[o]         #choosing target for effect
    active_effects[key].start(v)     #giving target to effect and starting it

#at the end of each turn for x in active_buffs.values(): x.check()

class Weapon:
    ID = 1000
    def __init__ (self, name, cost, dmg, dmg_var, dmg_type_1, dmg_type_2='none'):
        self.name = name
        self.stat_name = stat_len(name, 10)   #for stat purpose
        Weapon.ID += 1
        self.ID = Weapon.ID       #for sorting
        
        self.cost = cost
        self.dmg = dmg
        self.stat_dmg = stat_len(dmg, 2, 1)   #for stat purpose
        self.dmg_var = dmg_var
        
        self.dmg_type_1 = dmg_type_1
        self.dmg_type_2 = dmg_type_2
    def equip(self, char):
        char.weapon = self
        char.atk += self.dmg
        char.atk_var += self.dmg_var
        
        char.atkmin = char.atk - char.atk_var           #atkmin and atkmax are for status display
        char.atkmax = char.atk + char.atk_var
        char.atkmin = stat_len(char.atkmin, 2, 1)       # adding spaces for nicer comment(stat)
        char.atkmax = stat_len(char.atkmax, 2)
        
        char.dmg_type_1 = self.dmg_type_1         #for future elemental system
        char.dmg_type_2 = self.dmg_type_2
    def buy_equipment(self):
        global gold          #accesing held gold outside of function
        p = 'Are you sure you want to buy: ' + self.name + '? (type "yes" to confirm) '
        a = input(p)
        if a == 'yes':
            if gold >= self.cost:        #checking if enough gold is held
                gold -= self.cost
                held_weapons.append(self)    #adding itself to held weapons
                
                print('You bought ' + self.name)
                print('You currently have ' + str(gold) + 'gold')
                
                p = 'You are currently holding '
                held_weapons.sort(key = sortid)        #sorting held weapons
                for x in held_weapons:
                    p = p + x.name + ', '           #and displaying all of them
                print(p)
            else:
                print('You do not have enough gold')
    def sell_equipment(self):
        global gold, held_weapons
        p = 'Are you sure you want to sell: ' + self.name + '? (type "yes" to confirm) '
        a = input(p)
        if a == 'yes':
            g_gained = int(self.cost - self.cost * sell_red / 100)
            gold += g_gained
            held_weapons.pop(o)
            print('You sold ' + self.name + ' and gained ' + str(g_gained) + ' gold')
            
            

class Armor:
    ID = 1500
    def __init__(self, name, cost, defence, defence_type='none'):
        self.name = name
        self.stat_name = stat_len(name, 10)   #for stat purpose
        Armor.ID += 1
        self.ID = Armor.ID  #for sorting
        
        self.cost = cost
        self.defence = defence
        self.stat_defence = stat_len(defence, 2, 1)   #for stat purpose
        self.defence_type = defence_type
    def equip(self, char):
        char.armor = self
        char.defence += self.defence
        if char.defence_type_1 =='none':        #for future elemental system
            char.defence_type_1 = self.defence_type
        else:
            char.defence_type_2 = self.defence_type
        char.stat_defence = stat_len(char.defence, 3, 1)    #for stat purpose
    def buy_equipment(self):
        global gold          #accesing held gold outside of function
        p = 'Are you sure you want to buy: ' + self.name + '? (type "yes" to confirm) '
        a = input(p)
        if a == 'yes':
            if gold >= self.cost:        #checking if enough gold is held
                gold -= self.cost
                held_armor.append(self)    #adding itself to held armor
                
                print('You bought' + self.name)
                print('You currently have' + str(gold) + 'gold')
                
                p = 'You are currently holding '
                held_armor.sort(key = sortid)        #sorting held armor
                for x in held_armor:
                    p = p + x.name + ', '           #and displaying all of it
                print(p)
            else:
                print('You do not have enough gold')
    def sell_equipment(self):
        global gold, held_armor
        p = 'Are you sure you want to sell: ' + self.name + '? (type "yes" to confirm) '
        a = input(p)
        if a == 'yes':
            g_gained = int(self.cost - self.cost * sell_red / 100)
            gold += g_gained
            held_armor.pop(o)
            print('You sold ' + self.name + ' and gained ' + str(g_gained) + ' gold')
            

#-----Weapon-----
basic = Weapon('None', 0, 0, 0, 'blunt')        #(name, cost, dmg, dmg_var, dmg_type_1, dmg_type_2='None')
bat = Weapon('Bat', 50, 1, 1, 'blunt')
sword = Weapon('Sword', 150, 4, 0, 'slash')
hammer = Weapon('Hammer', 120, 3, 1, 'blunt')

imp_bas_wep = Weapon('None', 0, 0, 0, 'slash')
imp_lig_wep = Weapon('Light', 0, 1, 2, 'slash', 'fire')
imp_med_wep = Weapon('Medium', 0, 2, 3, 'blunt', 'fire')
imp_goo_wep = Weapon('Good', 0, 4, 0, 'pierce')

global_weapons = [bat, sword, hammer]   #for shop display
global_weapons.sort(key = sortid)

#-----Armor------
basal = Armor('None', 0, 0)  #name cost defence defence_type='none'
light = Armor('Light', 50, 2)
medial = Armor('Medial', 120, 4)
heavy = Armor('Heavy', 250, 6)

imp_bas_arm = Armor('None', 0, 0)
imp_lig_arm = Armor('Light', 0, 1)
imp_med_arm = Armor('Medium', 0, 3)
imp_goo_arm = Armor('Good', 0, 5)
imp_vgo_arm = Armor('Very good', 0, 8, 'shadow')

global_armor = [light, medial, heavy]  #for shop display
global_armor.sort(key = sortid)

global_equipment = {
    'Weapons': global_weapons,
    'Armor': global_armor
    }

held_weapons = [sword]
held_armor = [light]

class Char:
    def __init__ (self, name, maxhp, atk, atk_var, g_drop=0, defence=0, defence_type_1='none', weapon=basic, armor=basal):
        self.name = name
        self.stat_name = stat_len(name, 12)         #for stat purpose
        self.maxhp = maxhp
        self.hp = maxhp
        self.stat_maxhp = stat_len(self.maxhp, 3)       #for stat purpose
        self.stat_hp = stat_len(self.hp, 3, 1)      #for stat purpose
        
        self.atk = atk
        self.g_drop = g_drop                                                   #gold drop variable
        
        self.defence = defence                             #setting base for armor
        self.stat_defence = stat_len(self.defence, 3, 1)    #for stat purpose
        self.defence_type_1 = defence_type_1       #future elemental system?
        self.defence_type_2 = 'none'
        self.armor = armor
        armor.equip(self)
        
        self.atk_var = atk_var                                                 #attack variable
        self.atkmin = atk - atk_var
        self.atkmax = atk + atk_var
        self.atkmin = stat_len(self.atkmin, 2, 1)       #for stat purpose
        self.atkmax = stat_len(self.atkmax, 2)      #for stat purpose
        
#         self.dmg_type_1 = dmg_type_1                                     #damage type for future(?) elemental system
#         self.dmg_type_2 = dmg_type_2                #these are defined by weapon.equip() and char.unequip weapon() and same for armor
        
        self.base_maxhp = maxhp         #base/starting values for when something will bet out of control
        self.base_atk = atk
        self.base_armor = armor
        self.base_atk_var = atk_var
        
        self.t_comm = self.name + ' did not have a chance to attack'          #turn comment
        self.weapon = weapon
        weapon.equip(self)
    def take_dmg (self, damage):
        self.hp -= damage
        if self.hp < 0:                             #health can't be lower than zero
            self.hp = 0
        self.stat_hp = stat_len(self.hp, 3, 1)      #for stat purpose
    def deal_dmg (self):
        atk_var = randint(0,self.atk_var*2) - self.atk_var             #making variable for damage
        atk_dmg = self.atk + atk_var - p.defence                                          #calculating damage from atk and variable
        if atk_dmg <= 0:
            atk_dmg = 0
            self.t_comm = (self.name + ' dealt no damage to ' + p.name)                     #turn comment used in EoT_summ
        else:
            self.t_comm = (self.name + ' dealt ' + str(atk_dmg) + ' damage to ' + p.name)                      #turn comment used in EoT_summ
        return atk_dmg
    def heal_up(self):
        self.hp = self.maxhp
        self.stat_hp = stat_len(self.hp, 3, 1)  #for stat purpose
    def unequip_weapon(self):
        self.atk -= self.weapon.dmg
        self.atk_var -= self.weapon.dmg_var
        
        self.atkmin = self.atk - self.atk_var
        self.atmax = self.atk + self.atk_var
        self.atkmin = stat_len(self.atkmin, 2, 1)   #for stat purpose
        self.atkmax = stat_len(self.atkmax, 2)  #for stat purpose
        
        self.dmg_type_1 = 'blunt'
        self.dmg_type_2 = 'none'
        basic.equip(self)
    def unequip_armor(self):
        self.defence -= self.armor.defence
        self.stat_defence = stat_len(self.defence, 3, 1)    #for stat purpose
        if self.defence_type_2 != 'none':   #future elemental system?
            self.defence_type_2 = 'none'
        else:
            self.defence_type_1 = 'none'
        if self.armor != basal:
            held_armor.append(self.armor)
        basal.equip(self)
            

class Item:
    ID = 100
    def __init__ (self, name, cost, fnc_name, fnc, x):
        #fnc is a function, that said item will do. These functions have to be defined.
        self.name = name
        self.stat_name = stat_len(name, 10) #for stat purpose
        Item.ID += 1
        self.ID = Item.ID   #for sorting
        self.cost = cost
        
        self.fnc_name = stat_len(fnc_name, 5)   #for stat purpose
        self.fnc = fnc
        self.x = x
    def use_item (self):
        global held_items
        self.fnc(self.x)    #using function assigned to itself
        held_items.pop(l)   #deleting self from list
    def buy_item (self):
        global gold          #accesing held gold outside of function
        p = 'Are you sure you want to buy: ' + self.name + '? (type "yes" to confirm) '
        a = input(p)
        if a == 'yes':
            if gold >= self.cost:        #checking if enough gold is held
                gold -= self.cost
                held_items.append(self)    #adding itself to held items
                
                print('You bought' + self.name)
                print('You currently have' + str(gold) + 'gold')
                
                p = 'You are currently holding '
                held_items.sort(key = sortid)        #sorting held items
                for x in held_items:
                    p = p + x.name + ', '           #and displaying all of them
                print(p)
            else:
                print('You do not have enough gold')
    def sell_item(self):     #red == value reduction
        global gold, held_items
        p = 'Are you sure you want to sell: ' + self.name + '? (type yes to confirm) '
        a = input(p)
        if a == 'yes':
            g_gained = int(self.cost - self.cost * sell_red / 100)
            gold += g_gained
            held_items.pop(o)
            print('You sold ' + self.name + ' and gained ' + str(g_gained) + ' gold')

print('Functions defined')

#weapons are defined with class
#----items----
potion = Item('Potion', 12, 'heal', heal, 10)        #Item(name, cost, fnc_name, fnc, x(fnc_attrib)) 
potionv1 = Item('Potion v1', 23, 'heal', heal, 20)
potionv2 = Item('Potion v2', 45, 'heal', heal, 30)

atk_potion = Item('Atk_pot', 100, 'atk_up', atk_up, 4)

held_items = [potionv1, atk_potion]                      #defining held items
healing_items = [potionv1, potion, potionv2]        #defining list of healing items
healing_items.sort(key = sortid)


global_items = {                                            #using dictionary for easier manipulation
    'Healing items': healing_items
    }

gold = 100

#----Characters----
Hero = Char('Hero', 70, 10, 1)        #name maxhp atk atk_var g_drop=0 defence=0 defence_type='none' weapon=basic armor='basic'
Champion = Char('Champion', 90, 9, 2)

monster = Char('Monster', 120, 8, 0, 50, armor=light)
demon = Char('Demon', 40, 12, 4, 50, armor=light)

imp_1 = Char('Lesser Imp', 40, 4, 2, 20, 0, 'Subdemon', imp_bas_wep, imp_bas_arm)
imp_2 = Char('Imp Servant', 40, 4, 2, 30, 0, 'Subdemon', imp_lig_wep, imp_lig_arm)
imp_3 = Char('Imp', 60, 7, 1, 50, 0, 'Subdemon', imp_lig_wep, imp_lig_arm)
imp_4 = Char('Imp Soldier', 60, 7, 1, 60, 0, 'Subdemon', imp_med_wep, imp_med_arm)
imp_5 = Char('Higher Imp', 120, 10, 0, 100, 0, 'Demon', imp_lig_wep, imp_med_arm)
imp_6 = Char('Imp General', 120, 10, 0, 150, 0, 'Demon', imp_med_wep, imp_goo_arm)
imp_7 = Char('Imp Outcast', 120, 10, 0, 220, 0, 'Demon', imp_goo_wep, imp_vgo_arm)

# team_1 = [imp_1,imp_2,imp_3,imp_4,imp_5,imp_6,imp_7]
# team_1 = [Hero, Champion]                                                  #defining team 1
# team_2 = [imp_7]                                                  #defining team 2
# all_fghtr = team_1 + team_2
    #defining battle teams

#----Character-copies----
imp_1b = deepcopy(imp_1)      #copying class instance
imp_2b = deepcopy(imp_2)
imp_3b = deepcopy(imp_3)
imp_4b = deepcopy(imp_4)
imp_4c = deepcopy(imp_4)
imp_5b = deepcopy(imp_5)
imp_5c = deepcopy(imp_5)
imp_6b = deepcopy(imp_6)

#----fighting-groups----
allies = [Hero, Champion]
enem_1 = [imp_2, imp_1, imp_1b]      #remember to define more of the same char type as different entities(deepcopy)
enem_2 = [imp_3, imp_2, imp_1]
enem_3 = [imp_3, imp_3b]
enem_4 = [imp_4, imp_2, imp_2b]
enem_5 = [imp_4, imp_4b, imp_4c]
enem_6 = [imp_5, imp_3, imp_3b]
enem_7 = [imp_6, imp_4, imp_4b]
enem_8 = [imp_5, imp_5b, imp_5c]
enem_9 = [imp_6, imp_6b, imp_5]
enem_10 = [imp_7]
all_enem_fight = [enem_1, enem_2, enem_3, enem_4, enem_5, enem_6, enem_7, enem_8, enem_9, enem_10]

team_1 = allies     #needs to be defined for info display
print("defined")

while True:
    print('What do you want to do?')
    print('1.Fight a monster')
    print('2.Go to shop')
    print('3. Check items/character')
    a = input("Choose: ")
    
    try:              #error checking
        a = int(a)
    except:
        print('Wrong input')
        print()
    else:
        if a < 1 or a > 3:
            print('Choice out of range')
            print()
            continue

    if a == 1:
        while True:
            print()
            print('Available fights:')
            y = -1
            for x in all_enem_fight:
                y += 1
                v = stat_len(y, 2, 1) + '. enemies: '
                for z in x:
                    v += z.stat_name + ' ,'
                print(v)
                
            o = input('Choose one that you wish to participate(type "ex" to quit): ')
            
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
            
            fight(allies, all_enem_fight[o])
                 
    elif a == 2:
        sell_red = 10    #sell_reduction = percernage value reducing gold acquired from selling
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
                    for x in global_items:
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
                    v = global_items[d[l]]
                    for x in v:
                        y += 1
                        print(str(y) + '. ' + x.stat_name + ' function:' + x.fnc_name + ' for:' + str(x.x) + 'cost:' + str(x.cost))
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
                    if v == global_weapons:
                        y = -1
                        for x in v:
                            y += 1
                            print(str(y) + '. ' + x.stat_name + ': cost:' + stat_len(x.cost, 3, 1) + ' damage:' + x.stat_dmg + ' variable:' + str(x.dmg_var))

                    elif v == global_armor:
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
            
    elif a == 3:
        while True:
            print()
            print('What do you want to do?')
            print('1. Display information')
            print('2. Equip weapons')
            print('3. Unequip weapons')
            print('4. Equip armor')
            print('5. Unequip armor')
            print('6. Exit')
            
            a = input('Choose: ')
            
            try:
                a = int(a)
            except:
                print('Wrong input')
                continue
            else:
                if a < 0 or a > 6:
                    print('Choice out of range')
                    continue
            
            if a == 1:
                print('Your current team consists of:')
                stat_print(3)                     #printing extended stats
                print()
                
                print('Currently held items: ')
                if held_items:                             #printing extended items
                    for x in held_items:
                        print(' ' + x.stat_name + ': function:' + x.fnc_name + ' for:' + str(x.x))
                        print(x.ID)
                elif not held_items:
                    print("You don't hold any items in your inventory")
                print()
                
                if held_weapons:
                    print('Currently held weapons:')
                    for x in held_weapons:              #printing weapon stats
                        print(' ' + x.stat_name + ': damage:' + x.stat_dmg + '(' + str(x.dmg_var) + ') ' + x.dmg_type_1 + ' ' + x.dmg_type_2)
                elif not held_weapons:
                    print('No weapons are being held in inventory')
                    
                if held_armor:
                    print('Currently held armor:')
                    for x in held_armor:
                        print(' ' + x.stat_name + ': defence:' + x.stat_defence + ' defence type:' + x.defence_type)
                elif not held_armor:
                        print('No armor is being held in inventory')
                        
            elif a == 2 or a == 4:
                while True:
                    print()
                    if a == 2:
                        if held_weapons:         #if you hav any weapon in eq
                            y = -1
                            print('Currently held weapons:')
                            for x in held_weapons:                 #printing weapons with stats
                                y += 1
                                print(' ' + str(y) + '. ' + x.stat_name + ': damage:' + x.stat_dmg + '(' + str(x.dmg_var) + ') ' + x.dmg_type_1 + ' ' + x.dmg_type_2)
                            o = input('Choose weapon to equip(type "ex" to exit) ')
                            
                        else:
                            print("You don't hold any weapons in inventory")
                            break
                    else:
                        if held_armor:
                            y = -1
                            print('Currently held armor:')
                            for x in held_armor:
                                y += 1
                                print(' ' + str(y) + '. ' + x.stat_name + ': defence' + x.stat_defence + ' defence type:' + x.defence_type)
                            o = input('Choose armor to equip(type "ex" to exit) ')
                            
                        else:
                            print("Youd don't any armor in inventory")
                            break
                        
                    try:
                        o = int(o)
                    except:
                        if o == 'ex':
                            print()
                            break
                        else:
                            print('Wrong input')
                            continue
                    else:
                        if o < 0 or o > y:
                            print('Choice out of range')
                            
                    y = -1
                    for x in team_1:                         #printing char with info about weapon
                        if x == False:
                            continue
                        y += 1
                        if a == 2:
                            if x.weapon == basic:
                                print(' ' + str(y) + '. ' + x.stat_name + ' current weapon: ' + x.weapon.stat_name)
                            else:
                                print(' ' + str(y) + '. ' + x.stat_name + ' current weapon: ' + x.weapon.stat_name + ' damage:' + x.weapon.stat_dmg + '(' + str(x.weapon.dmg_var) + ')')
                        else:
                            if x.armor == basal:
                                print(' ' + str(y) + '. ' + x.stat_name + ' current armor: ' + x.armor.stat_name)
                            else:
                                print(' ' + str(y) + '. ' + x.stat_name + ' current armor: ' + x.armor.stat_name + ' defence:' + x.armor.stat_defence + ' defence type:' + x.armor.defence_type)
                    if a == 2:
                        l = input('Choose character that will wield this weapon(type "ex" to exit) ')
                    else:
                        l = input('Choose character that will wear this armor(type "ex" to exit) ')
                    
                    try:
                        l = int(l)
                    except:
                        if l == 'ex':
                            print()
                            break
                        else:
                            print('Wrong input')
                            continue
                    else:
                        if l < 0 or l > y:
                            print('Choice out of range')
                            continue
                            
                    
                    if a == 2 and team_1[l].weapon != basic:                         #if char already has a weapon
                        print(team_1[l].name + ' already has a ' + team_1[l].weapon.name + ' equipped')
                        x = input('Do you want to unequip ' + team_1[l].weapon.name + ' and equip ' + held_weapons[o].name + '? (yes to confirm) ')
                        if x != 'yes':         #only yes will allow  to equip a weapon
                            continue
                    elif a == 4 and team_1[l].armor != basal:
                        print(team_1[l].name + ' already wears ' + team_1[l].armor.name + ' armor')
                        x = input('Do you want to unequip ' + team_1[l].armor.name + ' armor and equip ' + held_armor[o].name + ' armor? (yes to confirm) ')
                        if x != 'yes':
                            continue
                    if a == 2:
                        v = team_1[l].weapon                                 #settin placeholder for weapon
                        team_1[l].unequip_weapon()                  #unequipping weapon old
                        
                        held_weapons[o].equip(team_1[l])            #equipping new weapon
                        print(team_1[l].name + ' now wields ' + held_weapons[o].name)     #comment
                        
                        held_weapons.pop(o)            #deleting new weapon from held weapons
                        if v != basic:             #if old weapon existed(wasnt basic)
                            held_weapons.append(v)                    #add old weapon to held weapons
                        held_weapons.sort(key = sortid)
                    else:
                        v = team_1[l].armor             #setting placeholder for armor
                        team_1[l].unequip_armor()           #unequipping old armor
                        
                        held_armor[o].equip(team_1[l])      #equipping new one
                        print(team_1[l].name + ' now wears ' + held_armor[o].name)  #comment
                        
                        held_armor.pop(o)           #deleting new one from held armor
                        if v != basal:          #if old weapon wasn't basal(was normal armor)
                            held_armor.append(v)            #add old one to held armor
                        held_armor.sort(key = sortid)       #sort

                
            elif a == 3 or a == 5:
                while True:
                    print()
                    y = -1
                    v = []
                    for x in team_1:
                        if x == False:
                            continue
                        if a == 3 and x.weapon == basic:       #if holds basic weapon then doesnt count
                            continue
                        elif a == 5 and x.armor == basal:
                            continue
                        v.append(x)
                        y += 1
                        if y == 0:
                            if a == 3:
                                print('Characters currently wielding a weapon:')
                            if a == 5:
                                print('Characters with their armor equipped:')
                        if a == 3:
                            print(str(y) + '. ' + x.stat_name + ': ' + x.weapon.stat_name + ' damage:' + x.weapon.stat_dmg + '(' + str(x.weapon.dmg_var) + ')')
                        if a == 5:
                            print(str(y) + '. ' + x.stat_name + ': ' + x.armor.stat_name + ' defence:' + x.armor.stat_defence)
                    if y == -1:
                        if a == 3:
                            print('None of your characters hold a weapon')
                            break
                        if a == 5:
                            print('None of your characters is armored')
                    if a == 3:
                        print('Choose one that will unequip his weapon')                    
                    if a == 5:
                        print('Choose one that will take off his armor')
                        
                    o = input('Choose(type "ex" to quit): ')
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
                    if a == 3:
                        held_weapons.append(v[o].weapon)       #adding ld weapon to eq
                        held_weapons.sort(key = sortid)      #sorting
                        v[o].unequip_weapon()               #unequipping weapon
                    elif a == 5:
                        held_armor.append(v[o].armor)
                        held_armor.sort(key = sortid)
                        v[o].unequip_armor()

            elif a == 6:
                print()
                break