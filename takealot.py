from bs4 import BeautifulSoup
import requests


r = requests.get('https://www.takealot.com/deals?sort=BestSelling%20Descending&rows=100&daily_deals_rows=100&start=0&filter=Available:true&filter=Promotions:56681&filter=Type:13')
print(r)
