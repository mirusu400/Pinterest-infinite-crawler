from selenium import webdriver
from bs4 import BeautifulSoup
import asyncio
from imagehelper import *
from time import sleep
class Pinterest():
    def __init__(self, login, pw):
        
        self.driver = webdriver.Chrome()
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
                self.driver.find_element_by_xpath("//button[@type='submit']").click()
                pass
    
    def scroll(self, n, url="https://pinterest.com/"):
        self.driver.get(url)
        self.driver.implicitly_wait(3)
        for i in range(n):
            height = self.driver.execute_script("return document.body.scrollHeight")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            while True:
                now_height = self.driver.execute_script("return document.body.scrollHeight")
                if now_height == height:
                    break
    
    def getdriver(self):
        return self.driver

    def download_image(self, dir="./download"):
        piclist=[]
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
            piclist.append(pic.get("src"))
        fail_image = asyncio.run(download_image_host(piclist, dir))

        return fail_image