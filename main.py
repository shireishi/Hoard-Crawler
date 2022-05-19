import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.elarajade.net"
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}

def Main():
    print("Starting Hoard Crawler.")
    """
    Description: Grabs the information at the provided starting url/file/data and then iterates through the provided resources to find information related
    to said information
    """

    f = requests.get(url, headers=headers) # request the data from the URL
    soup = BeautifulSoup(f.content, 'html.parser') # create the soup object from the collected HTML

    open('index.html', 'w').write(soup.body.prettify())