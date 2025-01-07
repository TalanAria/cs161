# Import the tools to work with dates and calendars
import calendar
from datetime import datetime



#Set the pet's type and name, and print it out using f string
pet_type = "Cat"
pet_name = "bob"
print(f"I have a {pet_type} and his name is {pet_name}.")






#Ask the user for their name, age, and how much they save each year, then print the info using f strings
name = input("Enter your first name:")
age = int(input("Enter your current age:"))
savings = int(input("Enter your yearly savings:"))
print(f"Hello {name}! You are currently {age} years old. In 10 years, you will be {age+10} years old. If you save ${savings} each year, in 5 years you will have saved ${savings*5}.")
print(f"Your average monthly savings is ${savings/12}")





#Find out how many seconds are in the current month and print it using f strings
secs_in_month = calendar.monthrange(datetime.now().year,datetime.now().month)[1] * 24 * 60 * 60
print(f"Seconds in the current month: {secs_in_month}")


#Ask how many eggs the user has, and calculate full dozens and leftover eggs
total_eggs = int(input("Enter the number of eggs:"))
print(f"This makes {total_eggs//12} dozen eggs with {total_eggs%12} left over")
