import requests
from bs4 import BeautifulSoup

URL = "https://www.airbnb.co.uk/rooms/33090114"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
print(page.text)

from selenium.webdriver import Chrome
from selenium.webdriver.Chrome.options import Options
opts = Options()
opts.set_headless()
assert opts.headless
browser = Chrome(options=opts)
browser.get('https://www.airbnb.co.uk/rooms/33090114')


