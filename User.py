class User:
    def __init__(self, first_name, last_name, email, age, is_rewards_member = False, gold_card_points = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age 
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)

    def enroll(self):
        if self.is_rewards_member == True:
            print("User is already a member")
            return False
        self.is_rewards_member = True
        self.gold_card_points = 200

    def spend_point(self, amount):
        if self.gold_card_points < amount:
            print("You don't have enough points")
            return False
        self.gold_card_points = self.gold_card_points - amount

user_patrick = User("Patrick", "Purington", "papurington@gmail.com", 30)
user_patrick.enroll()
user_patrick.spend_point(50)
# print(user_patrick.display_info())
# print(user_patrick.enroll())
user_debby = User("Debby", "Purington", "dpurington@gmail.com", 52)
user_debby.enroll()
print(user_debby.spend_point(2100))
# print(user_debby.display_info())
# print(user_patrick.display_info())
# print(user_patrick.enroll())
user_erek = User("Erek", "Purington", "epurington@gmail.com", 55)
user_erek.enroll()
user_erek.spend_point(40)
print(user_erek.display_info())
