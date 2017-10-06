# annual_salary = int(input("Enter the yearly salary: "))
annual_salary = 150000
monthly_salary = annual_salary/12
semi_annual_raise = .07
annual_return_rate = .04
monthly_return_rate = (annual_return_rate/12)
number_of_months = 36
down_payment = 250000
monthly_savings = 0
low = 0.0
high = 1.0

total_earned = 0
for month in range(1,37):
  if month % 6 == 0:
    monthly_salary += monthly_salary * semi_annual_raise
  this_months_return = total_earned * monthly_return_rate
  total_earned += monthly_salary + this_months_return
total_earned = round(total_earned, 2)
print('---------------------------------')
print('total earned over ' + str(month) + ' months: ' + str(total_earned))

solved = False
while solved == False:

  savings_rate = round(((low+high)/2), 4)
  total_saved = round((total_earned * savings_rate), 2)

  print("low: " + str(low) + "... rate: " + str(savings_rate) + "... high: " + str(high) + '... total saved: ' + str(total_saved))
  
  if total_saved > (down_payment-100) and total_saved < (down_payment+100):
    solved = True
  elif total_saved > down_payment:
    high = savings_rate
  elif total_saved < down_payment:
    low = savings_rate


print("success! optimal savings rate:")
