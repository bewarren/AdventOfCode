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
                print(id, num, data[colour])
                return 0

        if (total >= 12 + 13 + 14):
            return 0 
            
    # print (id)
    return int(id)

anwser = 0

for game in data_into_list:

    anwser += check_game(game)

print(anwser)