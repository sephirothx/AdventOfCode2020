key = 13316116
door = 13651422

for i in range(10**10):
    p = pow(7, i, 20201227)
    if p in (key, door):
        print(pow(door if p==key else key, i, 20201227))
        break
