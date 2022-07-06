def hotel_cost(nights):
  #cost is $140 a night
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  if city == "Tampa":
    return 220
  if city == "Pittsburgh":
    return 222
  if city == "Los Angeles":
    return 475

def rental_car_cost(days):
  price = 40 * days
  if days >= 7:
    price = price - 50
  elif days >= 3:
    price = price - 20
  return price

def trip_cost(city, days, spending_money):
  return hotel_cost(days - 1) + plane_ride_cost(city) + rental_car_cost(days) + spending_money
# TODO: add a drop down menu for city?
city = "Los Angeles"
days = int(input("Days Staying: "))
spending_money = int(input("Spending Money: "))

print("Hotel Cost: $" + str(hotel_cost(days - 1)))
print("Plane Cost: $" + str(plane_ride_cost(city)))
print("Car Cost:   $" + str(rental_car_cost(days)))
print("Spending:   $" + str(spending_money))
print("Total Cost: $" + str(trip_cost(city, days, spending_money)))
