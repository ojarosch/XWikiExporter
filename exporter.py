import requests
from lxml import html, etree

BASE_URL = "http://localhost:8080"
INDEX=BASE_URL+"/bin/view/Main/Spaces"

page = requests.get(INDEX)

# print(page.text)

tree = html.fromstring(page.text)

links = tree.xpath('//*[@id="xwikicontent"]/ul/li[*]/div/div[1]/a')


def parsePage(url):
    subpage = requests.get(url)
    subpage_tree = html.fromstring(subpage.text)

    HEADING = subpage_tree.xpath('//*[@id="document-title"]/h1/text()')[0]
    # print(HEADING)

    CONTENT = subpage_tree.xpath('//*[@id="xwikicontent"]/pre/text()')[0]
    # print(CONTENT)

    with open("./MKDocs/docs/"+HEADING+".md","a+") as f:
        f.write(CONTENT)



for link in links:
    # print(BASE_URL+link.get('href'))

    QUERY = "?outputSyntax=markdown"
    SUBPAGE_URL = BASE_URL + link.get('href')
    SUBPAGE_URL_QUERY = SUBPAGE_URL[:-1] + QUERY
    try:
        parsePage(SUBPAGE_URL_QUERY)
    except Exception as e:
        print("An exception occurred:", e)
