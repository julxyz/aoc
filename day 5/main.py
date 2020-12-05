with open ('input.txt', 'r') as f:
    rows = [line for line in f.readlines()]

maxid = 0
seats = []

for row in rows:
    #input to int
    r = int(row[:-4].replace("F", "0").replace("B", "1"),2)
    c = int(row[-4:].replace("L", "0").replace("R", "1"),2)

    #calulate ids
    id = r * 8 + c
    seats.append(id)

    #find biggest id
    if id > maxid: maxid = id

print(f"Biggest ID: {maxid}")

#find missing seats where surrounding seats are occupied
for i in range(0, 905):
    if i not in seats and i-1 in seats and i+1 in seats:
        print(f"My seat: {i}")