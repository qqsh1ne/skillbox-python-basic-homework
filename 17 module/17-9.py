initial_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
result = [lvl_3 for lvl_1 in initial_list for lvl_2 in lvl_1 for lvl_3 in lvl_2]
print(result)