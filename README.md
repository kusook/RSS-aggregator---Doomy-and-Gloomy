# Doomy and Gloomy
RSS news aggregator with colored terminal output
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Peculiarities
- Multiple RSS feeds support
- Colored terminal output
- HTML tag filtering in description
- Sorting by publication date
- Possibility to set a limit on the news displayed

## Requirements
- Python 3.8+
- Dependencies: `feedparser`, `colorama`, `beautifulsoup4`

## Script with RSS feed URLs
```bash
python doomy.py --urls "https://rss.example.com/feed1" "https://rss.example.com/feed2"
```

## Script with a file with RSS feed URLs
```bash
python doomy.py --file feeds.txt
```

## Setting a limit
```bash
python doomy.py --limit 2 --file feeds.txt
```

## Setting a keyword
```bash
python doomy.py --include "word" --limit 2 --file feeds.txt
```

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
pip install feedparser colorama
```
