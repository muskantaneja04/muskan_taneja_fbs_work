p=int(input("enter amount: "))
t=int(input("enter time: "))
r=float(input("rate of interest: "))

interest=p*((1+r/100)**t)-p
print("Compound interest will be",interest)
