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
                length_of_numbers += 1

    return length_of_numbers

anwser = 0
array_of_winnings = {}
for i, line in enumerate(data_into_list):
    val = i+1
    if (val in array_of_winnings):
        array_of_winnings[val] += 1
    else:
        array_of_winnings[val] = 1

    winning_number = get_winning_number(line)
    
    if (winning_number > 0):
        
        # check if we are past the end

        # 
        end = winning_number + 1
        if end + val > len(data_into_list) :
            
            end = len(data_into_list) - val + 1
        

        # go through number of winnings
        for j in range(1, end): # maybe change this
           
            # not sure
            if val+j in array_of_winnings:
                array_of_winnings[val+j] += array_of_winnings[val]
            else:
                array_of_winnings[val+j] = array_of_winnings[val]

      

for amount in array_of_winnings.values():
    anwser += amount



print(anwser)

