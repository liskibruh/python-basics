import numpy as np

arr = np.array([[1,22,5],[11,22,6],[34,55,67]]) 

rows = arr.shape[0]
diagonal_sum_new=0
rev_diagonal_sum_new=0
var=rows-1

for i in range(0,rows):
	diagonal_sum_new=arr[i][i]+diagonal_sum_new
	rev_diagonal_sum_new=arr[i][var]+rev_diagonal_sum_new
	var = var-1

abs_diff = abs(diagonal_sum_new-rev_diagonal_sum_new)
print(abs_diff)