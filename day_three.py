my_file = open("input_three.txt", "r")

data = my_file.read()

data_into_list = data.split("\n")

def get_symbol_locations(lines):

    list_of_symbol_locations = []
    
    # get symbol locations
    for line in lines:
        for i, symbol in enumerate(line.replace(" ", "")):
            if (symbol != "." and (not symbol.isdigit())):
                list_of_symbol_locations.append(i)
    return list_of_symbol_locations


def get_numbers(line):
     numbers = []
     num = {"number": '', "start": 0, "end": 0}
     lineLength = len(line) - 1
     start = False
     for i, val in enumerate(line):
        if (val.isdigit()):
             if (not start):
                 num["start"] = i
                 start = True
             num["number"] += val

             if (i == lineLength):
                start = False
                num['end'] = i-1
                numbers.append(num)
                num = {"number": '', "start": 0, "end": 0}
        else:
         if start:
             start = False
             num['end'] = i-1
             numbers.append(num)
             num = {"number": '', "start": 0, "end": 0}
         else: 
             pass
         
     return numbers
             
             
             
             
         

length_of_list = len(data_into_list)

anwser = 0

for i, line in enumerate(data_into_list):
    numbers = get_numbers(line.replace(" ", ""))

    symbol_locations = []

    if i == 0:
         symbol_locations = get_symbol_locations(data_into_list[0: 2])
    elif i == length_of_list -1:
           
           symbol_locations = get_symbol_locations(data_into_list[i-1: i+1])
    else:
        symbol_locations = get_symbol_locations(data_into_list[i-1: i+2])

    
    for num in numbers:
        for location in symbol_locations:
            if location in range(int(num["start"])-1, int(num["end"])+2):
                
                anwser += int(num["number"])
    
        
print(anwser)

