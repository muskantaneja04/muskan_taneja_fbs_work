#convert days into years, weeks and days.
days=int(input("enter no. of days:  "))
years=days//365
days=days%365                          
weeks=days//7
days=days%7
y="year"
y1="years"
w="week"
w1="weeks"
d="day"
d1="days"
if years==1:
    y1=y
if weeks==1:
    w1=w
if days==1:
    d1=d

# print(years,"years ,",weeks,"weeks ,",days,"days")
print(years, y1,weeks, w1,days, d1)


