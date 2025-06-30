#find area of rectangle and triangle
a=int(input("Enter 1 to find area of rectagle and 2 for triangle: "))
if a==1:
    length=int(input("enter length: "))
    breadth=int(input("enter breadth: "))
    print("area of rectangle: ",length*breadth)
elif a==2:
    base=int(input("enter base: "))
    height=int(input("enter height: "))
    print("area of triangle: ",base*height/2)
else:
    print("wrong input entered")