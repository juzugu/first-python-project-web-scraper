import requests
from bs4 import BeautifulSoup

urljob = "https://co.computrabajo.com/trabajos-de-python-en-cali"
urlresponse = requests.get(urljob)
soup = BeautifulSoup(urlresponse.text, "html.parser")
job_list = soup.find_all("article", class_="box_offer")
jobscraped_data = []
for jobarticle in job_list:
    jobfinderarticle = jobarticle.find("h2")
    if jobfinderarticle:
        link_tag = jobfinderarticle.find("a")
        company_title = jobarticle.find("p")
        company_title_text = company_title.text.strip()
        if link_tag:
            job_title = link_tag.text.strip()
            job_link = link_tag["href"]