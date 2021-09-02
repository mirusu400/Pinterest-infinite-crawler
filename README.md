# Pinterest-infinite-crawler
An **infinite** pinterest crawler, crawl image by page.
![main](https://raw.githubusercontent.com/mirusu400/Pinterest-crawler/main/docs/welcome.gif)

# Requirements
* Python 3.7+
* Selenium, requests, beautifulsoup4, pyyaml
* Chrome + Chromedriver

# Installation
1. Download requirements
```
git clone https://github.com/mirusu400/Pinterest-infinite-crawler.git
cd Pinterest-infinite-crawler
pip install -r requirements.txt
```

2. Download chromedriver

You **MUST** download [ChromeDriver](https://chromedriver.chromium.org/downloads) as the same version of [Chrome](chrome://settings/help).

And replace it the same directory with `main.py`.

3. (Optional) Set `config.yaml`

Copy `.config.yaml` to `config.yaml` and fill your Pinterest's email, password and directorys to save images
```
email: [your email here]
password: [your password here]
directory: ./download
```

# Usage
```
python main.py
```

# Using argument
You can also run crawler by passing argument, here are full document:
```
usage: main.py [-h] [-e EMAIL] [-p PASSWORD] [-d DIRECTORY] [-l LINK] [-g PAGE]

optional arguments:
  -h, --help                            show this help message and exit
  -e EMAIL, --email EMAIL               Your Pinterest account email
  -p PASSWORD, --password PASSWORD      Your Pinterest account password
  -d DIRECTORY, --directory DIRECTORY   Directory you want to download
  -l LINK, --link LINK                  Link of Pinterest which you want to scrape
  -g PAGE, --page PAGE                  Number of pages which you want to scrape
```

**Example:**
> main.py -e mirusu400@naver.com -p [your_password] -d download_image -l https://pinterest.com/ -g 10


# Q & A
### What is `Link to scrape` mean?
You can select **any** pages what you want to scrape in Pinterest, not only main page. Such as:
* [Releative-pins of one pin](https://www.pinterest.co.kr/pin/643240759283703965/)
* [Someone's board](https://www.pinterest.co.kr/eaobrienae/croquies/)
* [A search result](https://www.pinterest.co.kr/search/pins/?q=Github)
* Or anything!

### Does it can download video?
No, you can only download jpg images from this tool. Video is not support for now.

# Contribute
If you find an issue or wants to contribute, please issue or pull request.