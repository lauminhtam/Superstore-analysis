# print("hello world")
# print('hello'[0])
# print(123 + 567)

# a = "abc"
# print(type(a))
# age = 12
# print("I am" + " " + str(age))

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("Hơ much tip would you like to give? 10, 20, 30? "))
people = int(input("How many people are there? "))
tip_percent = tip / 100
total_tip = bill * tip_percent
total_bill = bill + total_tip
bill_person = total_bill / people
final_amount = round(bill_person, 2)
final_amount = "{:.2f}".format(bill_person)
print(f"Each person should pay: ${final_amount}")