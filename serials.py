import requests
from bs4 import BeautifulSoup



class ParserSerials:
    __URL="https://www.ts.kg"
    __HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"
    }


    @classmethod
    def __get_html(cls, url=None):
        if url is not None:
            req = requests.get(url=url, headers=cls.__HEADERS)
        else:
            req = requests.get(url=cls.__URL, headers=cls.__HEADERS)
        return req


    @staticmethod
    def __get_data(html):
            URL= "https://www.ts.kg"
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
F
    @classmethod
    def parser(cls):
        html=cls.__get_html(cls.__URL)
        if html.status_code == 200:
            page=cls.__get_data(html.text)
            return page
        else:
            raise Exception("Bad request")







