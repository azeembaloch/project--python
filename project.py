## input we need from the user
# total rent
# total food ordered for snacking
# electricity unit spend
#charge per unit
#person living in room/flat

#output
#total amount you've to pay is

rent = int(input("Enter the hostel/flat rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_unit = int(input("Enter the total of electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of persons living in the room/flat = "))

total_bill = electricity_unit * charge_per_unit
output = (food + rent + total_bill) // persons

print("Each person will pay:", output)