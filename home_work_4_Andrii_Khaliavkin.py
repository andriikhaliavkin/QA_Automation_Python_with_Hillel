# Є list довільних чисел, наприклад [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44].
# Напишіть код, який видалить (не створить новий, а саме видалить!) з нього всі числа, які менше 21 і більше 74.



lst = [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44]

for item in lst:
    if item < 21 or item > 74:
        lst.remove(item)

print(lst)


# Є два довільних числа які відповідають за мінімальну і максимальну ціну. Є Dict з назвами магазинів і цінами:
# { "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324, "x-store": 37.166, "the_partner": 38.988, "store": 37.720, "rozetka": 38.003}.
# Напишіть код, який знайде і виведе на екран назви магазинів, ціни яких попадають в діапазон між мінімальною і максимальною ціною.


stores_with_prices = {"cito": 47.999, "BB_studio": 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324,
                      "x-store": 37.166, "the_partner": 38.988, "store": 37.720, "rozetka": 38.003}
list_of_stores = list(stores_with_prices.keys())
list_of_prices = list(stores_with_prices.values())

while True:
    try:
        min_price = float(input('provide minimum price: '))
        max_price = float(input('provide maximum price: '))
        if min_price < 0 or max_price < 0 or max_price < min_price:
            print('Please enter correct price range (without negative values, max price should be higher then min '
                  'price.)')
            continue
        break
    except ValueError as e:
        print('Please enter prices in numbers: ')

# finding stores with prices in range and saving in a new list:
stores_in_range = []
for price in range(len(list_of_prices)):
    if min_price <= list_of_prices[price] <= max_price:
        stores_in_range.append(list_of_stores[price])

if len(stores_in_range) == 0:
    print('There is no any store with price in range')
elif len(stores_in_range) == 1:
    print(f'There is only 1 store with price in range: {stores_in_range}')
else:
    print(f'The are {len(stores_in_range)} stores with price in range: {stores_in_range}')
