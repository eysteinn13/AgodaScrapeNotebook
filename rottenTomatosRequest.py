import requests
from bs4 import BeautifulSoup
import json


if __name__ == '__main__':
    form_url = 'https://www.agoda.com/pages/agoda/default/DestinationSearchResult.aspx?asq' \
               '=bqBMpv5akSjg5TUdHEdKpxb8PNUjN58FGJp12vTy%2BruZ85TbBFquJEM51eUnDR6ZqmaFNwlcQXmK4zE89AlcN%2BfSUlag' \
               '%2BQsDAkNTh5QvCI%2Fynd2NSmA8NW5xDYXyReqxWCbmv4C8VqwFcq4HsanB7zb%2FuZ1bL9ETIhr0f1UK%2BQwBYQF2JOLVmf' \
               '%2Bi1NhwAUOdCpAzJy%2BIPcIhZIlXClDyyr%2BABxpbDmXPyxynowlSe%2FA%3D&city=1618&cid=-207&tick=636402350121' \
               '&pagetypeid=1&origin=SE&tag=&gclid=&aid=130589&userId=d278047e-eb16-458e-b5e4-16056156544c&languageId' \
               '=1&sessionId=gi5mij4x1rzd1pkmuv43bvuf&storefrontId=3&currencyCode=SEK&htmlLanguage=en-us&trafficType' \
               '=User&cultureInfoName=en-US&checkIn=2017-09-14&checkOut=2017-09-15&los=1&rooms=1&adults=2&children=0' \
               '&childages=&priceCur=SEK&hotelReviewScore=5&ckuid=d278047e-eb16-458e-b5e4-16056156544c '
    r = requests.post(form_url)

    soup = BeautifulSoup(r.content, 'html5lib')

    all_hotels = soup.findAll("div", {"class": "hotel-info"})
    print(len(all_hotels))
