from selenium import webdriver
from pinterest import Pinterest
import yaml
import os.path


if __name__ == "__main__":
    email = ""
    password = ""
    directory = ""

    # Check chromedriver exists
    if os.path.isfile("./chromedriver.exe"):
        print("No chromedriver found! Please download it")
        exit()

    if os.path.isfile("./config.yaml"):
        with open("./config.yaml", "r") as f:
            config = yaml.load(f)
            email = config["email"]
            password = config["password"]
            directory = config["directory"]
    else: 
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        directory = input("Enter the directory to save the images (Blank if you set default): ")

    pages = input("Enter the number of pages to scrape: ")
    pages = int(pages)
    link = input("Enter the link to scrape (Blank if default; Pinterest main page): ")

    print("Open selenium, download image..")
    p = Pinterest("mirusu400@naver.com", "mi2635121!")
    print("Scroll Down image")
    p.scroll(pages)
    print("Download Images asyncronous")
    p.download_image()
