import sys
import re
import urlparse
import urllib


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

    sys.stdout.write(data[0] + "\t" + url2domain(data[2]) + "\n")
