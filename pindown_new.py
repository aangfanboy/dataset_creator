from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
from threading import Thread, Lock
from queue import Queue
from cv2 import imwrite,imdecode,resize
from urllib.request import urlopen
from numpy import asarray

lock = Lock()
class bingo:
    DONE = False

class ilister:
    ilist = Queue()
    copy_l = []
    leni = 0
    fn = None
    def __init__(self,nmb,fn):
        ilister.fn = fn
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        link = "https://tr.pinterest.com/search/pins/?q=" + str(fn)
        driver.get(link)

        q = 0
        bfn = 0
        samen = 0
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            if(int(len(driver.find_elements_by_tag_name('img'))) >= int(nmb)):
                break

            if(int(len(driver.find_elements_by_tag_name('img'))) <= 5):
                q += 1
                if(q == 50):
                    print(f"Error! I can't find enough image!(Limit is 5, and there is no 5 image in this page! ) ")
                    break

            if(bfn == int(len(driver.find_elements_by_tag_name('img'))) ):
                samen += 1
                if(samen == 500):
                    print(f"There is no enough image, breaking down... I'm gonna download {bfn} image")
                    nmb = bfn
                    break


            bfn = int(len(driver.find_elements_by_tag_name('img')))

            time.sleep(0.5)

        images = driver.find_elements_by_tag_name('img')

        os.makedirs("pins_"+fn,exist_ok=True)

        q = 0
        for image in images:
            if(q >= int(nmb)):
                break
            item = (image.get_attribute('src').replace("236x","564x"),q)
            ilister.copy_l.append(item)
            ilister.ilist.put(item)
            q += 1
        ilister.leni = ilister.ilist.qsize()

        driver.close()

class downloader:
    time1 = None
    q = 0
    def __init__(self,reshapep,shape,pbar,iq = 20):
        self.fn = ilister.fn
        self.reshapep = reshapep
        self.shape = shape
        self.pbar = pbar

        downloader.time1 = time.time()
        downloader.q = 0
        for i in range(5):
            t = Thread(target = self.checker)
            t.daemon = True
            t.start()

        self.fpi = (100 - iq) / int(ilister.ilist.qsize())
        self.proc = iq
        ilister.ilist.join()
        del ilister.ilist
        ilister.ilist = Queue()

    def downloader2(self,image):
        number = image[1]
        image = image[0]
        img = imdecode(asarray(bytearray(urlopen(image).read()), dtype="uint8"), -1)
        if self.reshapep:
            img = resize(img,self.shape)

        imwrite(f"pins_{self.fn}/{self.fn}{number}.jpg",img)
        self.proc += self.fpi
        if self.pbar != None:
            self.pbar.setValue(int(self.proc))

        downloader.q += 1

    def checker(self):
        while True:
            image = ilister.ilist.get()
            self.downloader2(image)
            ilister.ilist.task_done()


def go(keyword,numberl,reshape,shape,pbar = None):
    if pbar != None:
        pbar.setValue(5)
    ilister(numberl,keyword)
    if pbar != None:
        pbar.setValue(20)

    if (ilister.leni <= 5):
        print(f"I can't find any image about {keyword}")
    else:
         downloader(reshape,shape,pbar)

    bingo.DONE = Thread

#go("emma watson",100,True,(200,200))