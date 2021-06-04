# TODO: Task 3
#  ist comprehension exercise
#  Use a list comprehension to make a list containing tuples (i, j) where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.

first_list = list(range(1, 11))
second_list = []

i = 0
while i < len(first_list):
    second_list.append(first_list[i]**2)
    i += 1

first_tuple = tuple(first_list)
second_tuple = tuple(second_list)
third_list = [first_tuple, second_tuple]
print(third_list)
