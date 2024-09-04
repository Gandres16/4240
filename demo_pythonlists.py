#append()
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

# index()
index = my_list.index(3)
print(index)  # Output: 2

#insert()
my_list.insert(3, 3)
print(my_list)  # Output: [1, 2, 3, 3, 4, 5, 6]

#pop()
my_list.pop(3)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

#remove()
my_list.remove(3)
print(my_list)  # Output: [1, 2, 4, 5, 6]

#reverse()
my_list.reverse()
print(my_list)  # Output: [6, 5, 4, 2, 1]

#sort()
letter_list = ['d', 'a', 'c', 'b']
my_list.sort()
print(my_list)  # Output: [1, 2, 4, 5, 6]
letter_list.sort()
print(letter_list)  # Output: ['a', 'b', 'c', 'd']