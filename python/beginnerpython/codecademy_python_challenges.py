def score_sorter(array, top_score):
  # Write your code here
    array.sort()
    array.reverse()
    newlist = []
    for n in array:
        if n <= top_score:
            newlist.append(n)
    return newlist




score_list = [1, 2, 3, 9999, 13]
top = 10000

print(score_sorter(score_list, top))

# takes in a number and returns all primes from 1 to n
def prime_finder(n):
  
    numberlist = list(range(0, n + 1))
    primelist = []
    
    def is_prime(x):
        if x < 2:
            return False
        else:
            for n in range(2, x - 1):
                if x % n == 0:
                    return False
            else:
                return True

    for x in numberlist:
        if is_prime(x) == True:
            primelist.append(x)

    return primelist

print(prime_finder(11))