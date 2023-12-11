import pathlib

if __name__ == "__main__":

    with open(pathlib.Path(__file__).parent / "input.txt") as f:
        lines = f.readlines()

        points = 0
        for i, l in enumerate(lines):

            card_points = 0
            line = l.split(":")[1]

            winning_num, nums = line.split("|")
            winning_num, nums = winning_num.split(), nums.strip('\n').split()
            
            for num in nums:
                if num in winning_num:
                    card_points += 1

            points += (2**(card_points-1)) if card_points > 0 else 0

        print(points)
                  
