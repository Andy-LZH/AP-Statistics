import math


def calculate_standard_diviation(number: list):

    sigma = 0
    store = 0

    for i in number:
        store += i

    m = store/len(number)
    for i in number:
        sigma += (i-m)*(i-m)

    return math.sqrt(sigma/len(number))


store_temp = []
for p in range(0, 401):
    store_temp.append(p)


print(calculate_standard_diviation(store_temp))
