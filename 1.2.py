import pdb

list_of_sums = []
new_result = 0

new = open("input2.txt", "r")
raw = new.read()
d = raw.split()

new_data = [int(i) for i  in d]


for i in range(len(new_data)):
    totals = sum(new_data[i:i + 3])
    list_of_sums.append(totals)
 
    
for i in range(1, len(list_of_sums)):
    x = list_of_sums [ i ]
    y = list_of_sums [ i - 1]
    if x > y:
        new_result += 1

print(new_result)
    
    

    
