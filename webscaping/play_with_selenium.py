import bs4, requests

res = requests.get('https://www.google.com')
res.raise_for_status()

page = bs4.BeautifulSoup(res.text, 'html.parser')
page_links = page.select('a')
print(page_links)
