import sys


for line in sys.stdin:
    data = line.strip().split(", ")
    sys.stdout.write(data[2] + "\t" + data[4] + "\n")
