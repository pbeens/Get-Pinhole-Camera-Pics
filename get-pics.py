"""
This program was written to grab the photos of the cameras used for the 2021 
Worldwide Pinhole Photography Day.

To visit this year's gallery of pinhole pics, visit:

https://pinholeday.org/gallery/2021/

"""

import wget
import time

base_url = 'http://pinholeday.org/gallery/2021/cameras/'
for n in range(0, 400):
    str_n = str(n).zfill(4)  # numbers are 4 digits with leading zeroes
    url = f'{base_url}{str_n}.jpg'
    try:
        # put photos in photos folder; create manually!
        filename = wget.download(url, out='photos')
        print(url)  # warm fuzzy feeling
    except:
        pass
    time.sleep(2)  # not necessary but nice to do
