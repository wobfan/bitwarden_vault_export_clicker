import json

l = json.load(open("/data", "r"))

unique_l = []
names = []

for x in l:
    if x[0] in names:
        continue
    unique_l.append(x)
    names.append(x[0])

headers = ["name", "login_username", "login_password", "login_uri"]

with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)

    for row in unique_l:
        writer.writerow(row)
    