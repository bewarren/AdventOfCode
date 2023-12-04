my_file = open("input_four.txt", "r")

data = my_file.read()

data_into_list = data.split("\n")

def get_winning_number(line):
    card_split = line.split(":")
    card_number, numbers = card_split[0], card_split[1]

    numbers_split = numbers.split("|")
    winning_numbers, my_numbers = [int(x) for x in numbers_split[0].split(" ") if x ], [int(y) for y in numbers_split[1].split(" ") if y]

    length_of_numbers = 0
    for x in my_numbers:
        if x in winning_numbers:
            if length_of_numbers == 0:
                length_of_numbers = 1
            else: 
                length_of_numbers *= 2

    return length_of_numbers

anwser = 0
for line in data_into_list:
    anwser += get_winning_number(line)

print(anwser)