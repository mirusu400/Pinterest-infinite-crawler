# Pinterest-crawler
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