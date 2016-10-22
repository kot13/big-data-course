import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) < 3:
        continue

    if data[0] == "" or data[0] == "-":
        continue

    if data[2] == "" or data[2] == "-":
        continue

    sys.stdout.write(data[2] + "\t1\n")
