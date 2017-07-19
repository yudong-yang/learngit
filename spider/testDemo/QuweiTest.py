
from entityItem import QuweiItem as quwei

for page in range(1,2):
    url = 'http://www.dsuu.cc/quwei-category/joke/page/%d'% page + '/'
    etree = quwei.perseUrl(url)

    lists = quwei.bulidlists(etree)
    print(lists)