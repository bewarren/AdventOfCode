
import math


my_file = open("input_eight.txt", "r")

data = my_file.read()

data_into_list = data.split("\n\n")



instructions, mappings = data_into_list[0], data_into_list[1]

letter_maps = mappings.split("\n")



alphabet_dict = {}

for num in letter_maps:
    split_vals = num.split("=")
    letters, order = split_vals[0].split()[0], split_vals[1].split(',')

   

    left, right = order[0][2:].split()[0], order[1][:-1].split()[0]
    alphabet_dict[letters] = {'L': left, 'R': right}
    


def ending_A(letter):
    return letter[-1] == 'A'

def ending_Z(letter):
    return letter[-1] == 'Z'

ending_a = list(filter(ending_A, alphabet_dict.keys()))
position = ending_a





def change_position(letter, instruction):
    return alphabet_dict[letter][instruction]


print(ending_a)
vals = []

for val in ending_a:
    pos = val
    count = 0
    break_out = True

    while break_out:
        for i in instructions:
            pos = change_position(pos, i)
            count += 1
            if (ending_Z(pos)):
                vals.append(count)
                break_out = False 
                break

print(math.lcm(*vals))
