import requests
from bs4 import BeautifulSoup
import re
from user_agent import generate_user_agent


class Scrap:
    rel_content = None

    # create a file used to hold the text
    writeFile = open('texting', 'wb')

    def __init__(self, url):
        self.url = url
        self.headers = {'User-Agent': generate_user_agent(device_type="desktop",
                                                          os=('mac', 'linux'))}

    def crawl(self, tag):
        try:

            # requests to get the page content
            r = requests.get(self.url, headers=self.headers, timeout=5)
            r.raise_for_status()
            print(r)
            # extracting the content
            content = r.content
            soup = BeautifulSoup(content, 'html.parser')

            # finding element of webpage
            main_content = soup.find('div', attrs={'class': 'entry-content'})

            # extract the relevant list of president as text
            self.rel_content = main_content.find(tag).text

            # self.writeFile.write(self.rel_content[1:].encode())

            # create a pattern to match names and find all names
            name_pattern = re.compile(r'^([A-Z].+?)(?:,)', flags=re.M)
            names = [name for name in name_pattern.findall(self.rel_content)]
            for name in names:
                self.writeFile.write("\n".encode())
                self.writeFile.write(name.encode())
                self.writeFile.write("      ".encode())

            # make school college and extract colleges
            college_patt = re.compile(r'(?:,|,\s)([A-Z]{1}.*?)(?:\s\(|:|,)')
            colleges = [coll for coll in college_patt.findall(self.rel_content)]
            for colle in colleges:
                self.writeFile.write("\n".encode())
                self.writeFile.write(colle.encode())

            # pattern to match the salaries
            salary_pattern = re.compile(r'\$.+')
            salaries = [sal for sal in salary_pattern.findall(self.rel_content)]

            # Convert salaries to numbers in a list comprehension
            new_salo = [int(''.join(s[1:].split(','))) for s in salaries]
            for sal in new_salo:
                self.writeFile.write("\n".encode())
                self.writeFile.write(str(sal).encode())

            self.writeFile.close()

        except Exception as e:
            print("There was a problem loading the page. {}".format(e))


class CleanText(Scrap):

    def __init__(self, url):
        super().__init__(url)


link = 'http://www.cleveland.com/metro/index.ssf/2017/12/case_western_reserve_university_president_barbara_snyders_base_salary_and_bonus_pay_tops_among_private_colleges_in_ohio.html'
web = CleanText(link)
print(web.crawl('ul'))
