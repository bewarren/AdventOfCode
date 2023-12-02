my_file = open("input_two.txt", "r")

data = my_file.read()

data_into_list = data.split("\n")

# only 12 red cubes, 13 green cubes, and 14 blue cubes
data = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def check_game(game):

    game_data = game.split(":")
    id = game_data[0].split(" ")[1]

    sets = game_data[1].split(";")

    for set in sets:
        cubes = set.split(",")
        total = 0
        for subset in cubes:
            values = subset.strip().split(" ")
            
            num, colour = values[0], values[1]

            total += int(num)

            if (int(num) > data[colour]):
                return 0

        if (total >= 12 + 13 + 14):
            return 0 
            
    # print (id)
    return int(id)

def min_set(game): 
    game_data = game.split(":")

    sets = game_data[1].split(";")

    min_red = 0
    min_green = 0
    min_blue = 0

    for set in sets:
        cubes = set.split(",")

        for subset in cubes:
            values = subset.strip().split(" ")
            
            num, colour = int(values[0]), values[1]

            if (colour == "red"):
                if (min_red < num):
                    min_red = num 
            
            elif (colour == "blue"):
                if (min_blue < num):
                    min_blue = num 
            
            else:
                if (min_green < num):
                    min_green = num
    return min_red * min_green * min_blue


anwser = 0

for game in data_into_list:

    anwser += min_set(game)

print(anwser)