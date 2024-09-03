my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

# clear[]
print(my_list)
my_list.clear()
print(my_list)  # Output: []

# copy[]
my_list = [1, 2, 3]
print(my_list)
new_list = my_list.copy()
print(new_list)  # Output: [1, 2, 3]

# count()
x = my_list.count(1)
print('1 appears',x, 'time')  # Output: 1

# extend()
print(my_list)
more_list = [4, 5, 6]
my_list.extend(more_list)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]