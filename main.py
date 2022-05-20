import requests
import lxml
from bs4 import BeautifulSoup
import json

"""
Project postponed due to call request limitations
"""

file_path = "./vaping_cat.jpg"
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}

def yandex_url():
    search_url = 'https://yandex.ru/images/search'
    files = {'upfile': ('blob', open(file_path, 'rb'), 'image/jpeg')}
    params = {'rpt': 'imageview', 'format': 'json', 'request': '{"blocks":[{"block":"b-page_type_search-by-image__link"}]}'}
    response = requests.post(search_url, params=params, files=files)
    query_string = json.loads(response.content)['blocks'][0]['params']['url']
    img_search_url = search_url + '?' + query_string
    return img_search_url

def Main():
    print("Starting Hoard Crawler.")
    """
    Description: Grabs the information at the provided starting url/file/data and then iterates through the provided resources to find information related
    to said information
    """
    url = yandex_url()

    f = requests.get(url, headers=headers) # request the data from the URL
    soup = BeautifulSoup(f.content, 'html.parser') # create the soup object from the collected HTML

    """
    related images div class name : JustifierRowLayout
    Find the a elements within this div
    grab the images using the a href img src
    """
    content = soup.body.find("div", {"class": "JustifierRowLayout"})
    for ind, val in enumerate(content):
        print(ind, val)
        print()
        for a in val.find_all('a', {"class": "Thumb"}):
            #print("ITERATING THROUGH ALL OF THE LINKS FOUND WITHIN THE DIVISION")
            #print(a)
            #print()
            content[ind] = a

    print(content)
    continued_list = list()

    for a in content:
        #print(a.attrs["href"])
        continued_list.append(a.attrs["href"])

    with open('index.html', 'w', encoding='utf-8') as file:
        file.write("")
        file.write(str(continued_list))
