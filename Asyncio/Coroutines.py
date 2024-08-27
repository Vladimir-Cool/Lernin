from inspect import getgeneratorstate


# Корутин работает уголком. yield отдает значение x и принимает значение через .send()
def subgen():
    x = "Ready to accept message"
    message = yield x
    print("subgen received:", message)


g = subgen()
print(getgeneratorstate(g))  # Генератор в сомтояние GEN_CREATED
g.send(None)  # Активация генератора
print(getgeneratorstate(g))  # Генератор в сомтояние GEN_SUSPENDED

print(g.send("okffffdfdf"))
