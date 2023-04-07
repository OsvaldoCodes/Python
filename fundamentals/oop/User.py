class user:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display(self):

        print("=======================================================")
        print("Please verify your information below:")
        print("=======================================================")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Membership: {self.is_rewards_member}")
        print(f"Points: {self.gold_card_points}")
        print("=======================================================")
        return self

    def enroll(self):
        if self.is_rewards_member == True:
            print("=======================================================")
            print("You have already been enrolled.")
            print("=======================================================")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 100

            print("=======================================================")
            print(f"Thank you for enrolling {self.first_name}!")
            print("=======================================================")
        return self

    def balance(self):

        print("=======================================================")
        print(f"Your balance is: {self.gold_card_points} points")
        print("=======================================================")
        return self

    def spend_points(self, amount):
        if self.gold_card_points <= 39:
            print("=======================================================")
            print("You don't have enough points to play")
            print("=======================================================")
        else:
            result = self.gold_card_points - amount
            print("=======================================================")
            print(f"You now have: {result} points")
            print("=======================================================")
        return self    


ozzy = user("Osvaldo", "Rivera", "or1234@gmail.com", 22)
john = user("John", "Smith", "smith123@gmail.com", 30)
julie = user("Julie", "Smith", "juliesmith123@gmail.com", 31)

ozzy.enroll().display().spend_points(50).enroll()
#ozzy.balance()

#john.enroll()
#john.display()
#john.spend_points(80)

julie.enroll().display().spend_points(40).enroll()

