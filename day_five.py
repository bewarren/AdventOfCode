from multiprocessing import Pool

my_file = open("input_five.txt", "r")

data = my_file.read()


data_into_list = data.split("\n\n")
#  [int(x) for x in numbers_split[0].split(" ") if x ]
seeds = data_into_list[0].split(":")[1].split(" ")
seeds = [int(x) for x in seeds if x]

seeds_extended = set()

for i, seed in enumerate(seeds):
    # print("here")
    if i % 2 == 1:
        pass 
    else:
        seeds_extended.update(range(seeds[i], seeds[i]+seeds[i+1]))
# this top bit is wrong -- need to look at each seed range and get mins

maps = data_into_list[1:]

print("done with seeds")

def get_location(seed):
    val = seed
    for m in maps:
        split_map = m.split(":")
        name, vals = split_map[0].split(" ")[0], split_map[1]
        # map_names = name.split("-")
        # from_name, to_name = map_names[0], map_names[2]

        map_vals = [v for v in vals.split("\n") if v]
        
        map_dict = {}
        for mp in map_vals:
            mpNumbers = mp.split(" ")
            destination_start, source_start, range_length = int(mpNumbers[0]), int(mpNumbers[1]), int(mpNumbers[2])

            if source_start <= val <= source_start+range_length:
                index = val - source_start 
                map_dict[source_start + index] = destination_start+index
                break

        if (val in map_dict):
            val = map_dict[val]
        else: 
            pass

    return val

   

# map structure {seed: {soil: {fertilizer}}}
# min_location = -1
# for seed in seeds_extended:
#     val = get_location(seed)
    # if (min_location == -1):
    #     min_location = val 
    
    # if (min_location > val):
    #     min_location = val

if __name__ == '__main__':
    with Pool(10) as p:
        min_locations = p.map(get_location, seeds_extended)
        print(min(min_locations))
    
    