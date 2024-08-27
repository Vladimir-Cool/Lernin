import json
from collections import deque


class_list = json.loads(input())

# class_list = [{"name": "B", "parents": ["A", "C"]},
#               {"name": "C", "parents": ["A"]},
#               {"name": "A", "parents": []},
#               {"name": "D", "parents": ["C", "F"]},
#               {"name": "E", "parents": ["D"]},
#               {"name": "F", "parents": []}]

count_dict = {}
queue = deque()

for val in class_list:

    if not val["name"] in count_dict.keys():
        count_dict[val["name"]] = 1

    key = val["name"]
    queue.append(val["name"])
    set_cls = set()
    while queue:
        cls = queue.popleft()

        for j in class_list:
            if not cls == j["name"]:
                if cls in j["parents"]:
                    set_cls.add(j["name"])
                    queue.append(j["name"])
    count_dict[val["name"]] += len(set_cls)


for el in sorted(count_dict):
    print(f"{el} : {count_dict[el]}")

