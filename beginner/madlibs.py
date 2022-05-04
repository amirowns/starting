
# doesn't work with written number right now, only integers
number = int(input("Number: "))
# line below not needed
if number == str: number = int(number)
adj = input("Adjective: ")
if number>1 or number<1: noun = input("Plural noun: ")
else: noun = input("Noun: ")
# need to make it so >1 is plural, with if statement?
# worked with if:else statement. needed to turn number into int tho
# realized 0 is also plural...
# fixed that with or, now what if someone puts a number as a string?
''' madlib = "I had " + str(number) + " " + adj + " " + noun + "." '''
madlib = f"I had {number} {adj} {noun}."
print (madlib)

# TODO: can come back later and turn written numbers into integers
