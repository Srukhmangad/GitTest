a=0
b=0
for i in range(101):
    if(i%2==0):
        a+=i 
    else:
        b+=i 
print("Even number Sum= ",a)
print("Odd number Sum= ",b)


x=0
y=0 #y=1
for i in range(0,101,2):
    x+=i
   # y=y+(i-1)
for j in range(1,101,2):
    y+=j
print("Even number Sum= ",x)
print("Odd number Sum= ",y)
        