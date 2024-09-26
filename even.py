n = int(input("Give n value : "))

i = 1

while i<= n:
    if not (i%2 == 0):
        i += 1
        continue
    print(i)
    i += 1