from bs4 import BeautifulSoup
import requests
import csv

sumber = requests.get('https://coreyms.com/').text

soup = BeautifulSoup(sumber, 'lxml')

filecsv = open('hasil.csv','w')
csv_writer = csv.writer(filecsv)
csv_writer.writerow(['Judul','desc','link'])

for article in soup.find_all('article'):
    judul = article.h2.a.text
    print(judul)

    desc=article.find('div', class_='entry-content').p.text
    print(desc)

    try: 
        #https://www.youtube.com/embed/z0gguhEmWiY?version=3&rel=1&showsearch=0&showinfo=1&iv_load_policy=1&fs=1&hl=en-US&autohide=2&wmode=transparent
        vid_src = article.find('iframe', class_='youtube-player')['src']
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        
        yt_link = f'https://www.youtube.com/watch?v={vid_id}' 
    except Exception as e:
        yt_link = None
    print(yt_link)

    print()

    csv_writer.writerow([judul,desc,yt_link])
filecsv.close()



    

