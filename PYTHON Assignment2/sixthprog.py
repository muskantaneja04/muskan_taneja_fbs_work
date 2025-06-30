#calculate total salary based on da(10% of basic salary) ta(12) hra(15) 
basicSalary=int(input("Enter basic Salary: "))
da=(basicSalary*10)/100
ta=(basicSalary*12)/100
hra=(basicSalary*15)/100
print("Total Salary is",basicSalary+da+ta+hra)