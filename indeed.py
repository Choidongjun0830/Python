import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
    result = requests.get(URL)

    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div",{"class" : "pagination"})

    links = pagination.find_all('a')
    pages = []
    for link in links[0 : -1]:
        pages.append(int(link.string))
    print(pages)
    max_page = pages[-1]
    return max_page

def extract_indeed_jobs(last_pages):
    for page in range(last_pages):
        result = requests.get(f"{URL}&start={page*LIMIT}")
        print(result.status_code)
    

