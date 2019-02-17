input_mat=[[1,2,3],[4,5,6],[7,8,9]]

cost_mat=[[0 for i in range(len(input_mat))] for i in range(len(input_mat))]
for i in range(len(input_mat)):
    cost_mat[0][i]=input_mat[0][i]
for y in range(1,len(input_mat)):
    for x in range(len(input_mat)):
        left=x-1
        if left<0:
            left=0
        right=x+1
        if right>len(input_mat)-1:
            right=len(input_mat)-1
        
        cost_mat[y][x]=input_mat[y][x]+min( cost_mat[y-1][left], cost_mat[y-1][x], cost_mat[y-1][right] )
print(min(cost_mat[ len(input_mat)-1 ][i] for i in range(len(input_mat)) ))
