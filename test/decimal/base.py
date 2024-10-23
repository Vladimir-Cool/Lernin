from decimal import Decimal, getcontext

getcontext().prec = 5

print(Decimal('100.01') + Decimal('100.01') + Decimal('100.01'))

print(Decimal(100.01) + Decimal(100.01) + Decimal(100.01))


