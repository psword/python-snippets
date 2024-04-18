# Variable Definitions
weight = 0
price = 0
# Ground Shipping
ground_flat_price = 20.00
ground_premium_price = 125.00

# Redefine weight
weight = 4.8

if weight <= 2:
  price = 1.50 * weight + ground_flat_price
elif 2 < weight <= 6:
  price = 3.00 * weight + ground_flat_price
elif 6 < weight <= 10:
  price = 4.00 * weight + ground_flat_price
elif 10 < weight:
  price = 4.75 * weight + ground_flat_price

print("Standard Ground Shipping", price)
print("Ground Premium Shipping", ground_premium_price)

# Drone Shipping
if weight <= 2:
  price = 4.50 * weight
elif 2 < weight <= 6:
  price = 9.00 * weight
elif 6 < weight <= 10:
  price = 12.00 * weight
elif 10 < weight:
  price = 14.25 * weight

print("Drone Shipping", price)