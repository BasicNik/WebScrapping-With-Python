from turtle import title
from bs4 import BeautifulSoup
import re
import requests

url="https://www.brainyquote.com/quote_of_the_day"

result=requests.get(url)
body=BeautifulSoup(result.text, "lxml")

quotess= body.find('div', class_="grid-item qb clearfix bqQt")
#for quote in quotess:
    #print(quote)
quotebyauthors = quotess.find('div', style="display: flex;justify-content: space-between").text.replace('  ','')
#print(quotebyauthors)
#quote=quotes.find('div', )
#print(quote.string)
author=quotess.find('a', class_="bq-aut qa_133100 oncl_a").text.replace('  ','')
#s
#print(author)
print(f'''
Quote:-{quotebyauthors}
Author :- {author}
''')
print(' ')