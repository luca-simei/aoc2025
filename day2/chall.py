def solve1(input_data):
    result = 0
    ids = input_data.split(",")

    for id in ids:
        first_id, last_id = id.split("-")

        for value in range(int(first_id), int(last_id) + 1):
            if len(str(value)) % 2 != 0:
                pass
            else:
                first_part, last_part = str(value)[:len(str(value)) // 2], str(value)[len(str(value)) // 2:]
                if first_part == last_part:
                    result += value
                    with open("output1.txt", "a") as f:
                        f.write(f"{first_part} {last_part} -> {result}\n")

    return result


def solve2(input_data):
    result = 0
    ids = input_data.split(",")

    for id in ids:
        first_id, last_id = id.split("-")

        for value in range(int(first_id), int(last_id) + 1):
            for i in range(1, len(str(value))):
                if len(str(value)) % i != 0:
                    pass
                else: 
                    parts = [str(value)[j:j + i] for j in range(0, len(str(value)), i)]
                    if all(part == parts[0] for part in parts):
                        result += value
                        with open("output2.txt", "a") as f:
                            f.write(f"{parts} -> {result}\n")
                        break
    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        input_data = f.read().strip()
    print(solve1(input_data))
    print(solve2(input_data))