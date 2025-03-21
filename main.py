import random

print("Welcome to Dungeon Raider!")
print("\nYou are a lone traveler that has set out in search of riches.")
print("One day, you stumble upon what appears to be the entrance to an abandoned dungeon.")
print("You venture inside and look around. It is dark and damp, but you don't mind.")

#The Combat Trial

print("\nYou push forward down a set of stairs and find yourself in a dimly lit room.")
print("On the other side of the room, guarding the only door, is a skeleton determined to keep you from passing.")

print("\nPrepare to fight.")

weapons = ["Sword" , "Axe" , "Bow" , "Dagger" , "Magic Staff"]

print("\nChoose your weapon:")
for i, weapon in enumerate(weapons, 1):
    print(f"{i}.{weapon}")
print("6.Random Weapon")

while True:
    choice=input("\nEnter the number of your choice:").strip()

    if choice.isdigit():
        choice = int(choice)

        if 1 <= choice <= 5:
            player_weapon = weapons[choice - 1]
            break
        elif choice == 6:
            player_weapon = random.choice(weapons)
            break
        else:
            print("Invalid choice. Select a number between 1 and 6.")
    else:
        print("Invalid input. Please enter a number.")
print(f"\nYou have chosen the {player_weapon}! Get ready for battle...")

if player_weapon in ["Sword" , "Axe" , "Bow" , "Magic Staff"]:
    print("\nYou engage in battle with the skeleton.")
    print(f"After a long and hard battle you attack the skeleton one final time with your {player_weapon} and the skeleton shatters.")
    print("\nCongratulations, you have defeated the skeleton. Proceed deeper.")
else:
    print("\nYou charge at the skeleton with your dagger.")
    print("The dagger is swatted out of your hand and the skeleton knocks you to the ground. You try to get up, but the skeleton is too fast. It charges you and skewers you with it's rusty blade.")
    print("You have been defeated.")
    print("\nGame Over.")
    exit()

#The Door Trial

print("\nYou continue down into the next room.")
print("Before you, there are three doors.")
print("It becomes apparent to you that only one of these doors is the correct one and the other doors lead to death.")
print("Which door do you choose?")

while True:
    door_choice = input("\nWould you like to enter Door 1, Door 2, or Door 3? Enter the number:").strip()

    if door_choice == "1":
        print("\nYou open the door, but as you step inside the floor collapses beneath you.")
        print("You fall into a pit of spikes.")
        print("\nGame Over.")
        exit()
    elif door_choice == "2":
        print("\nYou slowly open the door and find a dimly lit hallway leading to yet another room.")
        print("\nCongratulations! You chose the right door. Proceed deeper.")
        break
    elif door_choice == "3":
        print("\nYou open the door and step inside.")
        print("Everything seems fine, but there doesn't appear to be an exit to this room.")
        print("You walk deeper into the room to look for an opening on the opposite wall.")
        print("The door you entered through slams shut behind you. No matter how hard you try to open it, it won't budge.")
        print("Hours pass... then days. You have no food or water.")
        print("After what seems like aes, you collapse. You no loner have the energy needed to survive. The adventure ends here.")
        print("Game Over.")
        exit()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

#The Prisoner Trial

print("\nYou venture into the next room and notice a frail looking man locked in a cage off to the side.")
print("There is a door on the other side of the room, but it is locked.")
print("You approach the cage and the prisoner looks up at you.")
print("The prisoner says to you 'I was once an adventurer like you. I battled my way through this dungeon and ended up trapped in here. I know where the key to the door is. If you let me out of here, I will tell you.")

while True:
    choice = input("\nDo you choose to (1) let the prisoner out of his cage or (2) try to find the key yourself? Enter 1 or 2:").strip()

    if choice == "1":
        print("\nYou unlock the prisoners cage and free him. He thanks you profusely.")
        print("Suddenly, he pulls out a dagger and takes you to the ground. 'Imbecile! You should have left me to rot!")
        print("He starts stabbing you repeatedly. You have been killed.")
        print("\nGame Over.")
        exit()
    elif choice == "2":
        print("\nYou ignore the prisoners plea for help and search around the room.")
        print("You search for hours. The man keeps begging for your help, but you continue to ignore him.")
        print("Eventually, you find a tile in the wall that can be removed.")
        print("You pull the tile away and find the key to the door.")
        print("The man in the cage starts cackling and turns into a dark spirit.")
        print("He flies out of the cage and into the ceiling. You walk over and unlock the door.")
        print("\nCongratulations, you made the right choice. Proceed deeper.")
        break

#The End

print("\nYou continue down and enter a dead end room. In the center of the room is a massive chest.")
while True: 
    open_chest = input("Open the chest? (Type 'Yes' to open):").strip().lower()

    if open_chest == "yes":
        print("\nYou approach the chest and open it.")
        print("You can't believe your eyes, it is filled with more gold and jewels than you have ever seen in your entire life.")
        print("You are unfathomably rich.")
        print("\nCongratulations, You Win!")
        break
    else:
        print("\nThe chest is waiting for you. Open it to proceed.")