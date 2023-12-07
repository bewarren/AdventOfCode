from functools import cmp_to_key


my_file = open("input_seven.txt", "r")

data = my_file.read()

data_into_list = data.split("\n")

hands = list(map(lambda x: x.split()[0], data_into_list))
bids = list(map(lambda x: x.split()[1], data_into_list))


def map_hand(hand):
    counts = {'J':0}
    for val in hand:
        if val in counts:
            counts[val] += 1 
        else:
            counts[val] = 1
    
    values = list(counts.values())

    
    if (5 in values):
        return 7
    
    elif (4 in values):
        if counts['J'] == 1 or counts['J'] == 4:
            return 7
        else:
            return 6 
    elif (3 in values and 2 in values):
        if counts['J'] == 3 or counts['J'] == 2:
            return 7
        else:
            return 5
    elif (3 in values):
        if counts['J'] == 1 or counts['J'] == 3:
            return 6
        else:
            return 4
    
    elif (values.count(2) == 2):
        if counts['J'] == 2:
            return 6
        elif counts['J'] == 1:
            return 5
        else:
            return 3 
    
    elif (values.count(2) == 1):
        if counts['J'] == 1 or counts['J'] == 2:
            return 4
        else:
            return 2
    else:
        if counts['J'] == 1:
            return 2
        else:
            return 1

hand_values = list((map(map_hand, hands)))

def take_third(elem):
    return elem[2]

HAND_STRENGTH = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'][::-1]

def get_hand_letter_vals(hand_one, hand_two):
    
     if hand_one[2] < hand_two[2]:
         return -1
     elif hand_one[2] > hand_two[2]:
         return 1
     else:
         for i, j in zip(hand_one[0], hand_two[0]):
            if (HAND_STRENGTH.index(i) < HAND_STRENGTH.index(j)):
                return -1
            
            elif (HAND_STRENGTH.index(i) > HAND_STRENGTH.index(j)):
                return 1
            else: 
                pass

     return -1

z = list(map(list, zip(hands, bids, hand_values)))

z = sorted(z, key=cmp_to_key(get_hand_letter_vals))
# z.sort(key=take_third)
# for i in set(hand_values):
#     list = [hv for hv in z if hv[2] == i]
#     print(list)



anwser = 0 

for i, h in enumerate(z):
   
    anwser += int(h[1])*(i+1)

print(anwser)




# sort hands by value and if equal sort by hand 




         
         

