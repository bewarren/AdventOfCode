from functools import reduce

my_file = open("input_six.txt", "r")

data = my_file.read()

data_into_list = data.split("\n")
time, distance = int(reduce(lambda x, y: x+y, data_into_list[0].split(":")[1].split())), int(reduce(lambda x, y: x+y, data_into_list[1].split(":")[1].split()))
# print(time, distance)

def check_if_larger(t):
    dist = (time-t)*t
    if (dist>distance):
        return 1 
    else: 
        return 0

win = sum(map(check_if_larger, range(time+1)))

print(win)
