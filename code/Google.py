import requests
import webbrowser
import pyperclip
from bs4 import BeautifulSoup
from user_agent import generate_user_agent

headers = {'User-Agent': generate_user_agent(device_type="desktop",
                                             os=('mac', 'linux'))}

address = pyperclip.paste()

print('Googling...')  # display text while downloading the Google page
link = 'http://google.com/search?q=' + address

res = requests.get(link, headers=headers)
res.raise_for_status()

# retrieve top search results links
soup = BeautifulSoup(res.text, 'html.parser')

# open a browser tab for each result
linkElems = soup.select('.r a')

numOPen = min(5, len(linkElems))

for i in range(numOPen):
    print(linkElems[i].get('href'))
    webbrowser.open(linkElems[i].get('href'))

