# TODO: Task 2
#  Input data:
#  stock = {
#     "banana": 6,
#     "apple": 0,
#     "orange": 32,
#     "pear": 15
#  }
#  prices = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
#  }
#  Create a function which takes as input two dicts with structure mentioned above, then computes and returns the
#  total price of stock.

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

counter = 0
for fruit in stock.keys():
    counter = counter + stock[fruit] * prices[fruit]

total_price = counter
print(f'Total price: {total_price}')
