#while loop
n = int(input("Give n value : "))
i = 1
sum = 0
while i<=n:
    sum = sum+i
    i += 1
print(sum)

#for loop
n = int(input("Give n value : "))
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)
