# Скорость записи 4096 Кбит\с
write_speed = 4096
record_for_day = (write_speed * 60 * 60 * 24) / (8 * 1024 * 1024 * 1024)
number_of_camers = int(input("Введите количество камер : "))
days = int(input("Введите количество дней : "))
record_all_camers = number_of_camers * record_for_day


# print("В день записываеться ", record_for_day, "Гбайт")
print("Все камеры запишут", record_all_camers, "ТБ в день")
print(record_all_camers * days, f"ТБ за {days} дней")
