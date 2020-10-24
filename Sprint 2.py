# My name is Andrew McKay.
# This code is designed to be an interactive experience that asks the user questions.
# It may turn into a game in the future, or it may become a story?
def bunny_killer(num_arrows):
    if 0 < num_arrows < 3:
        print("Some of the bunnies get away.")
    elif num_arrows == 0:
        print("All of the bunnies survive.")
    elif num_arrows < 0:
        print("I guess you sat down and made some arrows? All the bunnies survive.")
    elif num_arrows == 3:
        print("You killed them all! What a horrible monster. Who will take care of the baby bunnies?!?")
    elif num_arrows > 3:
        print("You got them all, you don't have to keep shooting. How did you even get that many arrows?")



print("Hello, user. My name is Charlotte, and I look forward to working with you.")
num_arrows = input("If you had to pick a number of arrows to shoot with reckless abandon, how many would that be?")
num_arrows = int(num_arrows)
print("Your input is greatly appreciated.")
name = input("What is your name, oh strange shooter of arrows?")

if name.lower() == "scott":
    print("I hope you are having an especially good day, Professor.")
elif name.lower() == "andrew":
    print("Wow, okay then. Narcissist.")      # This brings the greetings to a close.
else:
    print("What a pleasure it is to meet you,", name + ".")

print("It is at this point I should inform you that using this program costs you money.")
time = input("How many hours do you plan to use this program for?")  # Note: if a string is here, things break

species = input("What species of animal would you consider yourself?").lower()  # lower() from Programiz.com
if species == "human":
    discount = 1
else:
    discount = 0

cost = float(time) * 7 - discount - 1  # This nonsense makes it cheaper to use the program for other species.
# Also, this means it costs 7 dollars per hour to use this machine for humans, but others get a dollar off.
print("Lucky you,", str(name) + ". It looks like using this program only costs you $" + str(cost))
print("That's right, only", str(cost) * 20)  # Did this to repeat the value 20 times.
print("Forgive me, I seem to have made a mistake. Regardless, you have now unlocked access to the calculator.")

calculator = input("Please enter which mode you would like to use: add, subtract, multiply, divide, or none").lower()

if calculator == "add":
    add_1 = float(input("Please input the first number you'd like to add."))
    add_2 = float(input("Please input the second number you'd like to add."))
    addition = add_1 + add_2
    print(addition)

elif calculator == "subtract":
    sub_1 = float(input("Please input the first number you'd like to have be subtracted."))
    sub_2 = float(input("Please input the second number you'd like to use to subtract."))
    subtraction = sub_1 - sub_2
    print(subtraction)

elif calculator == "multiply":
    mul_1 = float(input("Please input the first number to be multiplied."))
    mul_2 = float(input("Please input the second number to be multiplied."))
    multiply = mul_1 * mul_2
    print(multiply)

elif calculator == "divide":
    div_1 = float(input("Please input the number to be the dividend."))
    div_2 = float(input("Please input the second number to be the divisor."))
    divide = div_1 / div_2
    print(divide)

else:
    calculator = input("Then instead use modulo, floor division, exponent, or none.")

if calculator == "modulo":
    mod1 = float(input("Please input the number to be modified."))
    mod2 = float(input("Please input the modulus number base."))
    modular = mod1 % mod2
    print(modular)

elif calculator == "floor division":
    flr_div_1 = float(input("Please input the dividend."))
    flr_div_2 = float(input("Please input the divisor."))
    floor_division = flr_div_1 // flr_div_2
    print(floor_division)

elif calculator == "exponent":
    base = float(input("Please input the base."))
    exp = float(input("Please input the power the base is to be raised to."))
    exponent = base ** exp
    print(exponent)

else:
    print("In that case, please consider the number of arrows you shot.")

print("At the beginning of the program, I asked you to fire arrows.")
print("In reality, you were firing at a family of 3 bunnies about to go into retirement.")
bunny_killer(num_arrows)

if species == "bunny" or species == "Bunny":
    print("Wait, you said you were a bunny?.")
    if num_arrows < 0 or num_arrows ==0:
        print("At least you spared members of your own kind.")
    elif num_arrows != 0 and num_arrows > 0:
        print(name + ", you are truly cruel. Those were members of your own species!!!")
else:
    print("At least you aren't a bunny.")

while num_arrows > 0:
    num_arrows = int(input("Time for an intervention. How many arrows would you shoot knowing what you now know?"))

print("Now that I know you are not a bunny killer, let's adopt the bunnies!")

bunnies_adopted = int(input("Please input the number of bunnies you'd like to adopt."))
if bunnies_adopted < 10:
  bunnies_born = ''
  for k in range(1, bunnies_adopted+1, 1):
    k = str(k)
    bunnies_born = bunnies_born + k
    print(bunnies_born, sep='', end='\n')
  print("Whoops, it looks like you now have " + bunnies_born + " bunnies, which is frankly a lot.")
else:
    print("I took the liberty of naming them all Charlotte for you.")

if bunnies_adopted > 0:
    bunnies_adopted = not False

if bunnies_adopted == True:
    print("Thanks for adopting the bunnies!")
else:
    print("I know what you did.")
