fuel_price = float(input("What is the current fuel price: \nN"))
amount_owned = float(input("How much do you have in your wallet? \nN"))

# Check conditions
if fuel_price <= 600 and amount_owned >= 5000:
    print("Buy fuel now!")
elif fuel_price < 600 and amount_owned < 5000:
    print("Fuel price is good. But you're broke!")
else:
    print("Fuel price is high. Better wait!")
