import requests
import lxml.html
# from bs4 import BeautifulSoup

r = requests.get("https://depremzemin.ibb.istanbul/guncelcalismalarimiz/")
doc = lxml.html.fromstring(r.content)
links = doc.xpath("//ul/li/a[contains(@href, '.pdf') and not(contains(@href, 'TSUNAMI')) and not(contains(@href, 'TSUNAMi'))]")

for l in links:
    print("Start download " + l.attrib["title"])
    download = requests.get(l.attrib["href"])
    with open(f"{l.attrib['title']}.pdf", "wb") as file:
        file.write(download.content)
    print("Download completed " + l.attrib["title"])
