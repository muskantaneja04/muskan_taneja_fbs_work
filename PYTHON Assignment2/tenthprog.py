#revese three digit num
num=int(input("Enter three digit num: "))
a=num%10
num=num//10
b=num%10
c=num//10
print("reversed num is", a*100+b*10+c)
