import requests
from bs4 import BeautifulSoup
import sqlite3
con = sqlite3.connect("jobsscrapingjuzugu.db")
cur = con.cursor()
cur.execute(""" CREATE TABLE IF NOT EXISTS jobs_computrabajo (
    title TEXT,
    company TEXT,
    link TEXT UNIQUE
)""")

urlbook = "http://books.toscrape.com"
urlresponse = requests.get(urlbook)
soup = BeautifulSoup(urlresponse.text, "html.parser")
book_list = soup.find_all("article", class_="product_pod")
print(f"Found {len(book_list)} books.")
jobscraped_data = []
for jobarticle in book_list:
    jobfinderarticle = jobarticle.find("h2")
    if jobfinderarticle:
        link_tag = jobfinderarticle.find("a")
        if link_tag:
            company_title = jobarticle.find("p")
            company_title_justtext = "stillnothing"
            if company_title:
                company_title_justtext = company_title.text.strip()
            job_title = link_tag.text.strip()
            job_link = link_tag["href"]
            job_data = {"title" :job_title , "company":company_title_justtext , "link": job_link}
            SQL_insert = "INSERT OR IGNORE INTO jobs_computrabajo (title, company, link) VALUES (?, ?, ?)"
            USER_INFORMATION = (job_data["title"], job_data["company"], job_data["link"])
            cur.execute(SQL_insert,USER_INFORMATION)
con.commit()
con.close()
print("Done right now you can go to the file and you will find the results :D")

