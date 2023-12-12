import math
import sys

# 👇️ 1000

# 👇️ set recursion limit to 2000
sys.setrecursionlimit(100000)


my_file = open("input_ten.txt", "r")

data = my_file.read()

data_into_list = data.split("\n")

# find S 
s_location = {"row": 0, "column": 0}
for row_index, row in enumerate(data_into_list):
    if 'S' in row:
        column_index = row.index('S')
        s_location['row'] = row_index
        s_location["column"] = column_index
        break


num_rows = len(data_into_list) - 1
num_columns = len(data_into_list[0])



# for i, row in enumerate(data_into_list):
#     for j, val in enumerate(row):


def traverse(letter, direction, location, count): 
    '''
        Recursive traverse
    '''
    if location == s_location:
        return count
    
    else:
    
        if (letter == '|' and direction == "S" and location['row'] != num_rows):
            # adjust letter, direction, and location
            new_location = {'row': location['row']+1, 'column': location['column']}
            return traverse(data_into_list[location['row']+1][location['column']],'S', new_location,count+1)
        
        elif (letter == '|' and direction == "N" and location['row'] != 0):
            new_location = {'row': location['row']-1, 'column': location['column']}
            return traverse(data_into_list[location['row']-1][location['column']],'N', new_location ,count+1)
        
        elif(letter == '-' and direction == 'E' and location['column'] != num_columns ):
            new_location = {'row': location['row'], 'column': location['column']+1}
            return traverse(data_into_list[location['row']][location['column']+1], 'E', new_location ,count+1)
        
        elif(letter == '-' and direction == 'W' and location['column'] != 0 ):
            new_location = {'row': location['row'], 'column': location['column']-1}
            return traverse(data_into_list[location['row']][location['column']-1], 'W', new_location ,count+1)
        
        elif(letter == 'L' and direction == 'S' and location['column'] != num_columns ):
            new_location = {'row': location['row'], 'column': location['column']+1}
            return traverse(data_into_list[location['row']][location['column']+1], 'E', new_location ,count+1)
        
        elif(letter == 'L' and direction == 'W' and location['row'] != 0 ):
            new_location = {'row': location['row']-1, 'column': location['column']}
            return traverse(data_into_list[location['row']-1][location['column']], 'N', new_location ,count+1)
        
        elif(letter == 'J' and direction == 'S' and location['column'] != 0 ):
            new_location = {'row': location['row'], 'column': location['column']-1}
            return traverse(data_into_list[location['row']][location['column']-1], 'W', new_location ,count+1)
        
        elif(letter == 'J' and direction == 'E' and location['row'] != 0 ):
            new_location = {'row': location['row']-1, 'column': location['column']}
            return traverse(data_into_list[location['row']-1][location['column']], 'N', new_location ,count+1)
        
        elif(letter == '7' and direction == 'E' and location['row'] != num_rows ):
            new_location = {'row': location['row']+1, 'column': location['column']}
            return traverse(data_into_list[location['row']+1][location['column']], 'S', new_location ,count+1)
        
        elif(letter == '7' and direction == 'N' and location['column'] != 0 ):
            new_location = {'row': location['row'], 'column': location['column']-1}
            return traverse(data_into_list[location['row']][location['column']-1], 'W', new_location ,count+1)
        
        elif(letter == 'F' and direction == 'N' and location['column'] != num_columns ):
            new_location = {'row': location['row'], 'column': location['column']+1}
            return traverse(data_into_list[location['row']][location['column']+1], 'E', new_location ,count+1)
        
        elif(letter == 'F' and direction == 'W' and location['row'] != num_rows ):
            new_location = {'row': location['row']+1, 'column': location['column']}
            return traverse(data_into_list[location['row']+1][location['column']], 'S', new_location ,count+1)
        
        else:
            return 'no end'
    
traversals = []

if s_location["row"] != 0 and data_into_list[s_location['row']-1][s_location['column']] in ['F', '7', '|']:
    new_location = {'row': s_location['row']-1, 'column': s_location['column']}
    t_1 = traverse(data_into_list[s_location['row']-1][s_location['column']], 'N', new_location, 1)
    traversals.append(t_1)

if s_location['row'] != num_rows and data_into_list[s_location['row']+1][s_location['column']] in ['L', 'J', '|']:
    new_location = {'row': s_location['row']+1, 'column': s_location['column']}
    
    t_2 = traverse(data_into_list[s_location['row']+1][s_location['column']], 'S', new_location, 1)
    traversals.append(t_2)

if s_location['column'] != 0 and data_into_list[s_location['row']][s_location['column']-1] in ['F', 'L', '-']:
    new_location = {'row': s_location['row'], 'column': s_location['column']-1}
    t_3 = traverse(data_into_list[s_location['row']][s_location['column']-1], 'W', new_location, 1)
    traversals.append(t_3)

if s_location['column'] != num_columns and data_into_list[s_location['row']][s_location['column']+1] in ['J', '7', '-']:
    new_location = {'row': s_location['row'], 'column': s_location['column']+1}
    
    t_4 = traverse(data_into_list[s_location['row']][s_location['column']+1], 'E', new_location, 1)
    traversals.append(t_4)
 
print(traversals)
vals = [x for x in traversals if isinstance(x, int)]


max_val = max(vals)
print(math.floor(max_val/2))
     



    




        
        






