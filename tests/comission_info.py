
def cmsn_info(x, opt=0):
    ret = [f'Name: {x.name}',
                 f'Rank: {"If you see this remind me of this line"}',
                 f'Type: {x.type}']
    
    out = 'Completion requirement: '
    
    if x.type in ['hunt', 'assasination', 'gathering', 'raid']:
        for lis in [[x.cmpl_kill, x.cmpl_kill_cnt], [x.cmpl_item, x.cmpl_item_cnt]]:    #going over all of completion requirements
            lis, lis_cnt = lis                            #unpacking (instances and count) list
            
            if lis:
                out += 'assasinate' if x.type == 'assasination' else ('hunt' if lis == x.cmpl_kill else 'deliver')  #outputting header(?) for requirements
                
            for k, z in enumerate(zip(lis, lis_cnt)):                           #going over instances and count list with enumerator
                z, l = z
                print(f'z: {z} l: {l}')
                out += f' {l}x {z.name}' if x.type != 'assasination' else f' {z.name}'  #outputting how many of z is needed or outputting just z if it's assasination
                if k+1 < len(lis):        #if enumerator isn't last, add comma
                    out += ','
            out += ' '
    else:
        pass
        
    ret.append(out)
    
    ret.append('Rewards: ' if (x.rew_gold or x.rew_items) else 'Rewards: None')  #add this to table if reward is present, else add that
    ret.append(f' gold:{x.rew_gold} ' if x.rew_gold else '')
    
    if x.rew_items:
        out = ''
        for l, z in enumerate(x.rew_items):
            if l == 0:
                out += f' {"items" if len(x.rew_items) > 1 else "item"}: '
            out += f'{z.name} '
            if l+1 < len(x.rew_items):
                out += ', '
        ret.append(out)
    
    return ret