# user_age input|int define user input by type integer
user_age = int(input("Enter your age: "))

# months int calculate months by user input age
months = user_age * 12

# days int calculate days by user input age
days = user_age * 365

# running with variable and formatting from user input 
print(f"Your age {user_age} is equal to {months} months and equal to {days} days.")
