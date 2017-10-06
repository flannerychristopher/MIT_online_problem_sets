# how many months will it take to save for the down payment?

annual_salary = int(input("What is your annual salary?  "))
portion_saved = float(input("How much can you afford to save each month? Enter as a decimal   "))
monthly_savings = (annual_salary / 12.0) * portion_saved
print("Monthly savings: " + str(monthly_savings))

# total_cost is the cost of my dream home
total_cost = float(input("What is the cost of your dream home?   "))
portion_down_payment = total_cost / 4.0
print "Your down payment will be: " + str(portion_down_payment)

# end of month your savings increase from return on your investment, plus a percentage of your monthly salary
current_savings = 0
number_of_months = 0
annual_return_rate = 0.04
monthly_return_rate = annual_return_rate / 12.0

while current_savings < portion_down_payment:
  number_of_months += 1
  this_months_return = current_savings * monthly_return_rate
  current_savings += monthly_savings + this_months_return

print("It will take " + str(number_of_months) + " months to save for your dream home")