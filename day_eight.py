
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
    
break_out = True
at_letter = 'AAA'
count = 0
while break_out:
    for i in instructions:
        at_letter = alphabet_dict[at_letter][i]
        count += 1
        if (at_letter == 'ZZZ'):
            break_out = False 
            break

print(count)