pet_type = "Cat"
pet_name = "bob"
print(f"I have a {pet_type} and his name is {pet_name}.")

name = input("Enter your first name:")
age = int(input("Enter your current age:"))
savings = int(input("Enter your yearly savings:"))

print(f"Hello {name}! You are currently {age} years old. In 10 years, you will be {age+10} years old. If you save ${savings} each year, in 5 years you will have saved ${savings*5}.")
print(f"Your average monthly savings is ${savings/12}")