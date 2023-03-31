# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#T R U E L O V E
name_combined = name1 + name2
name_combined = name_combined.lower()
true = name_combined.count("t") + name_combined.count("r") + name_combined.count("u") + name_combined.count("e")
love = name_combined.count("l") + name_combined.count("o") + name_combined.count("v") +name_combined.count("e")
true_love = int(str(true) + str(love))
if true_love < 10 or true_love > 90:
    print("Your score is " + str(true_love) + ", you go together like coke and mentos.")
elif 40 < true_love < 50:
    print("Your score is " + str(true_love) + ", you are alright together.")
else:
    print("Your score is " + str(true_love) + ".")
