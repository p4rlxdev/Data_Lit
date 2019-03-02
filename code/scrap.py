from bs4 import BeautifulSoup
import requests

from user_agent import generate_user_agent

# generate a user agent

# headers = {'User-Agent': generate_user_agent(device_type="desktop",
#                                              os=('mac', 'linux'))}
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/49.0.2623.63 Safari/537.36'}

page_link = "https://www.imdb.com/movies-in-theaters/?ref_=nv_tp_inth_1"

# fetch content from the url
page_response = requests.get(page_link, timeout=5, headers=headers).content

# parse html
page_content = BeautifulSoup(page_response, "html.parser")

print(page_content.prettify())

# extract all html elements where the price is stored
# prices = page_content.find_all(class_='poster shadowed')

# extract all html elements by specifying the tag of the class
prices = page_content.find_all('div', attrs={'class': 'hover-over-image-zero-z-index'})
