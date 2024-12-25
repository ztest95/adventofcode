def solve_star_1(input: list[str]) -> int:
    # solution idea:
    # create dict for connections, bidirectional: for each connection, add two key and value
    # for each, key val, 
    #   get every computer pair, and for every pair, check if they have connection
    #       check if that network is already counted
    # if they do, check if atleast one starts with t, if so, add to counted set
    

    res = 0
    
    counted_network = set()
    connections = dict()

    for i in range(len(input)):
        temp = input[i].split("-")
        connections[temp[0]] = connections.get(temp[0], []) + [temp[1]]
        connections[temp[1]] = connections.get(temp[1], []) + [temp[0]]

    for key, val in connections.items():
        for i in range(len(val)):
            for j in range(i + 1, len(val)):
                if val[i] in connections[val[j]]:
                    # there is a three set computer network
                    network = frozenset([key, val[i], val[j]]) # frozensets are hashable
                    if key[0] == 't' or val[i][0] == 't' or val[j][0] == 't':
                        if network not in counted_network:
                            # print(network, counted_network)
                            res += 1
                            counted_network.add(network)

    print(connections)

    return res


def solve_star_2(input: list[str]) -> int:
    # solution idea

    res = 0

    return res

if __name__ == "__main__":

    with open('2024/24-23.txt') as f:
        input = [line.strip('\n') for line in f.readlines()]
    
    print(solve_star_1(input))
    print(solve_star_2(input.copy()))