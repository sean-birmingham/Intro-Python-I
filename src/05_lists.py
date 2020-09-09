# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
x.append(4)  # appends an object to a list
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
x.extend(y)  # extends a list by appending elements from the iterable

print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]

# x.pop(4)  <-- Takes index and returns value
# del x[4] <-- Deletes an element at the index passed in
x.remove(8)  # Removes the element passed in

print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]

x.insert(5, 99)  # Inserts an element at a specified position

print(x)

# Print the length of list x

# calculates the total length of a list that is passed in
print('length:', len(x))

# Print all the values in x multiplied by 1000
for num in x:
    print(num * 1000)
