def convert_seeds(seeds, conversion_map):
    # conversion map {
    #   source: (detination, range),
    #   98: (50, 2)
    # }
    # seeds: list[int]
    new_seeds = []
    for seed in seeds:
        for source, (destination, range) in conversion_map.items():
            if seed >= source and seed < source + range:
                new_seeds.append(destination + (seed - source))
                break
        else:
            new_seeds.append(seed)

    return new_seeds


if __name__ == "__main__":

    arrWords = []

    with open("day-5/input.txt") as f:

        first_line = f.readline()
        seeds = [int(seed) for seed in first_line.split()[1:]]
        print(seeds)
        conversion_map = {}
        
        for line in f.readlines():
            
            if ':'  in line:
                continue 
            
            # if line is empty
            if line.strip() != "": 

                linelist = [int(item) for item in line.strip().split(" ")]
                # destination, source, range
                # conversion_map[line[1]] = line[2],  line[0] # seed start, and range, soil_start

                conversion_map[linelist[1]] = linelist[0],  linelist[2]

            else:
                
                # convert seeds using the maps
                seeds = convert_seeds(seeds, conversion_map)

                # Create a new map
                conversion_map = {}

        
        seeds = convert_seeds(seeds, conversion_map)
        print(seeds)
        print(min(seeds))

            


 