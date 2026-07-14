import requests
from bs4 import BeautifulSoup
def goodreads():
    url = "https://www.goodreads.com/quotes"
    headers={ "User-Agent": "Mozilla/5.0(Windows NT 10.0; Win64 ; x64) appleWebKit/537.36 (KHTML ,Like Gecko Chrome/91.0.4472.124 Safari/537.36"}
    response= requests.get(url , headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    a = soup.find_all('div', class_ = "quote")
    detail =[]
    for i in a:
        details_l = i.find('a', class_='quoteDetails')
        text_l = i.find('div', class_='quoteText')
        title_l = i.find('span', class_='authorOrTitle')
        footer_l = i.find('a', class_='right')
        img_l = i.find('img')
        details = details_l.get_text(strip=True) if details_l else ""
        text = text_l.get_text(strip=True) if text_l else ""
        title = title_l.get_text(strip=True) if title_l else ""
        footer_details = footer_l.get_text(strip=True) if footer_l else ""
        image_url = img_l['src'] if img_l and img_l.has_attr('src') else ""
        detail.append({

          "quote": text,

          "author": title,

         

         "image_url": image_url

        })
    return detail