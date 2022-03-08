#Tracking movement across 2 dimensions with a third variable, aim.


new = open("aim.txt", "r").read()

data= new.split()


distance = 0
depth = 0
aim = 0

for i in range(len(data)):
    
    if data[i] == 'forward':
        distance += int(data[ i + 1])
        depth += aim * int(data[i + 1])
        continue
    if data[i] == "up":
        aim -= int(data[i + 1])
        continue
    if data[i] == "down":
        aim += int(data[i + 1])
        continue
 
print(depth * distance)