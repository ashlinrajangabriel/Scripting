from requests import get
from bs4 import BeautifulSoup
import pandas as pd
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}
url = "https://www.payscale.com/research/IN/Employer=Accenture/Reviews"
response = get(url, headers=headers)
html_soup = BeautifulSoup(response.text, 'html.parser')
Summary = html_soup.find_all('div', attrs = {'class':'review'})
for x in Summary:
    data=pd.DataFrame()
    print(x.find('div',attrs={'class':'review__headline'}).text)
    print(x.find('div',attrs={'class':'review__reviewer'}).text)
    print(x.find('div',attrs={'class':'review__cons'}).text)
    print(x.find('div',attrs={'class':'review__pros'}).text)
