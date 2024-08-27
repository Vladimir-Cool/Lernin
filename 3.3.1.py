import requests
import re


def search_url(url):
    req = requests.get(url)
    pattern = r'href=[\"\'](https?://.*?)[\"\']'
    return re.findall(pattern, req.text)

url1 = input().replace('stepic.org', 'stepik.org')
url2 = input().replace('stepic.org', 'stepik.org')
# url1 = "https://stepik.org/media/attachments/lesson/24472/sample0.html"
# url2 = "https://stepik.org/media/attachments/lesson/24472/sample2.html"

final_list = []
result = search_url(url1)

for i in result:
    final_list.extend(search_url(i.replace('stepic.org', 'stepik.org')))

for i in range(len(final_list)):
    final_list[i] = final_list[i].replace('stepic.org', 'stepik.org')


if url2 in final_list:
    print("Yes")
else:
    print("No")


