import json

row_dict = {
    "title": "Заголовок1",
    "description": "Описание1",
    "color": 16711680,
    "fields": [
        {"name": "Поле 1", "value": "Значение поля 1", "inline": False},
        {"name": "Поле 2", "value": "Значение поля 2", "inline": False},
    ],
}

example = {
    "title": "Информация по профилю: {{ name }}",
    "description": "Ваш опыт: {{ exp }}%\nКоличество персонажей: {{ count }} из {{ max_count }}\n",
    "color": 0x9932CC,
    "fields": {"name": "{{ name }}", "value": "{{ value }}", "inline": "{{ inline }}"},
}

example_2 = '[{"name": "Bumber", "value": "1 (0%)", "inline": ""},{"name": "lamumber", "value": "1 (0%)", "inline": ""}]'

# print(json.dumps(example, ensure_ascii=False))
#
# json_str = json.dumps(row_dict, ensure_ascii=False)
# print(json_str)
#
#
# json_dict = json.load(json_str)
# print(json_dict)

{"title": "Информация по профилю: {{ name }}", "description": "Ваш опыт: {{ experience}}%\nКоличество персонажей: {{ characters|length }} из {{ characters_count }}\n", "color": 10040012{% if characters %}, "fields": "[{% for char in characters %}{\"name\": \"{{ char.name }}\", \"value\": \"{{ char.level }} ({{ char.experience }}%)\"{% if char.is_inline %}, \"inline\": \"{{ char.is_inline }}\"{% endif %}},{% endfor %}]"{% endif %}}


print(json.loads(example_2))
