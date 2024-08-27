from re import match, findall, search
import socket


def is_ip(ip :str) -> bool:
    pattern = r"\d$|[1]?\d\d$|2[0-4]\d$|25[0-5]$"
    check = 0
    if len(ip.split(".")) > 4:
        return False
    for el in ip.split("."):
        if match(pattern, el) != None:
            check += 1
    if check != 4:
        return False
    else:
        return True



def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)  # Преобразование IP-адреса в 32-битное представление
        return True
    except socket.error:
        return False


pattern = r"^\d|^[1]?\d\d|^2[0-4]\d|^25[0-5]\.\d|[1]?\d\d|2[0-4]\d|25[0-5]\.\d|[1]?\d\d|2[0-4]\d|25[0-5]\.\d$|[1]?\d\d$|2[0-4]\d$|25[0-5]"

pattern = r"^a|b\.a\.a\.a$" # Так не работает =/

ip = "125.12.125.20"

print(is_ip(ip))
print(is_valid_ip(ip))

# result = match(pattern, "a.a.a.a")
# print(result)


