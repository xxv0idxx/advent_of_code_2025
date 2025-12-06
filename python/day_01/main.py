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
    prev_hit = False

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
            active_val = val
            extra_answers = 0
            #edge case where we had zero last time!!!!!
            if 0 > val:#tracking if we are negative
                active_val = abs(val) #copy the absolute value of the of the current value to play with
                if 99 >= active_val and not prev_hit:
                    extra_answers = 1 #make sure to track the spin past 0 incase it is only 1 spin and the value remains unders 99 as an absolute
            if active_val > 99: #the lock spins past "0" an amt_spin of times rather than just once
                # if prev_val > val: #we became negative
                #     amt_spin = abs(val) - prev_val
                # else: #we went above 99
                #     amt_spin = val - prev_val
                extra_answers = active_val // 100
                if val % 100 == 0 and extra_answers > 0:
                    extra_answers = extra_answers - 1
            print(f"We hit 0 this many times while rotating: {extra_answers}")
            answer = answer + extra_answers
            val = val % 100
            print(f"This is the finalized value {val}")
            match val:
                case 0:
                    answer += 1
                    prev_hit = True
                    print("Answer hit")
                case _:
                    prev_hit = False
                    pass
    print(answer)

def main():
    part_2()

if __name__ == "__main__":
    main()
