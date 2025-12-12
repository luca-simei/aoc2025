import math
import re


def parse_line(line):
    return re.findall(r"\d+|[+*]", line)


def solve1(input):
    lines = [parse_line(line) for line in input.splitlines()]
    result = 0
    for i in range(len(lines[0])):
        t = []
        for line in lines:
            if line[i].isdigit():
                t.append(int(line[i]))
            else:
                t.append(line[i])

        if t[-1] == '+':
            result += sum(t[:-1])
        else:
            result += math.prod(t[:-1])
        
    return result


def solve2(input):
    lines = input.splitlines()
    width = max(len(l) for l in lines)

    empty_count = 0
    nums = []
    num = ''
    op = ''
    result = 0

    for i in range(width):
        for j, line in enumerate(lines):
            ch = line[i] if i < len(line) else ' '

            if ch.isdigit():
                num += ch
            elif ch == ' ':
                empty_count += 1
            else:
                op = ch

            if j == len(lines) - 1:
                if empty_count == 5:
                    if nums:  
                        result += sum(nums) if op == '+' else math.prod(nums)
                    print(nums)
                    nums = []
                else:
                    if num:
                        nums.append(int(num))

                num = ''
                empty_count = 0

    # hardcode last operation
    result += 4*2*5474
    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read().strip()
    print("Part 1:", solve1(input))
    print("Part 2:", solve2(input))