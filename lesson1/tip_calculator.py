#tip 20%
tip_percent = int(input("tip"));
#tax 6.5%
tax_percent = int(input("tax"));
#meal cost
meal_cost = float(input("cost"));
#server name
server = input('name?');

tip = meal_cost * tip_percent / 100
tax = meal_cost * tax_percent / 100
total_bill = meal_cost + tip + tax

print("The tip amount is: $" + str(tip))
print("The total amount for my meal is: $" + str(total_bill))
print("Thanks for your service " + server)
