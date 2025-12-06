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
    prev_val = val

    with open("test_input.txt") as f:
        for index, line in enumerate(f):
            spin = False
            print(f"{index} entry, current value is {val}, current input is {line}")
            direction = line[0]
            print(f"This is the direction {direction}")
            amt = int(line[1:])
            print(f"This is the amt {amt}")
            match direction:
                case "L":
                    if amt > val:
                        spin = True
                    val = val - amt
                case "R":
                    if val + amt > 99:
                        spin = True
                    val = val + amt
                case _:
                    print("fuck")
            print(f"This is the val after altering {val}")
            if spin:
                extra_answers = 0
                if prev_val > val: #we became negative

                else: #we went above 99

                extra_answers = abs(val // 100)
                answer = answer + extra_answers
                print(f"We hit 0 this many times while rotating: {extra_answers}")
            prev_val = val
            val = val % 100
            print(f"This is the finalized value {val}")
            match val:
                case 0:
                    answer += 1
                    print("Answer hit")
                case _:
                    pass
    print(answer)

def main():
    part_2()

if __name__ == "__main__":
    main()
