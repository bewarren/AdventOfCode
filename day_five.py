my_file = open("test_input_five.txt", "r")

data = my_file.read()


data_into_list = data.split("\n\n")
#  [int(x) for x in numbers_split[0].split(" ") if x ]
seeds = data_into_list[0].split(":")[1].split(" ")
seeds = [int(x) for x in seeds if x]



maps = data_into_list[1:]

map_dict = {}
# map structure {seed: {soil: {fertilizer}}}
locations = []
for seed in seeds:
    val = seed
    for m in maps:
        split_map = m.split(":")
        name, vals = split_map[0].split(" ")[0], split_map[1]
        map_names = name.split("-")
        from_name, to_name = map_names[0], map_names[2]

        map_vals = [v for v in vals.split("\n") if v]
        
        map_dict = {}
        for mp in map_vals:
            mpNumbers = mp.split(" ")
            destination_start, source_start, range_length = int(mpNumbers[0]), int(mpNumbers[1]), int(mpNumbers[2])

            if val in range(source_start, source_start+range_length):
                index = val - source_start 
                map_dict[source_start + index] = destination_start+index
            
           

        if (val in map_dict):
            val = map_dict[val]
        else: 
            pass
    # print(val)
    locations.append(val)

print(min(locations))


    
    