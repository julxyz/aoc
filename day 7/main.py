with open ('input.txt', 'r') as f:
    rows = [line[:-2] for line in f.readlines()]

b = {}

class Bag:

    heldBags = {}
    held_by = []

    def __init__(self, contents, color):
        self.color = color
        for bag in contents:
            amount, color = bag[0], bag[2:]
            self.heldBags[color] = amount

    def registerParent(self, parent):
        self.held_by.append(parent.color)

    def registerChilds(self):
        for bag in self.heldBags:
            b[bag].registerParent(self)

for row in rows:
    color = row.split(" bags contain ")[0]
    contents = row.split(" bags contain ")[1].split(", ")
    if contents == ["no other bags"]: contents = [] 
    for i, c in enumerate(contents):
        if c.endswith("bags"):
            contents[i] = c[:-5]
        else:
            contents[i] = c[:-4]
    b[color] = Bag(contents, color)

for bag in b.values():
    bag.registerChilds()

print(b["shiny gold"].held_by)