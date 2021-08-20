from selenium import webdriver
from pinterest import Pinterest
from sys import exit
import yaml
import os.path


if __name__ == "__main__":
    email = ""
    password = ""
    directory = ""
    currentdir = os.getcwd()
    print(currentdir + "/chromedriver.exe")
    # Check chromedriver exists
    if not os.path.isfile(currentdir + "/chromedriver.exe"):
        print("No chromedriver found! Please download it")
        exit()

    if os.path.isfile(currentdir + "/config.yaml"):
        with open("./config.yaml", "r") as f:
            config = yaml.load(f)
            email = config["email"]
            password = config["password"]
            directory = config["directory"]
    else: 
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        directory = input("Enter the directory to save the images (Blank if you set default): ")
        if directory == "":
            directory = currentdir + "/download"
    pages = input("Enter the number of pages to scrape (Blank if infinity): ")
    if pages == "":
        pages = 999999
    else:
        pages = int(pages)

    link = input("Enter the link to scrape (Blank if default; Pinterest main page): ")
    if link == "":
        link = "https://pinterest.com/"

    print("Open selenium...")
    p = Pinterest(email, password)

    print("Download Image")
    p.crawl(pages, link, directory)
