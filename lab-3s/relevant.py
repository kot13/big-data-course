import sys
from decimal import *


getcontext().prec = 20

total = Decimal(3)
auto = Decimal(1)

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) < 3:
        continue

    relevant = (Decimal(data[2])/total)*(Decimal(data[2])/total) / ((Decimal(data[1])/total) * (auto/total))
    r = '{0:f}'.format(relevant)

    sys.stdout.write(data[0] + "\t" + r + "\n")
