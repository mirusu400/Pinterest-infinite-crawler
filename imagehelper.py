import requests
import asyncio
from bs4 import BeautifulSoup
from time import sleep

async def download_image(src, dir, i):
    ErrorLevel = 0
    failed = False
    filename = src.split('/')[-1]
    if dir[-1] != "/":
        dir += "/"
    savedir = dir + filename
    src = src.replace("/236x/", "/originals/").replace("/474x/", "/originals/").replace("/736x/", "/originals/")
    while True:
        try:
            request = requests.get(src)
            with open(savedir, 'wb') as file:
                file.write(request.content)
            break
        except Exception as e:
            print(f"{src} : Download fail! Error: {e}")
            ErrorLevel += 1
            sleep(1)
            if (ErrorLevel >= 10):
                failed = True
                print(src + ": Download fail, Skip image")
                break
    return failed


async def download_image_host(plist, dir):
    fail_image = 0
    fts = [asyncio.ensure_future(download_image(plist[i], dir, i)) for i in range(0, len(plist))]
    fail_image = await asyncio.gather(*fts)
    return fail_image
