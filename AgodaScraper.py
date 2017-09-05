from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    url = "https://www.agoda.com/phuket-airport-overnight-hotel/hotel/phuket-th.html?checkin=2017-09-14&los" \
                    "=1&adults=2&rooms=1&cid=-207&searchrequestid=6bf0ef95-c6e5-4548-8baa-77e8577e65bd "

    r = requests.get(url)
    content = r.text

    soup = BeautifulSoup(content)

    print(soup.prettify())






