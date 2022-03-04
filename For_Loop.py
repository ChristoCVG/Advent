import pdb



result = 0


a = [1, 2, 3, 2, 4, 5, 6, 3, 6, 2, 6, 7, 8, 9, 7]




for i in range(1, len(a)):
    
#    pdb.set_trace()
    x = a [ i ]
    y = a [ i - 1]
    if y < x:
        result += 1
        
        
print(result)

