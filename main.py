import slau as sl


mat = [[-1, 2, 6], [3, -6, 0], [1, 0, 6]]
keys = [15, -9, 5]
mat_1 = [[4, -2], [6, 1]]
keys_1 = [22, 45]
mat_2 = [[3, -2], [5, 4]]
keys_2 = [6, 32]
mat_3 = [[2, 3, 5], [3, 7, 4], [1, 2, 2]]
keys_3 = [10, 3, 3]


#print(sl.is_diagonal_mat(mat))
print(sl.slau(mat, keys))
print(sl.slau(mat_1, keys_1))
print(sl.slau(mat_2, keys_2))
print(sl.slau(mat_3, keys_3))
