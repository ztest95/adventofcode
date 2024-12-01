def parse_data(data):
    pass

if __name__ == "__main__":

    a = []
    b = []

    with open("2024/input.txt") as f:
        lines = f.readlines()
        
        for line in lines:
            q, w = line.split("   ")
            a.append(int(q))
            b.append(int(w.strip("\n"))) 

    a.sort()
    b.sort()
    
    sum_of_diff = 0
    for i in range(len(a)):
        sum_of_diff += abs(a[i] - b[i])

    print(sum_of_diff)


    
