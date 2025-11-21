# Snake_Water_Gun game similar to stone papper and scissor

import random 


choice = int(input("your choice between 1 to 3 : "))
comp_choice = random.randint(1,3)

print(f"Your choice is : {choice}")
print(f"computer's choice is : {comp_choice}")

if choice == comp_choice :
    print("Game Draw...!!")
elif choice == 1 and comp_choice == 2:
    print("You've Won The Game...")
elif choice == 1 and  comp_choice == 3:
    print("You Lost The Game...")
elif choice == 2 and comp_choice == 3:
    print("You've Won The Game...")
elif choice == 2 and  comp_choice == 1:
    print("You Lost The Game...")
elif choice == 3 and comp_choice == 1:
    print("You've Won The Game...")
elif choice == 3 and  comp_choice == 2:
    print("You Lost The Game...")