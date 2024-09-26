#using temporary variable

a = int(input("Enter the A value: "))
b = int(input("Enter the B value: "))

temp = a
a = b
b = temp
print(f"After Swaping A value is :{a}")
print(f"After Swaping B value is :{b}")

#without using temporary variable

a = int(input("Enter the A value: "))
b = int(input("Enter the B value: "))

b = b+a
a = b-a
b = b-a

print(f"After Swaping A value is :{a}")
print(f"After Swaping B value is :{b}")