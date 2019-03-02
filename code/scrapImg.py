import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve


def scrap_images(page_url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/49.0.2623.63 Safari/537.36'}

    req = requests.get(page_url, timeout=5, headers=headers).content

    return BeautifulSoup(req, 'lxml')


def get_images(page_url):
    soup = scrap_images(page_url)

    # making a list of bs4 elements tags
    images = [img for img in soup.find_all('img')]
    print(str(len(images)) + "Images found")

    print("Downloading the images scrapped")

    # compiling the unicode list of image links
    image_links = [link.get('src') for link in images]

    for link in image_links:
        fileName = link.split('/')[-1]
        urlretrieve(link, fileName)

    return image_links


def main():
    page_link = "https://www.imdb.com/movies-in-theaters/?ref_=nv_tp_inth_1"
    scraping = get_images(page_link)

    return scraping


if __name__ == '__main__':
    main()
