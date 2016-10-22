import sys


prevKey = None
total = 0

for line in sys.stdin:
    l = line.split("\t")

    currentKey = l[0]

    if currentKey != prevKey and prevKey is not None:
        sys.stdout.write(prevKey + "\t" + str(total) + "\n")
        total = 0

    total += 1
    prevKey = currentKey

sys.stdout.write(prevKey + "\t" + str(total) + "\n")