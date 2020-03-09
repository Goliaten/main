elif accept_cmsn.type == 'gathering':
    
    #convert mater list to 2d kill_counter-like list
    mater_counter = [[], []]
    for x in held_mater:
        if not x.ID in mater_counter[0]:
            mater_counter[0].append(x.ID)
            mater_counter[1].append(0)
        
        ind = mater_counter[0].index(x.ID)
        mater_counter[1][ind] += 1
        del ind
        
    #------------------------
    deliv_items = [[], []]
    for y, x in enumerate(accept_cmsn.prog_item):
        if x.ID in mater_counter[0]:                #if wanted material is held/owned
            cmsn_cnt = accept_cmsn.prog_item_cnt[y]         #get count of needed materials
            ind = mater_counter[0].index(x.ID)          #get index of held material
            cnt = mater_counter[1][ind]                 #get its count
            del_items = cnt if cnt < cmsn_cnt else cmsn_cnt  #calculate how many materials can be delivered
            
            deliv_items[0].append(x)                   #append ID and count of items that can be delivered
            deliv_items[1].append(del_items)
            del cmsn_cnt, ind, cnt, del_items
#         else:
#             deliv_items[0].append(x)
#             deliv_items[1].append(0)
    
    #------------------------
    temp_mater = num2char(deliv_items[0])
    out = 'You can deliver'
    for x, y in zip(temp_mater, deliv_items[1]):
        out += f'{y}x{x.name}'
    sec_menu.append(out)
    
    menu_print(temp_menu, 0, 0, sec_menu)
    o = input('Deliver these items(type "yes" to confirm) ') 
    
    if o == 'yes':
        mater_counter = list_sub_2d_id(mater_counter, deliv_items)
        
        mater_counter[0] = num2char(mater_counter[0])
        held_mater = []
        for x, y in mater_counter:
            for _ in range(y):
                held_mater.append(x)
            
        sec_menu += ['Items have been delivered.'
                    'Progress of comission will be updated.']
        
        menu_print(temp_menu, 0, 0, sec_menu)
    else:
        sec_menu.append('No progress has been made since last report.')
        
    del out, deliv_items, mater_counter
        
        