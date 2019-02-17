def get_n_ways_to_change_coin_dp(list_coin, sum_value): 
  
    table = [0 for k in range(sum_value+1)] 
    table[0] = 1
    for i in range(0,len(list_coin)): 
        for j in range(list_coin[i],sum_value+1):            
            table[j] += table[ j - list_coin[i] ] 
            print("table[%s]: %s" %(str(j),str(table[j]))) 
    print(table)
    return table[sum_value] 
  
get_n_ways_to_change_coin_dp([2,5,3,6], 10) 
