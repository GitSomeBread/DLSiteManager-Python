from lxml import html
import requests
import urllib3
import Utils

class DLSiteHtmlParser:
    cookies = {"adultchecked": "1"}

    def __init__(self, document):
        self.__document = document


    @classmethod
    def LoadFromSeries(self, series):
        url = Utils.get_home_URL(series)
        return DLSiteHtmlParser.LoadFromURL(url)

    @classmethod
    def LoadFromURL(self, url):
        resp = requests.get(url, allow_redirects=True, cookies=self.cookies)
        if resp.status_code == 200:
            document = html.fromstring(resp.content)
            return DLSiteHtmlParser(document)
        else:
            raise urllib3.exceptions.HTTPError(resp.status_code, resp.text)
    
    @property
    def product_name(self):
        return self.__document.xpath("//h1[@itemprop='name' and @id='work_name']/a[@itemprop='url']")[0].text
    
    @property
    def cycle(self):
        return self.__document.xpath("//span[@itemprop='brand' and @class='maker_name']/a")[0].text

    @property
    def seiyuus(self):
        return [seiyuu.text for seiyuu in self.__document.xpath("//table[@id='work_outline']/tr/th[contains(text(), '声優')]/../td/a")]
    