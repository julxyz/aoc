def get_addends(cache: list, sum: int) -> (int, int):
    for a in cache:
        for b in cache:
            if a == b:
                continue
            if (a + b) == sum:
                # print(a, b, sum)
                return a, b
    return 0, sum

def part1(seq: list) -> int:
    cache = []
    for v in seq:
        if len(cache) < 25:
            cache.append(v)
        else:
            a, b = get_addends(cache, v)
            cache.pop(0)
            cache.append(v)
            if a == 0:
                return b

def part2(seq: list, num: int) -> int:
    for i, v in enumerate(seq):
        sum = v
        offset = 0
        while sum < num:
            offset += 1
            sum += seq[i+offset]
        if sum == num:
            interval = seq[i:i+offset]
            return min(interval)+max(interval)

if __name__ == "__main__":
    with open ('input.txt', 'r') as f:
        sequence = [int(line[:-1]) for line in f.readlines()]
    
    num = part1(sequence)
    ew = part2(sequence, num)
    print(f"The invalid number is {num}")
    print(f"The encryption weakness is {ew}")