import pathlib

def solution1() -> int:

    with open(pathlib.Path(__file__).parent / "input.txt") as f:
        lines = f.readlines()

        time_list = [int(i) for i in lines[0].split(":")[1].strip().split()]
        distance_list = [int(i) for i in lines[1].split(":")[1].strip().split()]

        product = 1

        for i in range(len(time_list)):
            time = time_list[i]
            distance = distance_list[i]

            min_time = distance / time
            min_time = int(min_time) if min_time == int(min_time) else int(min_time) + 1

            for i in range(min_time, time//2):
                if i * (time - i) > distance:
                    min_time = i
                    break

            product *= (time - min_time*2) +1

        return product
    
def solution2() -> int:

    with open(pathlib.Path(__file__).parent / "input.txt") as f:
        lines = f.readlines()

        time = int("".join(lines[0].split(":")[1].strip().split()))
        distance = int("".join(lines[1].split(":")[1].strip().split()))

        product = 1

        # Lowst possible charge time, is distance / time
        min_time = distance / time
        # Ceiling function
        min_time = int(min_time) if min_time == int(min_time) else int(min_time) + 1

        for i in range(min_time, time//2):
            if i * (time - i) > distance:
                min_time = i
                break

        product *= (time - min_time*2) +1

        return product

if __name__ == "__main__":

    print(solution1())
    print(solution2())


            



