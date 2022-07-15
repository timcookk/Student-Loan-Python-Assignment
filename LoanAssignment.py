#1
loan_per_year=float(input("What is your loan per year?"))
interest_rate=float(input("What is the interest rate?"))
years=int(input("How many years?"))
total_owed=0
counter=0


while counter<years:
    counter+=1
    total_owed=(total_owed+loan_per_year)*(1+interest_rate)
    print(total_owed)
 

print("Total Owed At Graduation")
print("$",total_owed)

#2
monthly_payment=float(input("What is your monthly payment?"))
monthly_interest_rate=interest_rate/12

if monthly_payment>monthly_interest_rate*total_owed:
    print("A monthly payment of $",monthly_payment,"will work!")
    print("The minimum monthly payment for this loan would be",monthly_interest_rate*total_owed,"dollars")
else:
    print("A monthly paymeny of $",monthly_payment, "wont work! You will be paying off your loans forever.")
    print("The minimum monthly payment for this loan would be",monthly_interest_rate*total_owed,"dollars")

#3
month=0
while total_owed>0:
    month+=1
    total_owed=total_owed-monthly_payment
    total_owed=total_owed*(1+monthly_interest_rate)
    
print("It will take",month,"months to pay off your student loans.")
print("It will take", month/12,"years to pay off your student loans")
