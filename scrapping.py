import requests
from bs4 import BeautifulSoup
url = "https://www.geeksforgeeks.org/"

r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent,'html.parser')
print(soup.prettify())