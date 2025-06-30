#calculate minimum no. of note required  for representing an amount
amount=int(input("Enter amount:"))
n500=amount//500
amount=amount%500
n200=amount//200
amount=amount%200
n100=amount//100
amount=amount%100
n50=amount//50
amount=amount%50
n20=amount//20                      
amount=amount%20                                #amount%=20
n10=amount//10
print("note of 500: ",n500)
print("note of 200: ",n200)
print("note of 100: ",n100)
print("note of 50: ",n50)
print("note of 20: ",n20)
print("note of 10: ",n10)