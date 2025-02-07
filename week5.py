import requests
import re
import psutil

def pool_admission(age):
    """
    Returns the pool admission price based on age.

    Parameters:
    age (int): The age of the person.

    Returns:
    str: The admission price as a string or "free" if under 2.
    """
    if age < 2:
        return "free"
    elif age < 11:
        return "3"
    elif age < 60:
        return "6"
    else:
        return "4"


#checking if a number divisible by 5
number = int(input("Enter a number: "))
if number % 5 == 0:
    print("it is divisible by 5")
else:
    print("it is not divisible by 5")



#using if and elif statments to find captial of states
state = input("Enter the name of a state: ")
if state.lower() == "california":
    print("sacramento")
elif state.lower() == "oregon":
    print("salem")
elif state.lower() == "florida":
    print("tallahassee")
elif state.lower() == "new york":
    print("albany")
elif state.lower() == "illinois":
    print("springfield")
elif state.lower() == "ohio":
    print("columbus")
else:
    print("State not in the list.")


#using a dic to find the capial of a state
states = {
	"california": "sacramento",
	"oregon": "salem",
	"florida": "tallahassee",
    "new york": "albany",
    "illinois": "springfield",
    "ohio": "columbus"
}
state = str(input("Enter the name of a state: "))
print(states.get(state, "Not found"))

#using match cases to look for the capital of a state
states = str(input("Enter the name of a state: "))
match states:
    case "california":
        print("sacramento")
    case "oregon":
        print("salem")
    case "florida":
        print("tallahassee")
    case "new york":
        print("albany")
    case "illinois":
        print("springfield")
    case "ohio":
        print("columbus")
    case other:
        print("Not found")


price = pool_admission(int(input("Enter your age: ")))
print(price)

#check the hmtl to see how much times 160 is there
x = requests.get('http://coccbobcat.com')
instances = re.findall('160', x.text)
print(f" 160 was found {len(instances)} times")

#check how many processes are running on your system
num_processes = len(psutil.pids())
print(f"Number of running processes: {num_processes}")