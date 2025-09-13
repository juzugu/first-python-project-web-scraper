import requests
from bs4 import BeautifulSoup
import sqlite3
urljob = "https://co.computrabajo.com/trabajos-de-python-en-cali"
urlresponse = requests.get(urljob)
soup = BeautifulSoup(urlresponse.text, "html.parser")
job_list = soup.find_all("article", class_="box_offer")
jobscraped_data = []
for jobarticle in job_list:
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
            jobscraped_data.append(job_data)