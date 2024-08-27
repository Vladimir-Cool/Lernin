from california_pizza import CaliforniaStylePizzaStore
from ny_pizza import NYStylePizzaStore
from chicago_pizza import ChicagoStylePizzaStore

calif_stor = CaliforniaStylePizzaStore()
ny_stor = NYStylePizzaStore()
chic_stor = ChicagoStylePizzaStore()


ny_hawaii = ny_stor.order_pizza("Гавайская")
chic_chees = chic_stor.order_pizza("Сырная")


print(ny_hawaii)
print(ny_hawaii.veggies)
print(chic_chees)
