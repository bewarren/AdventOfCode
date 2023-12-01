my_file = open("input.txt", "r")

data = my_file.read()


data_into_list = data.split("\n")


def get_number(item):
    numbers = []

    item = item.replace('one', 'o1e')
    item = item.replace('two', 't2o')
    item = item.replace('three', 't3e')
    item = item.replace('four', 'f4r')
    item = item.replace('five', 'f5e')
    item = item.replace('six', 's6x')
    item = item.replace('seven', 's7n')
    item = item.replace('eight', 'e8t')
    item = item.replace('nine', 'n9e')

    for v in item:
        if v.isdigit():
            numbers.append(v)
    
    if (len(numbers) == 0):
        return 0
    
    else:
        return int(numbers[0] + numbers[-1])
    

anwser = 0

for v in data_into_list:
    anwser += get_number(v)

print(anwser)

