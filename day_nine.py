my_file = open("test_input_nine.txt", "r")

data = my_file.read()

data_into_list = data.split("\n")

def recursive_row(row):
    
    if len(row) == row.count(0):
        return 0

    else:
        diffs = []
        first_val = row[0]
        for val in row[1:]:
            diffs.append(val-first_val)
            first_val = val 
        
        return diffs[-1] + recursive_row(diffs)

anwser = 0
for row in data_into_list:
    val = int(row.split()[-1])+ recursive_row(list(map(int, row.split())))
    
    anwser += val

print(anwser)