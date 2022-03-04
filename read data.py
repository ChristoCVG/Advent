# importing or reading a list



raw_data = open("input.txt", "r")

result = 0

raw = raw_data.read()
d = raw.split()

data = [int(i) for i  in d]


for i in range(1, len(data)):
    
#    pdb.set_trace()
    x = data [ i ]
    y = data [ i - 1]
    if y < x:
        result += 1

print(result)
