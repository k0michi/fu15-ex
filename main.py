import random

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

if hCount > tCount:
  print("You won")
else:
  print("You lost")

print(f"Heads: {hCount}, Tails: {tCount}")