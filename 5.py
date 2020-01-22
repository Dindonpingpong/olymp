t = [[False for i in range(5)] for j in range(17)]
t[0] = ['A','B','C','D','F']
for i in range(8,17): t[i][0] = True
for i in range(5,14,8): 
    for j in range(4):
        t[i+j][1] = True
for i in range(3,17,4):
    t[i][3] = True
    t[i+1][3] = True
for el in t:
    el[4] = ((el[0] and el[3] or el[3]) and (el[1] != el[0]))      
for el in t: print(el)
