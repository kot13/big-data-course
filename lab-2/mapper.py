import sys
import happybase


connection = happybase.Connection('localhost')
table = connection.table('pavel.murkin')

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) < 3:
        continue

    if data[0] == "" or data[0] == "-":
        continue

    if int(data[0]) % 256 != 194:
        continue

    if data[1] == "" or data[1] == "-":
        continue

    if data[2] == "" or data[2] == "-":
        continue

    table.put(data[0], {'data:url': data[2]}, int(data[1].replace('.', '')))
