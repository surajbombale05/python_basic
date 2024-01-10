a = 12
b = 13
print("before swaffing a=",a," b=",b)
c=a
a=b
b=c
print("after swapping a=",a," b=",b)

#without using third variable
a,b = b,a

print("after swapping a=",a," b=",b)
