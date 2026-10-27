from product import Product


def recursive_total_price(products):
    if len(products) == 0:
        return 0.0
    return products[0].get_price() + recursive_total_price(products[1:])


def fewest_coins(coins, amount, memo=None):
    if memo is None:
        memo = {}
    
    if amount in memo:
        return memo[amount]
    if amount == 0:
        return 0
    if amount < 0:
        return -1

    min_coins = float("inf")
    for coin in coins:
        res = fewest_coins(coins, amount - coin, memo)
        if res != -1:
            if 1 + res < min_coins:
                min_coins = 1 + res

    if min_coins == float("inf"):
        memo[amount] = -1
    else:
        memo[amount] = int(min_coins)
        
    return memo[amount]


def bubble_sort(products):
    n = len(products)
    for i in range(n):
        for j in range(0, n - i - 1):
            if products[j].get_id() > products[j + 1].get_id():
                temp = products[j]
                products[j] = products[j + 1]
                products[j + 1] = temp


def selection_sort(products):
    n = len(products)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if products[j].get_id() < products[min_idx].get_id():
                min_idx = j
        temp = products[i]
        products[i] = products[min_idx]
        products[min_idx] = temp


def insertion_sort(products):
    for i in range(1, len(products)):
        key_product = products[i]
        j = i - 1
        while j >= 0 and products[j].get_id() > key_product.get_id():
            products[j + 1] = products[j]
            j = j - 1
        products[j + 1] = key_product


def binary_search(products, product_id):
    low = 0
    high = len(products) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_id = products[mid].get_id()

        if mid_id == product_id:
            return mid
        elif mid_id < product_id:
            low = mid + 1
        else:
            high = mid - 1

    return -1
