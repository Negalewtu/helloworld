
import statistics

fruits = ["Apple", "Pineapple", "Orange", "Pear"]
print(fruits, type(fruits)) 

# temp_list = [10.25, 5.36, 8.25, 10.2]
# int_list = [12, 5, 889, 15]
# mixed_list = ["Marina", 10, True, 12.56]

# index
print(fruits[0])
print(fruits[1])
fruits[3] = "Lime"
print(fruits)

# length of the list
print("length of the list", len(fruits))
print(fruits[len(fruits) - 1])

# add a new element to the list
fruits.append("Banana")
fruits.append("Lemon")
print(fruits)

# remove an element from the list
fruits.pop()
fruits.pop(0)
print(fruits)

int_list = [541, 237, 882, 423, 112, 779, 300, 885, 789, 724,
435, 638, 452, 662, 998, 723, 536, 679, 465, 812,
172, 729, 957, 117, 224, 867, 544, 698, 453, 645,
879, 898, 420, 829, 789, 715, 951, 563, 337, 687,
666, 899, 525, 394, 868, 171, 123, 858, 474, 977,
344, 181, 814, 970, 177, 903, 184, 316, 733, 343,
756, 357, 261, 545, 248, 646, 540, 853, 849, 369,
497, 282, 540, 824, 730, 779, 647, 579, 595, 430,
337, 801, 896, 261, 983, 276, 725, 272, 599, 636,
309, 244, 331, 354, 654, 177, 844, 429, 482, 647]

print(int_list)

# loop though list
# for num in int_list:
#     print(num)

# max
maximum = -555555;
for num in int_list:
    if maximum < num:
        maximum = num
print("max =", maximum)

maximum = max(int_list)
print("max =", maximum)

minimum = min(int_list)
print("min =", minimum)

average = statistics.mean(int_list)
print("avg =", average)

sum = sum(int_list)
print("sum =", sum)
