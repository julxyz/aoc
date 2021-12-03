def part1():
    pass

def part2():
    pass


if __name__ == "__main__":
    with open ('input.txt', 'r') as f:
        sequence = [line[:-1] for line in f.readlines()]

    print(f"Solution for part 1: {part1()}")
    print(f"Solution for part 2: {part2()}")