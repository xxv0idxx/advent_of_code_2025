def part_1():
    answer = 0
    with open("input.txt") as f:
       content = f.read()
       list = content.split(",")
       for i in list:
           id_min = int(i.split("-")[0])
           id_max = int(i.split("-")[1])
           for j in range(id_min,id_max+1):
               str_j = str(j)
               str_length = len(str_j)
               if str_length %2 == 0:
                   midpoint = int(str_length / 2)
                   if str_j[:midpoint] == str_j[midpoint:]:
                        answer = answer + j

    print(answer)

def main():
    part_1()


if __name__ == "__main__":
    main()
