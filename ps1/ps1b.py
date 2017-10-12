annual_salary = int(input("What is your annual salary?  "))
portion_saved = float(input("How much can you afford to save each month? Enter as a decimal   "))

total_cost = float(input("What is the cost of your dream home?   "))
portion_down_payment = total_cost / 4.0

semi_annual_raise = float(input("Enter a semi-annual raise as a decimal:   "))

current_savings = 0
number_of_months = 0
annual_return_rate = 0.04
monthly_return_rate = annual_return_rate / 12.0

while current_savings < portion_down_payment:
  monthly_savings = (annual_salary / 12.0) * portion_saved

  number_of_months += 1
  this_months_return = current_savings * monthly_return_rate
  current_savings += monthly_savings + this_months_return
  if number_of_months % 6 == 0:
    annual_salary += annual_salary * semi_annual_raise
    print(annual_salary)

print("It will take " + str(number_of_months) + " months to save for your dream home")