#read input
with open ('input.txt', 'r') as f:
    rows = [int(line) for line in f.readlines()]

def part1():
    for entry1 in rows:
        for entry2 in rows:
            if entry1 == entry2:
                pass
            elif entry1 + entry2 == 2020:
                print(f"The two numbers are {entry1} and {entry2}. {entry1}*{entry2}={entry1*entry2}")
                break
        else:
            continue
        break

def part2():
    for entry1 in rows:
        for entry2 in rows:
            if entry1 == entry2:
                pass
            else:
                for entry3 in rows:
                    if entry1 == entry3 or entry2 == entry3:
                        pass
                    elif entry1 + entry2 + entry3 == 2020:
                        print(f"The three numbers are {entry1}, {entry2} and {entry3}. {entry1}*{entry2}*{entry3}={entry1*entry2*entry3}")
                        break
                else:
                    continue
                break
        else:
            continue
        break

if __name__ == "__main__":
    part1()
    part2()