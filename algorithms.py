def selection_sort(products):

    """sort products in place by product ID using selection sort"""
    n = len(products)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if products[j].get_id() < products[min_index].get_id():
                min_index = j

        temp = products[i]
        products[i] = products[min_index]
        products[min_index] = temp


def insertion_sort(products):
    """sort products in place by product ID using insertion sort"""

    for i in range(1, len(products)):
        current = products[i]

        j = i - 1
        while j >= 0 and products[j].get_id() > current.get_id():
            products[j + 1] = products[j]
            j -= 1
        products[j + 1] = current


def binary_search(products, product_id):
    """return index of product_id or -1"""

    low = 0
    high = len(products) - 1
    while(low <= high):
        mid = (low + high) // 2
        mid_id = products[mid].get_id()
        if mid_id == product_id:
            return mid
        elif mid_id < product_id:
            low = mid + 1
        else:
            high = mid - 1
    return -1
