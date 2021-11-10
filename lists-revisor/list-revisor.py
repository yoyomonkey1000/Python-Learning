# list-revisor was starting to forget the different list functions

numbers = []
print(numbers)

numbers = [2,4,5,6]

print(numbers)

del numbers[1] 

print(numbers)

#del numbers
#print(numbers) #error numbers no longer exists

print(len(numbers))

print(numbers[-1])

#functions methods 

numbers.append(6666)

print(numbers)

numbers.insert(2, 999)

print(numbers)

my_list = []  # Creating an empty list.

for i in range(5):
    my_list.append(i + 1)

print(my_list)

my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)

#variable_1, variable_2 = variable_2, variable_1



my_list = [8, 10, 6, 2, 4]  # list to sort

for i in range(len(my_list) - 1):  # we need (5 - 1) comparisons
    if my_list[i] > my_list[i + 1]:  # compare adjacent elements
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # If we end up here, we have to swap the elements.



my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.

while swapped:
    swapped = False  # no swaps so far
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)


my_list = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)


print(my_list.reverse())


list_1 = [1]
list_2 = list_1
list_1[0] = 2 #change the contents of list one or so you think!!
print(list_2)

# this next program will copy a list 

# Copying the entire list.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

#print(my_list[start:])

print(6 in new_list)

 

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list:
    if i > largest:
        largest = i

print(largest)


my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)


my_list = [10, 1, 8, 3, 5]
length = len(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)


cubed = [num ** 3 for num in range(5)]
print(cubed)  # outputs: [0, 1, 8, 27, 64]
 
 # 2 dimensional arrays


# A four-column/four-row table - a two dimensional array (4x4)

table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]

print(table)
print(table[0][0])  # outputs: ':('
print(table[0][3])  # outputs: ':)'



row = []

for i in range(8):
    row.append(WHITE_PAWN)


row = [WHITE_PAWN for i in range(8)]


# multidimensional lists 

board = []

for i in range(8):
    row = [EMPTY for i in range(8)] # the inner loop in here create a row array with 8 elements the line above does it 8 times 
    board.append(row)


board = [[EMPTY for i in range(8)] for j in range(8)]


temps = [[0.0 for h in range(24)] for d in range(31)] # write these in the interative fasion 

# Three-dimensional arrays

# Python does not limit the depth of list-in-list inclusion. Here you can see an example of a three-dimensional array:

# Imagine a hotel. It's a huge hotel consisting of three buildings, 15 floors each. There are 20 rooms on each floor. For this, you need an array which can collect and process information on the occupied/free rooms.

# First step - the type of the array's elements. In this case, a Boolean value (True/False) would fit.

# Step two - calm analysis of the situation. Summarize the available information: three buildings, 15 floors, 20 rooms.

# Now you can create the array: rooms then floots then buildings


rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

#but when reference it is rooms[1][9][13] = True # which is building then floor then room 13
# rooms[0][4][1] = False  # first building then 5th floor then 2 room 



# Cube - a three-dimensional array (3x3x3)

cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],

        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],

        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]

print(cube)
print(cube[0][0][0])  # outputs: ':('
print(cube[2][2][0])  # outputs: ':)'





