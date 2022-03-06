#Tracking movement across 2 dimensions

new = open("coordinates.txt", "r").read()

data= new.split()


distance = 0
depth = 0

for i in range(len(data)):
    if data[i] == 'forward':
        distance += int(data[ i + 1])
        continue
    if data[i] == "up":
        depth -= int(data[i + 1])
        continue
    if data[i] == "down":
        depth += int(data[i + 1])
        continue
    
result = distance * depth

print(result)

        
    
        
