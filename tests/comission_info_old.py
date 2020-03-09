def cmsn_info(x, opt=0):
    ret = [f'Name: {x.name}',
                 f'Rank: {"If you see this remind me of this line"}',
                 f'Type: {x.type}']
    
    out = 'Completion requirement: '
    if x.type == 'hunt':          #if it's hunting comission
        out += 'kill'
        for k, z in enumerate(zip(x.cmpl_kill, x.cmpl_kill_cnt)):     #go over 2 lists and enumerate them
            z, l = z
            out += f' {l}x {z.name}'
            if k+1 < len(x.cmpl_kill):          #if there are more requirements in list
                out += ','                     #add a comma for style points
                
    elif x.type == 'assasination':
        out += 'assasinate'
        for k, z in enumerate(x.cmpl_kill):
            out += f' {z.name}'
            if k+1 < len(x.cmpl_kill):
                out += ','
                
    elif x.type == 'protection':
        pass
    
    elif x.type == 'gathering':
        out += 'deliver'
        for k, z in enumerate(zip(x.cmpl_item, x.cmpl_item_cnt)):     #go over 2 lists and enumerate them
            z, l = z
            out += f' {l}x {z.name}'
            if k+1 < len(x.cmpl_item):          #if there are more requirements in list
                out += ','                     #add a comma for style points
                
    elif x.type == 'raid':
        out += 'kill'
        for k, z in enumerate(zip(x.cmpl_kill, x.cmpl_kill_cnt)):     #go over 2 lists and enumerate them
            z, l = z
            out += f' {l}x {z.name}'
            if k+1 < len(x.cmpl_kill):          #if there are more requirements in list
                out += ','                     #add a comma for style points
                
        out += '; deliver'
        for k, z in enumerate(zip(x.cmpl_item, x.cmpl_item_cnt)):     #go over 2 lists and enumerate them
            z, l = z
            out += f' {l}x {z.name}'
            if k+1 < len(x.cmpl_item):          #if there are more requirements in list
                out += ','                     #add a comma for style points
    
                
    elif x.type == 'search':
        pass
    
    else:
        out += 'unknown target'
    
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