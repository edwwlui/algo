def get_n_ways_to_change_coin(sum_value, list_coin):
    if sum_value==0:
        return 1
    if sum_value<0: 
        return 0
    if len(list_coin)<=0 and sum_value>0:
        return 0
    return get_n_ways_to_change_coin(sum_value-list_coin[0],list_coin)+\
            get_n_ways_to_change_coin(sum_value,list_coin[1:])
    
get_n_ways_to_change_coin(10,[2,5,3,6])
