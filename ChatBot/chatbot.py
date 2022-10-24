# 1-st stage

print("Hello! My name is DICT_Bot")
print("I was created in 2022")

# 2-nd stage

print("Please, remind me your name")
user_input = input(">")
print("What a great name you have,", user_input, '!')

# 3-rd stage

print("Let me guess your age")
print("Enter remainders of dividing your age by 3, 5 and 7")

remainder3 = input(">")
remainder5 = input(">")
remainder7 = input(">")

age = (int(remainder3) * 70 + int(remainder5) * 21 + int(remainder7) * 15) % 105
print("Your age is", age, ",that's a good time to start programming!")

# 4-th stage

print("Now I will prove to you that I can count to any number you want")
from_num = int(input(">"))
print("Counting numbers from " + str(from_num))

for number in range(from_num + 1):
    print(number, "!")

print("Completed, have a nice day!")

# 5-th stage

print("Let's test your astronomy knowledge.")
print("What color is the sun?")
print("1.Red""\n2.Yellow"
      "\n3.Orange""\n4.White")

answer = 0
while answer != 4:
    answer = int(input("Try to guess the answer:"))
    if answer > 4:
        print("Please, try again!")
    elif answer < 4:
        print("Please, try again!")
    elif answer == 4:
        print("Completed, have a nice day!""\nCongratulations, have a nice day!")
