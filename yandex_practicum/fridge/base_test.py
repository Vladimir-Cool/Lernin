from decimal import Decimal
from datetime import date


from base import add, add_by_note, find, amount, expire

goods = {
    'Пельмени Универсальные': [
        # Первая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('0.5'), 'expiration_date': date(2023, 7, 15)},
        # Вторая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('2'), 'expiration_date': date(2023, 8, 1)},
    ],
    'Вода': [
        {'amount': Decimal('1.5'), 'expiration_date': None}
    ],
}

add(goods, 'Вода', Decimal('10'))
add(goods, 'Яйца', Decimal('10'),  '2023-2-2')
add(goods, 'Шоколад', Decimal('3'), '2024-12-6')
add(goods, 'Творог', Decimal('3'), '2024-10-14')



# print(goods)

add_by_note(goods, 'Яйца 2 2024-12-30')
add_by_note(goods, 'Вода 2')
add_by_note(goods, 'Кока колла лайт 30 2026-1-1')
add_by_note(goods, 'Томатная паста 1 2020-2-6')

# for el in goods:
#     print(el)
#     print(goods[el])
print('===finde===')
print(find(goods, 'шоколад'))
print(find(goods, 'Шоколад'))

print('===amount===')
print(amount(goods, 'Яйца'))
print(amount(goods, 'шоколад'))
print(amount(goods, 'макарон'))

print('===expire===')
print(expire(goods, 4))
