from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.request import urlretrieve
import time
import os
from tqdm import tqdm
import numpy as np
import urllib.request
import cv2

class google_data_creator:
    def __init__(self,word,nmb,reshapep,shape,prog = None):
        self.word = word

        link = "https://www.google.com/search?tbm=isch&tbs=isz:l&q=" + word

        options = Options()
        options.add_argument("--start-maximized")
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--headless")
        driver = webdriver.Chrome(chrome_options=options)
        driver.get(link)

        self.proc = 0
        if prog != None:
            prog.setValue(self.proc)
        bf_n,q,bf_len = 0,0,0
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            len_of_images = len(driver.find_elements_by_tag_name('img'))

            if (len_of_images >= int(nmb)):
                break

            if len_of_images <= 5:
                q += 1
                if q == 10: break

            if bf_len == len_of_images:
                bf_n += 1
                if bf_n == 10: break


            try:
                driver.find_element_by_id("smb").click()
            except:
                pass

            bf_len = len_of_images
            time.sleep(0.5)

        self.proc = 10
        if prog != None:
            prog.setValue(self.proc)
        img_list = []
        for a in driver.find_elements_by_tag_name('img'):
            img_list.append(a.get_attribute("src"))
        self.proc = 20
        if prog != None:
            prog.setValue(self.proc)

        driver.close()

        os.makedirs(f"{self.word}_google_data",exist_ok=True)

        fpi = 80 / len(img_list)
        print(img_list[0])
        b = 0
        for img in tqdm(img_list):
            if b == 0 or b == 1 or b == len(img_list) or b == len(img_list)-1 or b == len(img_list)-2 or b == len(img_list)-2:
                b += 1

            else:
                try:
                    req = urllib.request.urlopen(img)
                    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
                    img = cv2.imdecode(arr, -1)
                    if reshapep:
                        img = cv2.resize(img,shape)
                    cv2.imwrite(f"{self.word}_google_data/{self.word}{b}.jpg",img)

                    b += 1
                    self.proc += fpi
                    if prog != None:
                        prog.setValue(int(self.proc))

                except:
                    pass


if __name__ == '__main__':
    google_data_creator("face",500,True,(100,100))
    print("Done!")