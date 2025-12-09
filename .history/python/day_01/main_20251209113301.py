def part_1():
    answer = 0
    val = 50
    index = 0
    with open("input.txt") as f:
        for index, line in enumerate(f):
            print(f"{index} entry, current value is {val}, current input is {line}")
            direction = line[0]
            print(f"This is the direction {direction}")
            amt = int(line[1:])
            print(f"This is the amt {amt}")
            match direction:
                case "L":
                    val = val - amt
                case "R":
                    val = val + amt
                case _:
                    print("fuck")
            print(f"This is the val after altering {val}")
            val = val % 100
            print(f"This is the finalized value {val}")
            match val:
                case 0:
                    answer += 1
                    print("Answer hit")
                case _:
                    pass
    print(answer)

def part_2():
    answer = 0
    val = 50

    with open("test_input.txt") as f:
        for line in f:
            old_val = val
            direction = line[0]
            amt = int(line[1:])
            match direction:
                case "L":
                    val =- amt
                case "R":
                    val =+ amt
                case _:
                    print("shit on my dickcccckckckckckkk")
            for i in range(old_val, val):
                if i % 100 == 0 and i != old_val:
                    answer =+ 1
            formatted_val = val % 100
            if formatted_val == 0:
                answer += 1
    print(answer)

def main():
    part_2()

if __name__ == "__main__":
    main()
