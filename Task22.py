def create_array(n, mn, mx):
    import random
    array = [random.randint(mn, mx) for _ in range(n)]
    return array


n = int(input('Кол-во элементов первого набора? -> '))
m = int(input('Кол-во элементов второго набора? -> '))
listing_1 = create_array(n, 2, 13)
listing_2 = create_array(m, 2, 13)
print(listing_1)
print(listing_2)

set_1 = set(listing_1)
set_2 = set(listing_2)

result = set_1 & set_2
print('Пересечение множеств - ', sorted(result), '\n')
