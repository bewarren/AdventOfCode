from functools import cmp_to_key


my_file = open("input_seven.txt", "r")

data = my_file.read()

data_into_list = data.split("\n")

hands = list(map(lambda x: x.split()[0], data_into_list))
bids = list(map(lambda x: x.split()[1], data_into_list))


def map_hand(hand):
    counts = {}
    for val in hand:
        if val in counts:
            counts[val] += 1 
        else:
            counts[val] = 1
    
    values = list(counts.values())
    
    if (5 in values):
        return 7
    
    elif (4 in values):
        return 6
    elif (3 in values and 2 in values):
        return 5
    elif (3 in values):
        return 4
    
    elif (values.count(2) == 2):
        return 3 
    
    elif (values.count(2) == 1):
        return 2
    else:
        return 1

hand_values = list((map(map_hand, hands)))

def take_third(elem):
    return elem[2]

HAND_STRENGTH = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'][::-1]

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




         
         

