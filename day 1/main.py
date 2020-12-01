#read input
entries = []
with open("input.txt") as input:
    entries = input.readlines()
    for i, entry in enumerate(entries):
        entries[i] = int(entry)

#part 1
for entry1 in entries:
    for entry2 in entries:
        if entry1 == entry2:
            pass
        elif entry1 + entry2 == 2020:
            print(f"The two numbers are {entry1} and {entry2}. {entry1}*{entry2}={entry1*entry2}")
            break
    else:
        continue
    break

#part 2
for entry1 in entries:
    for entry2 in entries:
        if entry1 == entry2:
            pass
        else:
            for entry3 in entries:
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