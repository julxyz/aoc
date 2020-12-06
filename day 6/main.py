#read input
with open ('input.txt', 'r') as f:
    rows = [line[:-1] for line in f.readlines()]

def getSets(rows: list, handler: str) -> list:
    i = 0
    res = []
    for row in rows:
        if row == "":
            i += 1
        else:
            res = eval(handler)
    return res

#calculates union for current group and person
def union(i: int, row: str, res: list) -> list:
    if len(res) == i:
        res.append(set(row))
    else:
        res[i] |= set(row)
    return res

#calculates the intersection for the current group and person
def intersect(i: int, row: str, res: list) -> list:
    if len(res) == i:
        res.append(set("abcdefghijklmnopqrstuvwxyz"))
    res[i] &= set(row)
    return res

#calculates the sum of all set lengths
def sum(l: list) -> int:
    s = 0
    for e in l:
        s += len(e)
    return s

#part 1
print("Part 1: "+str(sum(getSets(rows, "union(i, row, res)"))))

#part 2
print("Part 2: "+str(sum(getSets(rows, "intersect(i, row, res)"))))
