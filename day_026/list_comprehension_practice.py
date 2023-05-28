a_list = [1, 2, 3]
b_list = [n + 1 for n in a_list[::-1]]
print(b_list)

c_list = [2 * n for n in range(1, 4)]
print(c_list)

d_list = ['Alex', 'Beth', 'Caroline']
e_list = [name.upper() for name in d_list]