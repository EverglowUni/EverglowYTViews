#pip install requests
#pip install bs4

import requests
from bs4 import BeautifulSoup

#BonBonChocolat
title1 = "Bon Bon Chocolat MV"
url = 'https://www.youtube.com/watch?v=HvGql8HwOIM'
soup1 = BeautifulSoup(requests.get(url).text, 'lxml')
print(title1 + " - " + soup1.select_one('meta[itemprop="interactionCount"][content]')['content'])

#Adios
title2 = "Adios MV"
url = 'https://www.youtube.com/watch?v=4gX_p1VkgA4'
soup2 = BeautifulSoup(requests.get(url).text, 'lxml')
print(title2 + " - " + soup2.select_one('meta[itemprop="interactionCount"][content]')['content'])

#Dun Dun
title3 = "Dun Dun MV"
url = 'https://www.youtube.com/watch?v=NoYKBAajoyo'
soup3 = BeautifulSoup(requests.get(url).text, 'lxml')
print(title3 + " - " + soup3.select_one('meta[itemprop="interactionCount"][content]')['content'])


#SelfNote : To add a python excel script inside to send them directly to an excel file