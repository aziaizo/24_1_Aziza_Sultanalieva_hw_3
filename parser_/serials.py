from pprint import pprint

import requests
from bs4 import BeautifulSoup


URL="https://www.ts.kg"
HEADERS={
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"
}

def get_html(url):
    req=requests.get(url=url, headers=HEADERS)
    return req

def get_data(html):
    soup=BeautifulSoup(html,"html.parser")
    items=soup.find_all("div", class_="show")
    serials=[]
    for item in items:
        info=item.find("img").get("title").split(", ")
        card={
            "title": item.find("p", class_="show-title").getText(),
            "link": URL+(item.find("a").get("href")),
            "type": info[0],
            "genre": info[-1],
        }
        serials.append(card)
    return serials


def parser():
    html=get_html(URL)
    if html.status_code == 200:
        page=get_data(html.text)
        return page
    else:
        raise Exception("Bad request")







