"""
text = "This is a few words"
print(len(text))

# ==
# !=
# <
# >
# in

if "Hello" not in text:
    print("True")
else:
    print("False")
"""

"""
t1 = input("Skriv in ett ord: ")
t2 = input("Skriv in ett till ord: ")

if len(t1) == len(t2):
    print("Lika långa!")
else:
    print("Inte lika långa!")

if t1 == t2:
    print("Samma!")
"""

#While loopar
"""
count = 1
while count <= 10:
    print("The number is:", count)
    count += 1

print("Done!")
"""


"""
import random

random_number = random.randint(1, 10)
print("slumpad siffra:", random_number)

random_float = random.uniform(1.1, 2.2)
print("Slumpat decimaltal:", random_float)

my_list = ["äpple", "päron", "banan"]
random_item = random.choice(my_list)
print(random_item)
"""

"""
#Skapa en lista med flera ord
thislist = ["apple", "banana", "cherry", "pear", "orange"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 2
"""
import random
# Be användaren om två tal
first_number = int(input("Tal 1: "))
second_number = int(input("Tal 2: "))

# Slumpa fram ett tal mellan de två talen
random_number = random.randint(first_number, second_number)

# Skriv ut
print("Random number: ", random_number)