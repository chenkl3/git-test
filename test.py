count = 0
for i in (1,2,3,4):
    for j in (1,2,3,4):
        for k in (1,2,3,4):
            if i !=j and i !=j and j != k:
                count += 1
print(count)