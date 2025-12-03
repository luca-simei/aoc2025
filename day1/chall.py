def solve1(input_str: str) -> int:
    curr = 50
    result = 0

    with open("output1.txt", "w") as f:
        for line in input_str.splitlines():
            dir = line[0]
            val = int(line[1:])

            if dir == "R":
                curr = (curr + val) % 100
            else:
                curr = (curr - val) % 100

            # debug
            f.write(f"{line} - {curr}\n")

            if curr == 0:
                result += 1

    return result


def solve2(input_str: str) -> int:
    curr = 50
    result = 0

    with open("output2.txt", "w") as f:
        for line in input_str.splitlines():
            dir = line[0]
            val = int(line[1:])

            if dir == "R":
                result += (curr + val) // 100
                curr = (curr + val) % 100
            else: 
                if curr == 0:
                    result += val // 100
                elif val < curr:
                    pass
                else:
                    result += 1 + (val - curr) // 100

                curr = (curr - val) % 100

            # debug
            f.write(f"{line} - {curr} - {result}\n")

    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        input_data = f.read().strip()
    print(solve1(input_data))
    print(solve2(input_data))