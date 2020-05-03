import requests
import re
import os
from urllib import error
 
def main():
    dirPath = "E:\Python\girl_images"
    url = "https://www.dbmeinv.com/?pager_offset="
    i = 1
    j = 0
    while i < 10:
        url = url + str(i)
        try:
            result = requests.get(url, timeout=10)
        except error.HTTPError as e:
            i += 1
            continue
        else:
            text = result.text
            list = re.findall('src="(.*?.jpg)"', text, re.S)
            if len(list) == 0:
                i += 1
                continue
            else:
                for enum in list:
                    image = requests.get(enum, timeout=7)
                    filePath = os.path.join(dirPath, "girl_image_" + str(j) + ".jpg")
                    f = open(filePath, 'wb')
                    f.write(image.content)
                    f.close()
                    j += 1
                i += 1
 
if __name__ == '__main__':
    main()
