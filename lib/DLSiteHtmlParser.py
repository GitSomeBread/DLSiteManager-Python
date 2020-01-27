from lxml import html
import requests
import urllib3

class DLSiteHtmlParser:
    cookies = {"adultchecked": "1"}

    def __init__(self, document):
        self.__document = document


    @classmethod
    def LoadFromSeries(self, series):
        url = f"DLSite.com/mainax/work/product_id/{series}"
        return DLSiteHtmlParser.LoadFromURL(url)

    @classmethod
    def LoadFromURL(self, url):
        resp = requests.get(url, allow_redirects=False, cookies=self.cookies)
        if resp.status_code == 200:
            document = html.fromstring(resp.content)
            return DLSiteHtmlParser(document)
        else:
            raise urllib3.exceptions.HTTPError(resp.status_code, resp.text)
    
    @property
    def product_name(self):
        return self.__document.xpath("//title")[0].text
    
    @property
    def cycle(self):
        return self.__document.xpath("//title")[0].text

    @property
    def seiyuus(self):
        return [seiyuu.text for seiyuu in self.__document.xpath("//title")]
    