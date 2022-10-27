import slau as sl
import matrix as m


mat = [[1, 2, 1], [3, -5, 3], [2, 7, -1]]
keys = [4, 1, 8]
mat_1 = [[4, -2], [6, 1]]
keys_1 = [22, 45]
mat_2 = [[3, -2], [5, 4]]
keys_2 = [6, 32]
mat_3 = [[2, 3, 5], [3, 7, 4], [1, 2, 2]]
keys_3 = [10, 3, 3]

rv = [[1, 2], [3, 4]]
rv_k = [6, 8]

#print(sl.is_diagonal_mat(mat))
print(mat, keys)
print(sl.slau_by_gauss_jordan(mat, keys))
print(sl.slau_by_rv_mat(mat, keys))
print(mat_1, keys_1 )
print(sl.slau_by_gauss_jordan(mat_1, keys_1))
print(sl.slau_by_rv_mat(mat_1, keys_1))
print(rv, rv_k)
#print(sl.slau(mat_2, keys_2))
#print(sl.slau(mat_3, keys_3))
print(sl.slau_by_gauss_jordan(rv, rv_k))
print(sl.slau_by_rv_mat(rv, rv_k))
print()
print(sl.reverse_mat(rv))

#print(m.mul(sl.slau(mat), rv_k))
