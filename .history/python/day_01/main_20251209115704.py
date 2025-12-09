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
            print("################################")
            print("LOOP START")
            entered_loop = False
            print(f"Current value is {val}, current input is {line}")
            old_val = val
            print(f"This is the old val {old_val}")
            direction = line[0]
            amt = int(line[1:])
            print(f"This is the direction {direction} and this is the amount {amt}")   
            match direction:
                case "L":
                    val = val - amt
                case "R":
                    val = val + amt
                case _:
                    print("shit on my dickcccckckckckckkk")
            print(f"This is the new value {val} and this is the old value {old_val}")
            if val > 0:
                for i in range(old_val, val):
                    entered_loop = True
                    print(f"i's current value: {i}")
                    if i % 100 == 0 and i != old_val:
                        print(f"HIT!!!! when i is {i}")
                        answer = answer + 1
            else:
                 for i in reversed(range(old_val, val)):
                    entered_loop = True
                    print(f"i's current value: {i}")
                    if i % 100 == 0 and i != old_val:
                        print(f"HIT!!!! when i is {i}")
                        answer = answer + 1

            print(f" did we enter loop for i in range({old_val}, {val})? {entered_loop}")
            formatted_val = val % 100
            if formatted_val == 0:
                print(f"we hit at the end!!!: {formatted_val}")
                answer = answer + 1
            print("LOOP END")
            print("#################################")
    print(answer)

def main():
    part_2()

if __name__ == "__main__":
    main()
