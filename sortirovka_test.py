


l = [{'name': 'Pacita Abad', 'birthday': '1946'}, {'name': 'Norman Ackroyd', 'birthday': '1938'}, {'name': 'Boris Achour', 'birthday': '1966'}, {'name': 'Vincenzo Abbati', 'birthday': '1803'}, {'name': 'Zainul Abedin', 'birthday': '1914'}, {'name': 'Nicolai Abildgaard', 'birthday': '1743'}, {'name': 'Adam D. Miller', 'birthday': '1982'}, {'name': 'Otto Abt', 'birthday': '1903'}, {'name': 'Achille Laugé', 'birthday': '1861'}, {'name': 'Alvar Aalto', 'birthday': '1898'}, {'name': 'Pablo Accinelli', 'birthday': '1983'}, {'name': 'Jussuf Abbo', 'birthday': '1888'}, {'name': 'Hans Aarsman', 'birthday': '1951'}, {'name': 'Abdullah  M. I. Syed', 'birthday': '1974'}, {'name': 'Adam Adach', 'birthday': '1962'}]

def sort_two(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - 1 - i):
            if list[j]["birthday"] > list[j+1]["birthday"]:
                list[j], list[j + 1] = list[j+1], list[j]

            elif list[j]["birthday"] == list[j+1]["birthday"]:

                if list[j]["name"] > list[j + 1]["name"]:
                    list[j], list[j + 1] = list[j + 1], list[j]

sort_two(l)
print(l)