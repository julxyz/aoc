import re

with open ('input.txt', 'r') as f:
    rows = [line for line in f.readlines()]

mandatory_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

class Passport:

    def __init__(self, args: list):
        for arg in args:
            sarg = arg.split(":")
            setattr(self, sarg[0], sarg[1])

    def validate_fields(self):
        for f in mandatory_fields:
            if not hasattr(self, f): return False
        return True

    def _validate_byr(self):
        return len(self.byr) == 4 and 1920 <= int(self.byr) <= 2002

    def _validate_iyr(self):
        return  len(self.iyr) == 4 and 2010 <= int(self.iyr) <= 2020

    def _validate_eyr(self):
        return len(self.eyr) == 4 and 2020 <= int(self.eyr) <= 2030

    def _validate_hgt(self):
        return self.hgt[-2:] == "cm" and 150 <= int(self.hgt[:-2]) <= 193 or self.hgt[-2:] == "in" and 59 <= int(self.hgt[:-2]) <= 76

    def _validate_hcl(self):
        return re.compile("^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$").match(self.hcl)

    def _validate_ecl(self):
        return self.ecl in colors
    
    def _validate_pid(self):
        return len(self.pid) == 9

    def validate_field_data(self):
        return self._validate_byr() and self._validate_iyr() and self._validate_eyr() and self._validate_hgt() and self._validate_hcl() and self._validate_ecl() and self._validate_pid()

i, pps = 0, []
for row in rows:
    if row[:-1] == "":
        i += 1
    elif len(pps) < i+1:
        pps.append(row[:-1])
    else:
        pps[i] += (f" {row[:-1]}")

def part1():
    v = 0
    for pp in pps:
        p = Passport(pp.split(" "))
        if p.validate_fields():
            v += 1
    print(v)

def part2():
    v = 0
    for pp in pps:
        p = Passport(pp.split(" "))
        if p.validate_fields():
            if p.validate_field_data():
                v += 1
    print(v)

if __name__ == "__main__":
    part1()
    part2()
