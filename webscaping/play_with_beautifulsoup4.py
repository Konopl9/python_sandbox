import bs4, requests

res = requests.get('https://www.weather.gov/')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
elem = soup.select('#topnews > div.body > p')
print(elem[0].text.strip())