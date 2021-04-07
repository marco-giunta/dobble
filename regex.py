from urllib.request import urlopen
import re
url = "https://www.markporthouse.net/spot-it-dobble-symbol-list"
figure = re.findall("[1-5]*[0-9]+\. ([A-Z][a-z]+’* *[a-z]* *[A-Z]*[a-z]* *[a-z]* *[a-z]*)",urlopen(url).read().decode())
print(figure)

with open("figure.txt","w") as fh :
    for i in range(len(figure)) :
        fh.write(figure[i]+"\n")
