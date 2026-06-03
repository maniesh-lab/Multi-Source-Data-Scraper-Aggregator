from bs4 import BeautifulSoup
import requests
import pandas as pd


def scrape_books(url):
    page = requests.get(url)                  
    soup = BeautifulSoup(page.content,"lxml")  # .content lets BeautifulSoup handle decoding — avoids encoding issues with £ symbols

    rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

    books = soup.find_all("article", class_="product_pod")

    category = soup.find("h1").text.strip()

    data=[]

    for book in books:
        title = book.h3.a["title"]

        price = book.find("p",class_="price_color").text

        raw_rating = book.find("p",class_="star-rating")["class"][1]
        rating = rating_map[raw_rating]

        data.append({

            "Title":title,
            "Price":price,
            "Rating": rating,
            "Category":category    

            })
        
    return pd.DataFrame(data)


if __name__ == "__main__":
    df = scrape_books("https://books.toscrape.com/catalogue/category/books/classics_6/index.html")
    print(df)