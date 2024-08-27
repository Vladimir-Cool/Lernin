import requests
import re

def sort_list(spisc):
    for i in range(len(spisc) - 1):
        for j in range(len(spisc) - i - 1):
            if spisc[j] > spisc[j+1]:
                spisc[j], spisc[j+1] = spisc[j+1],spisc[j]



# link = input()
link = "http://pastebin.com/raw/7543p0ns"
res = requests.get(link)

test = "<a href=\"ya.ru\"> <a href=\"www.ya.ru\"> <a href=\"../skip_relative_links\"> <a href=\'http://neerc.ifmo.ru:1345\'> <a href=\'https://stepik.org\'> <a href=\"http://stepik.org/courses\"> <a href=\"ftp://mail.ru/distib\" >"


# pattern = r"href=[\"\']([^.]*?)+(*?)[/\"]"
pattern = r"<a.*?href=[\"\']?(\w*?://)?(\w.*?)[\"\':/]"
site_list = re.findall(pattern, res.content.decode("utf-8"))

fin_list = []
for i in site_list:
    fin_list.append(i[1])

eshe_list = list(set(fin_list))
sort_list(eshe_list)
for out in eshe_list:
    print(out)



# test1_list = re.findall(pattern, test)
# test2_list = []
# for i in test1_list:
#     test2_list.append(i[1])
# test3_list = list(set(test2_list))
# sort_list(test3_list)
# print(test3_list)
