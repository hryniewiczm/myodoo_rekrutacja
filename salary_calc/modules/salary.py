import requests
from lxml import html

def check_salary(value):
  url = 'https://zarobki.pracuj.pl/kalkulator-wynagrodzen/' + str(value) + '-brutto'
  try:
    page = requests.get(url)
    tree = html.fromstring(page.content)
    salary_netto = tree.xpath('//*[@id="main"]/div[1]/div/ul/li[1]/a/span[2]//text()')
    x = salary_netto[0]
    y = x.split('\xa0')
    z = y[0] + y[1]
    return z
  except:
    return 'Błąd serwera'

