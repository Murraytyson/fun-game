#fav videogame
#knowing someone's fav game can help know the character

Name = input("Please enter your name: ")
print(f"Hello {Name} Welcome to fun quiz")#practicing on customer input

print(f"Knowing someone's fav game plays a great deal to shape one's character, {Name}, fill in the quiz appropriatly.")

name = input("Please enter the name of the game : ")
print("Great game choice")

time = int(input("How much time do you spend playing daily[HOURS]: "))
if time >= 5:
    print("Too much game time is bad for your health")
elif time <= 5:
    print("It is great to balance gametime for your health")
else:
    print("INVALID CHOICE")
achievement = input("Achievements you have obtained in game: ")
print(f"That's great {Name} congratulation on your great achievement")
rest = int(input("How many hours do you sleep daily: "))
if rest == 0 or rest <= 4:
    print("Lack of enough sleep is harmful for your health")
elif rest >= 5 and rest <= 8:
    print("Improve your rest hours for better performance in game")
elif rest >= 9:
    print("Enough rest boosts your gametime effectively")
else:
    print("INVALID CHOICE")
exercise = input("Which exercise do you prefer: ")
print(f"Great choice {Name} ")
exercise_hours = int(input("How many hours do you spend exercising? [H] "))
if exercise_hours >= 2:
    print("Keep up the good work")
elif exercise_hours == 1:
    print("Concistency is key")
else:
    ("INVALID CHOICE")
food = input("Do you prefer healthy food to fast food[Y/N]: ")
if food == "Y":
    print(f"Keep up {Name} , Healthy food hepls boost your immunity")
elif food == "N":
    print(f"eating fast food migth hinder your health {Name}")

print(f"Thanks you {Name} for your collaboration .Take care")