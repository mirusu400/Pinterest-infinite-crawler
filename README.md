# Pinterest-crawler
An pinterest crawler, crawl image by page.

# Requirements
* Python 3.7+
* Selenium, requests, beautifulsoup4, pyyaml
* Chrome + Chromedriver

# Installation
1. Download requirements
```
git clone https://github.com/mirusu400/Pinterest-crawler
cd Pinterest-crawler
pip install -r requirements.txt
```

2. Download chromedriver
You MUST Download [ChromeDriver](https://chromedriver.chromium.org/downloads) as the same version of [Chrome](chrome://settings/help).

And replace it the same directory with `main.py`

3. Set `config.yaml` (Optional)
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