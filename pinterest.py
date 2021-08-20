from selenium import webdriver
from bs4 import BeautifulSoup
import asyncio
from imagehelper import *
from time import sleep
class Pinterest():
    def __init__(self, login, pw):
        self.piclist = []
        options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        # options.add_argument('window-size=1920x1080')
        # options.add_argument("disable-gpu")
        self.driver = webdriver.Chrome('chromedriver', chrome_options=options)
        try:
            self.driver.get("https://pinterest.com/login")
            emailelem = self.driver.find_element_by_id("email")
            passelem = self.driver.find_element_by_id("password")
            emailelem.send_keys(login)
            passelem.send_keys(pw)
            sleep(1)
            self.driver.find_element_by_xpath("//button[@type='submit']").click()
        except Exception as e:
            raise e
        
        
        while True:
            try:
                self.driver.find_element_by_xpath('//*[@id="HeaderContent"]')
                break
            except:
                sleep(1)
                try:
                    self.driver.find_element_by_xpath("//button[@type='submit']").click()
                except:
                    pass
    
    def crawl(self, n=-1, url="https://pinterest.com/", dir="./download"):
        global loop
        fail_image = 0
        if n == -1:
            n = 999999999
        loop = asyncio.get_event_loop()
        
        self.driver.get(url)
        self.driver.implicitly_wait(3)
        for i in range(n):
            timeout = 0
            download_pic_count = len(self.piclist)
            print(f"Scroll down {i} Page, downloaded {download_pic_count} images.")
            height = self.driver.execute_script("return document.body.scrollHeight")
            while True:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(2)
                now_height = self.driver.execute_script("return document.body.scrollHeight")

                # If height changed
                if now_height != height:
                    self.download_image(dir)
                    break
                else:
                    timeout += 1
                    if timeout >= 10:
                        print("It seems we find the end of current page, stop crawling.")
                        print(f"Totally scroll down {i} page, download {download_pic_count} images.")
                        exit()
            sleep(2)
        loop.close
    
    def getdriver(self):
        return self.driver

    def download_image(self, dir="./download"):
        page_pic_list=[]
        req = self.driver.page_source
        soup = BeautifulSoup(req, 'html.parser')
        pics = soup.find_all("img")
        if pics is None:
            return 0
        for pic in pics:
            src = pic.get("src")
            
            # Profile image, skip
            if "75x75_RS" in src:
                continue

            if src not in self.piclist:
                self.piclist.append(src)
                page_pic_list.append(src)
        
        fail_image = sum(loop.run_until_complete(download_image_host(page_pic_list,dir)))
        return fail_image