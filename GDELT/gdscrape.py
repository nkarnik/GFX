"""
Nikhil Karnik
7/3/2014

"""

import requests
from pattern import web
import time
import os
import sys

#Set url paths to scrape, and suffix for zip files to download

indexu = "http://data.gdeltproject.org/events/index.html"
base = "http://data.gdeltproject.org/events/"
suffix = ".export.CSV.zip"


def gdscrape():
'''
Main function for scraping and downloading historical/daily GDELT data
'''

    index = requests.get(indexu).text
    dom = web.Element(index)
    urls =[]

    for link in dom.by_tag('a'):
        urls.append(link.content)

    final = []
    loaded = []

    
    #Load file with list of already downloaded files
    with open('/home/ubuntu/GFX/GDELT/loadedgd.txt', 'r') as f:
        for l in f:
            loaded.append(l.strip('\n'))


    #Only add file paths that haven't yet been downloaded        
    for u in urls:
        try:
            if(int(u[0])):
                if u not in loaded: 
                    final.append(u)
                    with open('/home/ubuntu/GFX/GDELT/loadedgd.txt', 'a') as f:
                        f.write(u+'\n')

        except:
            continue


    #Use wget to download the files that haven't been downloaded yet
    for f in final:
        print base + f
        os.system('cd /home/ubuntu/GFX/GDELT/; wget ' + base + f)
        os.system('cd /home/ubuntu/GFX/GDELT/temp_l/; pwd; wget '+ base + f)
        
if __name__ == "__main__":
    gdscrape()