# inputs a,b,c
a = int(input("Entet A value: "))
b = int(input("Entet b value: "))
c = int(input("Entet c value: "))

root1 = 0
root2 = 0

d = (b**2)-4*a*c
root1 = (-b + (d**(0.5))) / 2*a
root2 = (-b - (d**(0.5))) / 2*a

print(f"Roots:({root1},{root2})")