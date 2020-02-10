def sum_element(list_1):

    high_element = 0

    for x in list_1:

        high_element = max(sum(x), high_element)

    return high_element

list_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

print(sum_element(list_1))
