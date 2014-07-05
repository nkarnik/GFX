import requests
from pattern import web
import time
import os

indexu = "http://data.gdeltproject.org/events/index.html"
base = "http://data.gdeltproject.org/events/"
suffix = ".export.CSV.zip"

index = requests.get(indexu).text

dom = web.Element(index)
urls =[]

for link in dom.by_tag('a'):
    urls.append(link.content)

final = []
loaded = []

with open('/home/ubuntu/GFX/GDELT/loadedgd.txt', 'r') as f:
    for l in f:
        loaded.append(l.strip('\n'))

print loaded


for u in urls:
    try:
        if(int(u[0])):
            if u not in loaded: 
                final.append(u)
                with open('/home/ubuntu/GFX/GDELT/loadedgd.txt', 'a') as f:
                    f.write(u+'\n')
                with open('/home/ubuntu/GFX/GDELT/temp_l.txt', 'a') as f:
                    f.write(u+'\n')

    except:
        continue


for f in final:
    print base + f
    os.system('cd /home/ubuntu/GFX/GDELT/; wget ' + base + f)
    os.system('cd /home/ubuntu/GFX/GDELT/temp_l/; pwd; wget '+ base + f)
    os.system('pwd')
#    os.system('wget ' + base + f)

#print '---------------------'
#print base+time.strftime("%Y%m%d")+suffix
