#Simple quiz game

print("Welcome to my Python quiz!")

playing =  input("Do you want to play? ")

if playing != "yes":
    quit()
print("Okay, let's play!")
score = 0

answer = input("In Python, which data type is used to store a sequence of items? List | Array | Function ")
print(answer)
print(answer.lower())
if answer.lower() == "list":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the maximum length of a Python identifier? 32 | 16 | No fixed length ")
if answer.lower() == "no fixed length":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Are tuples in Python variable or immutable? ")
if answer.lower() == "immutable":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What will be the class output of the statement -> \"print(type(5 // 2))\" ? ")
if answer.lower() == "int":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("Great, you got " + str(score) + " questions correct!")
print("You got " + str((score/4)*100) + "%.")