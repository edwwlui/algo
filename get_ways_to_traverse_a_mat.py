def get_ways_to_traverse_a_mat(n,m):
    if n==1 or m==1:
        return 1
    return get_ways_to_traverse_a_mat(n-1,m)+get_ways_to_traverse_a_mat(n,m-1)
get_ways_to_traverse_a_mat(5,5)
