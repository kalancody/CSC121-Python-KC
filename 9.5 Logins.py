class User:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        print(f"The user is {self.age} years old, and is {self.gender}.")
    
    def greet_user(self):
        print(f"Welcome {self.first_name.title()} {self.last_name.title()}.")
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

myself = User('Kalan', 'Cody', 18, 'male')
myself.describe_user()
myself.greet_user()

# I included a while loop here to call increment_login_attempts multiple times.
x = 0
while x < 6:
    myself.increment_login_attempts()
    x += 1

print(f"Login attmepts before reset: {myself.login_attempts}")
myself.reset_login_attempts()
print(f"Login attempts after reset: {myself.login_attempts}")