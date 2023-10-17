name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go?").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across. Type 'walk' to walk around or 'swim' to swim across.")

    if answer == "swim":
        print("You swam across and were eaten by an alligator. You lose!")
    elif answer == "walk":
        print("You walked for many miles and ran out of water. You lose!")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    print("You come to a bridge, it looks wobbly, do you want to cross it or back off? (cross/back)")
    if answer == "back":
        print("You backed off but were shit on by a crow. You lose!")
    elif answer == "cross":
        print("You meet an ancient tribe that has never been disturbed before. They see you as hostile, kill you with arrows and eat your flesh after you are dead.")
    else:
        print("Not a valid option. You lose.")
else: 
    print("Not a valid option. You lose.")

print("Thank you for trying", name)