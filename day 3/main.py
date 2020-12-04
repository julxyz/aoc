with open ('input.txt', 'r') as f:
    rows = [line for line in f.readlines()]

def count_trees(area: list, dx: int, dy: int) -> int:
    x, y, trees = 0, 0, 0
    while y <= len(area) - 1:
        if rows[y][x] == "#":
            trees += 1
        x = (x + dx) % (len(area[0]) - 1)
        y += dy

    return trees

def part1():
    trees = count_trees(rows, 3, 1)
    print(trees)

def part2():
    trees = count_trees(rows, 1, 1)
    trees *= count_trees(rows, 3, 1)
    trees *= count_trees(rows, 5, 1)
    trees *= count_trees(rows, 7, 1)
    trees *= count_trees(rows, 1, 2)
    print(trees)

if __name__ == "__main__":
    part1()
    part2()