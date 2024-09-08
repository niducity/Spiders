import requests
import re


urls = [f'https://www.worldofdante.org/comedy/dante/paradise.xml/3.{i}' for i in range(1,34)]

headers = {
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
                }

def get(url, headers):
    resp = requests.get(url, headers=headers)
    text = resp.text
    resp.close()
    return text

def clean(text):
    obj = re.compile('<td class="line eng">(?P<sen>.*?)</td>', re.S)
    results = obj.findall(text)
    return results
        
def write(results):
    for i in results:
        i = i.replace('&nbsp;','')
        with open(f'1.txt', 'a') as fo:
            fo.write(f'{i}\n')

marks = ['I','II','III','IV', 'V',
         'VI','VII','VIII','IX','X',
         'XI','XII','XIII','XIV','XV',
         'XVI','XVII','XVIII','XIX','XX',
         'XXI','XXII','XXIII','XXIV','XXV',
         'XXVI','XXVII','XXVIII','XXIX','XXX',
         'XXXI','XXXII','XXXIII','XXXIV','XXXV']
j = 0
for url in urls:
    mark = marks[j]
    with open('1.txt', 'a') as fo:
        fo.write(f'***PARADISE {mark}***\n\n')
    text = get(url, headers)
    results = clean(text)
    write(results)
    with open('1.txt','a') as fo:
        fo.write('\n')
    j += 1

