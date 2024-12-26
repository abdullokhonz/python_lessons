# a = int(input());
# for i in range(12, 21, 2):
#     print((i * a) * 0.1);










# Input the price of 1 kg of sweets
price_per_kg = float(input("Enter the price of 1 kg of sweets: "))

# Calculate and output the cost of 1.2 to 2 kg of sweets
print("Cost of sweets:")
for kg in range(12, 21, 2):
    cost = kg * 0.1 * price_per_kg
    print(f"{kg * 0.1:.1f} kg: {cost:.2f}")