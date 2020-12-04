#I started doing this in C and got very frustrated, that's why some vars are named like they are thank you


#read input
with open ('input.txt', 'r') as f:
    rows = [line for line in f.readlines()]

#fuck shit class
class Password:
    def __init__(self, password, letter, min, max):
        self.password = password
        self.letter = letter
        self.min = min
        self.max = max

    def validate(self):
        count = self.password.count(self.letter)
        if count >= self.min and count <= self.max:
            return True
        else:
            return False

    def validate2(self):
        if ((self.password[self.min-1] == self.letter) != (self.password[self.max-1] == self.letter)) and ((self.password[self.min-1] == self.letter) or (self.password[self.max-1] == self.letter)):
            return True
        else:
            return False

#go through input and SEX
valid = 0
valid2 = 0
for entry in entries:
    shit = entry.split(":")
    pw = shit[1][1:]
    poop = shit[0].split(" ")
    doodoo = poop[0].split("-")
    p = Password(pw, poop[1], int(doodoo[0]), int(doodoo[1]))
    if p.validate():
        valid += 1
    if p.validate2():
        valid2 += 1

print(valid)