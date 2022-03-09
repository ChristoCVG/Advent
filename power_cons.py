raw_data = open("power_cons.txt", "r").read()

ordered_data = raw_data.split()

one = 0
zero = 0
gamma = []
epsilon = []

for i in ordered_data:
    for val in i[0]:
        if val == "0":
            zero += 1
        if val == "1":
            one += 1


print(one)
print(zero)

gamma = [1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1]
epsilon = [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0]

res_gamma = int("".join(str(x) for x in gamma), 2)
res_epsilon = int("".join(str(x) for x in epsilon), 2)

#print(res_gamma * res_epsilon)


