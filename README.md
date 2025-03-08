# RSS-aggregator---Doomy-and-Gloomy
RSS news aggregator with colored terminal output
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Peculiarities
- Multiple RSS feeds support
- Colored terminal output
- HTML tag filtering in description
- Sorting by publication date

## Requirements
- Python 3.8+
- Dependencies: `feedparser`, `colorama`, `beautifulsoup4`

## Structure of feeds.txt
```
https://habr.com/ru/rss/articles/
https://thefederalist.com/feed/
https://www.kp.ru/rss/allsections.xml
```

## Installation
```bash
git clone https://github.com/kusook/RSS-aggregator---Doomy-and-Gloomy.git
cd RSS-aggregator---Doomy-and-Gloomy
pip install -r requirements.txt
```
