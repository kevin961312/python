from urllib.request import urlopen
import time


class WebPage:
    def __init__(self,url):
        self.url = url
        self._content = None

    @property
    def content(self):
        if not self._content:
            print("Retrieving New Page...")
            self._content = urlopen(self.url).read()
        return self._content

webpage = WebPage("http://ccphillips.net/")
now = time.time()
content_one = webpage.content
print(time.time()-now)
now = time.time()
content_two = webpage.content
print(time.time()-now)
print(content_one==content_two)


#calculate of average of integer list
class Average(list):
    @property
    def average(self):
        return sum(self/len(self)

        