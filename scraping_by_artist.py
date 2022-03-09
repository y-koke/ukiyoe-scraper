
"""
Sample command:
    python scraping_by_artist.py 広重 --maxnum 1000 --skip 500 --sleep True

"""

import os
import time
import random
import re
import argparse

import requests
from bs4 import BeautifulSoup


def ukiyoe_scraper(name, maxnum, skip, dir, sleep):
    path = dir + name + '/'
    if os.path.exists(path) == False:
        os.mkdir(path)

    for i in range(maxnum) :
        page_url = 'http://www.dh-jac.net/db/nishikie/results-big.php?f9[]=1&f11[]=1&f23[]=' + name \
            + '&f44[]=名所絵&f69[]=%3D&-format=resultsp.htm&-max=' + str(maxnum) \
            + '&singleskip=' + str(skip + i) \
            + '&enter=portal&lang=ja&skip=' + str(skip)

        headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0"}
        r = requests.get(page_url, headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        find = soup.find('img',src=re.compile('.jpg$'))

        if find == None:
            print("File is not found.")
        else:
            pic_url = find.get('src')
            pic_r = requests.get(pic_url)
            filename = str(path)+str(skip + i).zfill(4)+str('.jpeg')
            with open(filename,'wb') as file:
                file.write(pic_r.content)
            print(str(skip + i) + ':' + filename)

        if sleep == True:
            if i % 531 == 0 & i != 0:
                time.sleep(random.randint(40,80))
            else:
                time.sleep(random.randint(3,7))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('name', type = str, help = 'Name of artist.')
    parser.add_argument('-mn', '--maxnum', help = 'Maximum number of scraped images.', type = int, default = 1000)
    parser.add_argument('--save_dir', help = 'Save directry.', default = './output_images/')
    parser.add_argument('--skip', help = 'Number of skipped images.', type = int, default = 0)
    parser.add_argument('--sleep', help = 'Sleep setting.', type = bool, default = False)
    args = parser.parse_args()
    name = args.name
    maxnum = args.maxnum
    save_dir = args.save_dir
    skip = args.skip
    sleep = args.sleep

    if maxnum > 1000:
        for i in range(skip, maxnum, 1000):
            ukiyoe_scraper(name, 1000, i, save_dir, sleep)
    else:
        ukiyoe_scraper(name, maxnum, skip, save_dir, sleep)


if __name__ == '__main__':
    main()