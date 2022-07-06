x = input("Type some numbers")
y = x.split()

z = [int(s) for s in y]

def greatest_number(z):
    print(max(z))
    return max(z)

greatest_number(z)