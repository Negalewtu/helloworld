
# my_list = []
# for i in range(5):
#     ss = input("Please enter any string or number: ")
#     my_list.append(ss)

# print(my_list)

import random

# [2:16 PM] Nega Lewtu
RESET = "\033[0m"
COLOURS = ["\033[30m", "\033[31m", "\033[32m", "\033[33m", "\033[34m", 
           "\033[35m", "\033[36m", "\033[37m","\033[90m", "\033[91m", "\033[92m", 
           "\033[93m", "\033[94m", "\033[95m", "\033[96m", "\033[97m","\033[49m", 
           "\033[40m", "\033[41m", "\033[42m", "\033[43m", "\033[44m", "\033[45m", 
           "\033[46m", "\033[47m", "\033[100m", "\033[101m", 
           "\033[102m", "\033[103m", "\033[104m", "\033[105m", "\033[106m", "\033[107m"]
for potato in range(30):
    rnd_color = random.choice(COLOURS)
    print(rnd_color, "Hello, students", RESET)



# def get_rendom_choice(choices) :
#     return random.choice(choices)
# print(get_rendom_choice(['1', '3', '4', '5', '5', '5',]))
# ''' how to use  choice in python '''