import sys


prevKey = None
total = 0.0

for line in sys.stdin:
    l = line.split("\t")

    currentKey = l[0]
    currentPayout = float(l[1])

    if currentKey != prevKey and prevKey is not None:
        sys.stdout.write(prevKey + "\t" + str(total) + "\n")
        total = 0.0
        prevKey = currentKey

    total += currentPayout
    prevKey = currentKey

sys.stdout.write(prevKey + "\t" + str(total) + "\n")
