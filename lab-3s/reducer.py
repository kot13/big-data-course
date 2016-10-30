import sys


prevDomain = None
currentDomainAuto = 0
currentDomainTotal = 0

for line in sys.stdin:
    l = line.split("\t")

    currentDomain = l[0]

    if currentDomain != prevDomain and prevDomain is not None:
        sys.stdout.write(
            prevDomain + "\t" + str(currentDomainTotal) + "\t" + str(currentDomainAuto) + "\n"
        )
        currentDomainAuto = 0
        currentDomainTotal = 0

    currentDomainAuto += int(l[1])
    currentDomainTotal += 1
    prevDomain = currentDomain

sys.stdout.write(
    prevDomain + "\t" + str(currentDomainTotal) + "\t" + str(currentDomainAuto) + "\n"
)
