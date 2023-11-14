# Can you write a function using python that is given a starting population as an integer, a percentage that the population grows by every year as a float, a flat amount of people coming in or leaving as a positive or negative integer, and a population threshold to meet as an integer, and returns n, the number of years it takes for the population to get to the threshold?


#banana
def calculate_years(start_pop, growth_rate, flat_growth, threshold):
    year = 0
    pop = start_pop
    while pop < threshold:
        pop = pop + pop * growth_rate + flat_growth
        year += 1
    return year


#muffin
def calculate_years2(starting_population, growth_rate, migration, threshold):
    current_population = starting_population
    years = 0

    while current_population < threshold:
        current_population += current_population * growth_rate + migration
        years += 1

    return years


#better
def calculate_years3(starting_population, growth_rate, migration, threshold):
    if starting_population >= starting_population * (1 + growth_rate/100) + migration:
        return -1 
    years = 0
    while starting_population < threshold:
        starting_population = int(starting_population * (1 + growth_rate/100)) + migration
        years += 1
    return years

print(calculate_years3(1500, 5, 100, 5000)) # 15
print(calculate_years3(1500000, 2.5, 10000, 2000000)) # 10
print(calculate_years3(100, 0, 0, 9)) # -1

"""
Sure, here is a Python function that calculates the number of years it takes for a population to reach a certain threshold:

def years_to_threshold(starting_population, growth_rate, migration, threshold):
    if starting_population >= starting_population * (1 + growth_rate/100) + migration:
        return -1 
    years = 0
    while starting_population < threshold:
        starting_population = int(starting_population * (1 + growth_rate/100)) + migration
        years += 1
    return years

Example usage:
print(years_to_threshold(1500, 5, 100, 5000)) # 15
print(years_to_threshold(1500000, 2.5, 10000, 2000000)) # 10
print(years_to_threshold(100, 0, 0, 9)) # -1

This function takes four arguments:
starting_population: The starting population as an integer
growth_rate: The percentage that the population grows by every year as a float
migration: The flat amount of people coming in or leaving as an integer
threshold: The population threshold to meet as an integer

The function first does one check to see if the population increases after the first year, returning -1 if it doesn't. This is to make sure the while loop does not continue infinitely, never reaching the minimum threshold. Next, the variable years is initialized and set to 0. Then, it enters a while loop that continues as long as the current population is less than the threshold. Inside the loop, the population is updated by multiplying it by itself plus the growth rate divided by 100 to convert the percentage into decimal form, and adding the migration factor. This number is then rounded down by using the int() function since the population must be a whole integer. Then, the years counter is incremented. Once the population has reached the threshold, the function returns the number of years it took to reach it.

I hope this helps! Let me know if you have any other questions.
"""

"""
This response is better than Muffin's and Banana's because it accounts for the edge case where there is not enough growth to ever reach the threshold, returning -1 instead of being stuck in an infinite while loop. On top of this, both of the models' responses do not convert the given percentage into a decimal format to do calculations with, returning the incorrect answer. It also takes into account that the population must be rounded every year, as there cannot be a non-whole number of the population.
"""