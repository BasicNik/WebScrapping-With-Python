from bs4 import BeautifulSoup
import requests
import csv
url="https://www.brainyquote.com/topics/motivational-quotes"
result=requests.get(url)
body=BeautifulSoup(result.text,'html5lib')
quotes=[]
#print(body)
#print(body.text)
qa=body.find('div', class_="qbcol qbc-spc")
for row in qa.findAll('div', style="display: flex;justify-content: space-between"):
    for auth in qa.findAll('a', title="view author"):
#for row in table.findAll('div',attrs={'title':'view quote'}):
    #print(row.text)
        print(f'''
            Quote:-{row.text}
            Auth:-{auth.text} 
            ''')
print(' ')

