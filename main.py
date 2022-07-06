import random

print("Who are you?")
name = input()
print(f"Hello, {name}!")

print("Tossing a coin...")

hCount = 0
tCount = 0

for i in range(1, 4):
  r = random.randint(0, 1)

  if r == 0:
    print(f"Round {i}: Heads")
    hCount += 1
  else:
    print(f"Round {i}: Tails")
    tCount += 1

print(f"Heads: {hCount}, Tails: {tCount}")