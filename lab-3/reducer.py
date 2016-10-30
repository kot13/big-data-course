import sys


def isAutouserByVisits(visits):
    for domain in ['cars.ru', 'avto-russia.ru', 'bmwclub.ru']:
        if domain in visits and visits[domain] >= 10:
            return "1"
    return "0"


def isYoungparentuserByVisits(visits):
    for domain in ['samara-papa.ru', 'vodvore.net', 'mama51.ru']:
        if domain in visits and visits[domain] >= 10:
            return "1"
    return "0"


def isPregnantuserByVisits(visits):
    for domain in ['sp.krasmama.ru', 'forum.krasmama.ru', 'forum.omskmama.ru']:
        if domain in visits and visits[domain] >= 10:
            return "1"
    return "0"


def isPoliticsuserByVisits(visits):
    for domain in ['novayagazeta.ru', 'echo.msk.ru', 'inosmi.ru']:
        if domain in visits and visits[domain] >= 10:
            return "1"
    return "0"


def formatOutputLine(prevUser, currentUserVisits):
    return prevUser + "\t" + \
           isAutouserByVisits(currentUserVisits) + "\t" + \
           isYoungparentuserByVisits(currentUserVisits) + "\t" + \
           isPregnantuserByVisits(currentUserVisits) + "\t" + \
           isPoliticsuserByVisits(currentUserVisits) + "\n"


prevUser = None
currentUserVisits = {}

for line in sys.stdin:
    l = line.split("\t")

    currentUser = l[0]
    currentDomain = l[1].strip()

    if currentUser != prevUser and prevUser is not None:
        sys.stdout.write(
            formatOutputLine(prevUser, currentUserVisits)
        )
        currentUserVisits = {}

    if currentDomain in currentUserVisits:
        currentUserVisits[currentDomain] += 1
    else:
        currentUserVisits[currentDomain] = 1

    prevUser = currentUser

sys.stdout.write(
    formatOutputLine(prevUser, currentUserVisits)
)
