#conversion of dist. given in feets and inches in meter and centimeter
feets=int(input("enter distance in feets: "))
inches=int(input("enter distance in inches: "))
totalinches=feets*12+inches
totalcm=totalinches*2.54
m=totalcm//100
cm=totalcm%100
print(m,"meter",cm,"centimeter")


'''DIRECT METHOD
m=feets*0.3048
cm=inches*2.54
print(m,"meter",cm,"centimeter")'''