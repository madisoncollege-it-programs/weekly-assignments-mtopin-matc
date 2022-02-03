#!/usr/bin/python3
import sys
varRed = "Red"
varGreen = "Green"
varBlue = "Blue"
varName = "Timmy"
varLoot = 10.4516295
print("1. Question: Hello Timmy")
print(f"Hello {varName: <0s}")

print("2. Question: Red-Green-Blue")
print(f"{varRed: <0s}-{varGreen: <0s}-{varBlue: <0s}")

print("3. Question: Is this green or blue?")
print(f"Is this {varGreen.lower(): <0s} or {varBlue.lower(): <0s}?")

print("4. Question: My name is TIMMY")
print(f"My name is {varName.upper(): <0s}")

print("5. Question: [++Red++]")
print(f"[{varRed:+^7s}]")

print("6. Question: [green==]")
print(f"[{varGreen.lower():=<7s}]")

print("7. Question: [*****blue]")
print(f"[{varBlue.lower():*>9s}]")

print("8. Question: BlueBlueBlueBlueBlueBlueblueBlueBlueBlue")
print(f"{varBlue*10: <0s}")

print("9. Question: 10.4516295")
print(f"{varLoot:.7f}")

print("10. Question: 10.5")
print(f"{varLoot:.1f}")

print("11. Question: I have $10.45")
print(f"I have ${varLoot:.2f}")

print("12. Question: [$$$Red$$$$] [$$Green$$$] [$$$Blue$$$]")
print(f"[{varRed:$^10s}] [{varGreen:$^10s}] [{varBlue:$^10s}]")

print("13. Question: [   deR    ] [  Green   ] [   eulB   ]")
print(f"[{varRed[::-1]: ^10s}] [{varGreen: ^10s}] [{varBlue[::-1]: ^10s}]")

print("14. Question: First Color:[Red] Second Color:[Green] Third Color:[Blue]")
print(f"First Color:[{varRed: <0s}] Second Color:[{varGreen: <0s}] Third Color:[{varBlue: <0s}]")
