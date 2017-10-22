annual_salary = int(input("Enter the yearly salary: "))
monthly_salary = annual_salary/12
semi_annual_raise = .07
annual_return_rate = .04
monthly_return_rate = annual_return_rate / 12
number_of_months = 36
down_payment = 250000

total_earned = 0
for month in range(1,37):
  this_months_return = total_earned * monthly_return_rate
  total_earned += monthly_salary + this_months_return
  if month % 6 == 0:
    monthly_salary += monthly_salary * semi_annual_raise
total_earned = round(total_earned, 2)

solved = False
count = 0
low = 0.0
high = 1.0

if total_earned < down_payment:
  solved = True

while solved == False:
  count += 1
  savings_rate = (low+high) / 2
  total_saved = total_earned * savings_rate

  if total_saved > (down_payment-100) and total_saved < (down_payment+100):
    solved = True
  elif total_saved > down_payment:
    high = savings_rate
  elif total_saved < down_payment:
    low = savings_rate

if solved == True and total_earned < down_payment:
  print("It is not possible to pay the down payment in three years.")
elif solved == True:
  print("success! optimal savings rate: " + str(round(savings_rate, 4)))
  print("steps in bisection search: " + str(count))
  