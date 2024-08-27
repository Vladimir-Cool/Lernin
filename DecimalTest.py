from decimal import Decimal, getcontext

number = 45.23

number = Decimal(number).quantize(Decimal("1.000000"))

print(number)
