import requests
from bs4 import BeautifulSoup
import json

def get_books():
    req = requests.get('https://www.goodreads.com/list/show/13086.Goodreads_Top_100_Literary_Novels_of_All_Time')
    soup = BeautifulSoup(req.text, 'lxml')
    books_list = soup.findAll('a',{'class':'bookTitle'})

    with open('all_books.txt','w') as f:
        for book in books_list:
            f.write(book['href']+'\n')


def get_book_data():
    with open('all_books.txt') as f:
        book_list = f.readlines()

    res = []
    for i,book in enumerate(book_list):
        print(f"Extracting for book {i+1}")
        req = requests.get('https://www.goodreads.com/'+book)
        soup = BeautifulSoup(req.text, 'lxml')

        data = {
            'title': soup.find('h1', {'id':'bookTitle'}).text.strip(),
            'author' : soup.find('span',{'itemprop':'name'}).text.strip(),
            'ratings' : soup.find('span',{'itemprop':'ratingValue'}).text.strip(),
            'genre' : soup.find('a',{'class':'actionLinkLite bookPageGenreLink'}).text.strip()
        }

        res.append(data)
        
    with open('result.json','w') as f:
        f.write(json.dumps(res))

get_book_data()