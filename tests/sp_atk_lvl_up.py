def sp_atk_lvl_up(tree, src, count):
    out = []
	for y, x in enumerate(tree[count]):     #going over level of a tree      (y is spell family, x is spell level)
		if x != 0:                                     #0 means, that sp_atk is not gained
			x -= 1                                     #reducing, so that basic spell is 0
			
			if type(src[0]) == list:     #------custom---------
				out.append(deepcopy(src[y][x]))            #appending to skill_list deepcopy of a spell
			
			elif type(src[0]) == sp_skill:    #------default------- #if no new sp_atk gain order is defined
				n_sp_atk = src[y]   #creating new basic skill
				
				while x >= n_sp_atk.level and n_sp_atk.upgrade != None:   #upgrading it till it can't be upgraded anymore
					n_sp_atk = n_sp_atk.upgrade
					
				out.append(deepcopy(n_sp_atk))    #adding it to the list
    return out
