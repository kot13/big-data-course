import sys
import re
import urlparse
import urllib


autoUsers = []
with open('lab03_users.txt', 'r') as tsv:
    for line in tsv:
        data = line.strip().split('\t')
        if data[1] == "1":
            autoUsers.append(data[0])


def url2domain(url):
    try:
       a = urlparse.urlparse(urllib.unquote(url.strip()))
       if (a.scheme in ['http','https']):
           b = re.search("(?:www\.)?(.*)", a.netloc).group(1)
           if b is not None:
               return str(b).strip()
           else:
               return ''
       else:
           return ''
    except:
       return


for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) < 3:
        continue

    if data[0] == "" or data[0] == "-":
        continue

    if data[2] == "" or data[2] == "-":
        continue

    host = url2domain(data[2])

    if host == "" or host is None:
        continue

    isAutoUser = "0"
    if data[0] in autoUsers:
        isAutoUser = "1"

    sys.stdout.write(host + "\t" + isAutoUser + "\n")
