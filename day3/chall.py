def solve1(input_data):
    result = 0
    lines = input_data.splitlines()
    for line in lines:
        first_value = 0
        first_idx = 0
        for i in range(len(line)-1):
            if first_value < int(line[i]):
                first_value = int(line[i])
                first_idx = i
        second_value = 0
        for i in range(first_idx+1, len(line)):
            if second_value < int(line[i]):
                second_value = int(line[i])
        result += int(str(first_value) + str(second_value))
        with open("output1.txt", "a") as f:
            f.write(f"{first_value} {second_value} -> {result}\n")

    return result


def solve2(input_data):
    result = 0
    lines = input_data.splitlines()
    for line in lines:
        joltage = []
        start_idx = 0
        for j in range(12):
            joltage.append(0)
            for i in range(start_idx, len(line)-11+j):
                if joltage[j] < int(line[i]):
                    joltage[j] = int(line[i])
                    start_idx = i + 1
        result += int(''.join(str(x) for x in joltage))
        with open("output2.txt", "a") as f:
            f.write(f"{joltage} -> {result}\n")
    return result
        

if __name__ == "__main__":
    with open("input.txt") as f:
        input_data = f.read().strip()
        print(solve1(input_data))
        print(solve2(input_data))
