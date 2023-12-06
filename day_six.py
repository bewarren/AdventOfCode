from functools import reduce
import math

my_file = open("input_six.txt", "r")

data = my_file.read()

data_into_list = data.split("\n")
time, distance = int(reduce(lambda x, y: x+y, data_into_list[0].split(":")[1].split())), int(reduce(lambda x, y: x+y, data_into_list[1].split(":")[1].split()))
print(time, distance)

# distance = (time - t)*t = -t^2 +time*t
# (-1)*t^2 + time*t - distance = 0

t_one = (-time + (time**2 - 4*(-1)*(-distance))**.5)/(2.0*(-1))
t_two = (-time - (time**2 - 4*(-1)*(-distance))**.5)/(2.0*(-1))

# if (t_one < 0):
#     t_one = 0
# else:
#     t_one = t_one

# if (t_two > time):
#     t_two = time 
# else:
#     t_two = t_two

print(int(math.fabs(math.floor(t_one) - math.floor(t_two))))



# def check_if_larger(time, t, distance):
#     dist = (time-t)*t
#     if (dist>distance):
#         return 1 
#     else: 
#         return 0

# win = sum(check_if_larger(time, i, distance) for i in range(time+1))

    

# anwser = reduce(lambda x, y: x*y, winning)
# print(win)
