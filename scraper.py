import requests
from bs4 import BeautifulSoup
import sqlite3

con = sqlite3.connect("booksjuzugu.db")
cur = con.cursor()
cur.execute(""" CREATE TABLE IF NOT EXISTS books_scraper (
    book_name TEXT,
    price TEXT 
)""")
urlbook = "http://books.toscrape.com"
urlresponse = requests.get(urlbook)
soup = BeautifulSoup(urlresponse.text, "html.parser")
book_list = soup.find_all("article", class_="product_pod")
print(f"Found {len(book_list)} books.")
for bookarticle in book_list:
    bookfinderarticle = bookarticle.find("h3")
    if bookfinderarticle:
        link_tag = bookfinderarticle.find("a")
        if link_tag:
            book_name_text = link_tag["title"]
            bookprice = bookarticle.find("p", class_="price_color")
            book_price_text = bookprice.text.strip()
            book_data = {"book_name": book_name_text, "price": book_price_text}
            SQL_insert = "INSERT OR IGNORE INTO books_scraper (book_name, price) VALUES (?, ?)"
            USER_INFORMATION = (book_data["book_name"], book_data["price"])
            cur.execute(SQL_insert, USER_INFORMATION)
con.commit()
con.close()
print("Done right now you can go to the file and you will find the results :D")
