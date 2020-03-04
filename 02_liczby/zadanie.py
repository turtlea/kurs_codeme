l_per_100 = 6.4
distance = 120
price_per_l = 5.04

l_per_100 = float(input("Podaj spalanie: "))
distance = int(input("Jak daleko?"))
price_per_l = 5.04
total_price = price_per_l * distance / 100 * l_per_100
print(round(total_price, 2))