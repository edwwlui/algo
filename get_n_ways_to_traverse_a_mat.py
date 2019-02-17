def get_n_ways_to_traverse_a_mat(length,width):
    if length==1 or width==1:
        return 1
    return get_n_ways_to_traverse_a_mat(length-1,width)+get_n_ways_to_traverse_a_mat(length,width-1)
get_n_ways_to_traverse_a_mat(5,5)
