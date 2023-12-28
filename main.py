#!/usr/bin/python

# Libraries
import numpy as np

# Modifiers
## Make character class
GENDELF_ToHit = 8
GENDELF_Dmg = 4
GENDELF_Spell = 3

# Helper functions
def gendelf_toHit(attack):
    roll = np.random.randint(1, 21)
    print(f"Attack {attack}: {roll} + {GENDELF_ToHit} = {roll + GENDELF_ToHit}")

def nl():
    print("\n")

# Read character
nl()
character = input("Character: ")
if (character == "gendelf"): # if using python >= 3.10 this could be refactored to a match statement
    pass
else:
    print("Invalid charater")
    exit(0)
nl()

# Run program
while 1:
    if (character == "gendelf"):
        inputString = input("Roll: ").split()

        slashing = 0
        frost = 0
        thunder = 0
        thunderMove = 0
        fire = 0
        fireLeap = 0

        if (inputString[0] == "a"): # Attack (to hit)
            for i in range(1, 4):
                if (str(i) in inputString): gendelf_toHit(attack = i)
            nl()

        elif (inputString[0] == "b"): # Booming Blade
            if ("1" in inputString):
                slashing += np.random.randint(1, 7) + GENDELF_Dmg
                frost += np.random.randint(1, 7)
                thunder += np.random.randint(1, 9)
                thunderMove += (np.random.randint(1, 9) + np.random.randint(1, 9))
            elif ("1c" in inputString):
                slashing += np.random.randint(1, 7) + np.random.randint(1, 7) + GENDELF_Dmg
                frost += np.random.randint(1, 7) + np.random.randint(1, 7)
                thunder += np.random.randint(1, 9) + np.random.randint(1, 9)
                thunderMove += np.random.randint(1, 9) + np.random.randint(1, 9) + np.random.randint(1, 9) + np.random.randint(1, 9)
            if ("2" in inputString):
                slashing += np.random.randint(1, 7)
            elif ("2c" in inputString):
                slashing += np.random.randint(1, 7) + np.random.randint(1, 7)
                slashing += 7
            if ("3" in inputString):
                slashing += np.random.randint(1, 7) + GENDELF_Dmg
                frost += np.random.randint(1, 7)
            elif ("3c" in inputString):
                slashing += np.random.randint(1, 7) + np.random.randint(1, 7) + GENDELF_Dmg
                frost += np.random.randint(1, 7) + np.random.randint(1, 7)

            print(f"Slashing: {slashing}")
            print(f"Frost: {frost}")
            print(f"Thunder: {thunder}")
            print(f"Thunder (move): {thunderMove}")
            print(f"Total: {slashing + frost + thunder} (not move)")
            nl()

        elif (inputString[0] == "g"): # Green-Flame Blade
            if ("1" in inputString):
                slashing += np.random.randint(1, 7) + GENDELF_Dmg
                frost += np.random.randint(1, 7)
                fire += np.random.randint(1, 9)
                fireLeap += np.random.randint(1, 9) + 3
            elif ("1c" in inputString):
                slashing += np.random.randint(1, 7) + np.random.randint(1, 7) + GENDELF_Dmg
                frost += np.random.randint(1, 7) + np.random.randint(1, 7)
                fire += np.random.randint(1, 9) + np.random.randint(1, 9)
                fireLeap += np.random.randint(1, 9) + np.random.randint(1, 9) + 3
            if ("2" in inputString):
                slashing += np.random.randint(1, 7)
            elif ("2c" in inputString):
                slashing += np.random.randint(1, 7) + np.random.randint(1, 7)
                slashing += 7
            if ("3" in inputString):
                slashing += np.random.randint(1, 7) + GENDELF_Dmg
                frost += np.random.randint(1, 7)
            elif ("3c" in inputString):
                slashing += np.random.randint(1, 7) + np.random.randint(1, 7) + GENDELF_Dmg
                frost += np.random.randint(1, 7) + np.random.randint(1, 7)

            print(f"Slashing: {slashing}")
            print(f"Frost: {frost}")
            print(f"Fire: {fire}")
            print(f"Fire (leap): {fireLeap}")
            print(f"Total: {slashing + frost + fire} (not leap)")
            nl()

        elif (inputString[0] != "e"):
            print("Invalid input")
            nl()
    
    if (inputString[0] == "e"): # Exit
        nl()
        exit(0)
