from pprint import pprint
import re
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv


def compare_and_join(l1, l2):
    if l1[0] == l2[0] and l1[1] == l2[1] and l1[2] == l2[2]:
        print("Дубль:", l1[0:3])
        if l1[3] == "": l1[3] = l2[3]
        if l1[4] == "": l1[4] = l2[4]
        if l1[5] == "": l1[5] = l2[5]
        if l1[6] == "": l1[6] = l2[6]
        return True
    return False


with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)


list_info = []
for contact in contacts_list:
    fio = ' '.join(contact[:2]).strip().split(' ')
    contact[:len(fio)] = fio
    if fio:
        phone = re.compile(r'(8|\+7)\W*(\d{3})\W*(\d{3})\W*(\d{2})\W*(\d{2})(\s\W*(\w+[.])\s*(\d+))?')
        phone_sub = r'+7(\2)\3-\4-\5 \7\8'
        phone_res = re.sub(phone, phone_sub, contact[5])
        list_info.append([fio[0], fio[1], contact[2], contact[3], contact[4], phone_res, contact[6]])


list_info = sorted(list_info, key=lambda d: (d[0], d[1], d[2]))
contacts_list, i = [], 0
while i < len(list_info):
    while i + 1 < len(list_info) and compare_and_join(list_info[i], list_info[i + 1]):
        del list_info[i + 1]
    contacts_list.append(list_info[i])
    i += 1

pprint(contacts_list)



