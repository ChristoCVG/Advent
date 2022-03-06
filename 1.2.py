sums = []
increases = 0

raw = open("input2.txt", "r").read()
lines = raw.split()

lines = [int(i) for i  in lines]


for i in range(len(lines)-2):
    totals = sum(lines[i:i + 3])
    sums.append(totals)
 
    
for i in range(1, len(sums)):
    x = sums [ i ]
    y = sums [ i - 1]
    if x > y:
        increases += 1

print(increases)
