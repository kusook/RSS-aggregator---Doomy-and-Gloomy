import feedparser
import argparse
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

COLORS = {
    'title': Fore.YELLOW + Style.BRIGHT,
    'source': Fore.CYAN,
    'date': Fore.GREEN,
    'link': Fore.MAGENTA,
    'reset': Style.RESET_ALL
}

def parse_feed(url):
    entries = []
    feed = feedparser.parse(url)
    
    if feed.bozo:
        print(f"{Fore.RED}Ошибка при парсинге {url}: {feed.bozo_exception}")
        return entries

    for entry in feed.entries:
        entry_data = {
            'title': entry.get('title', 'Без заголовка'),
            'link': entry.get('link', '#'),
            'published': entry.get('published', ''),
            'source': feed.feed.get('title', url),
            'description': entry.get('description', '')
        }
        
        if entry_data['published']:
            entry_data['dt'] = datetime(*entry.published_parsed[:6])
        else:
            entry_data['dt'] = datetime.min
            
        entries.append(entry_data)
    
    return entries

def main():
    parser = argparse.ArgumentParser(description="Doomy and Gloomy")
    parser.add_argument('-u', '--urls', nargs='+', help='Список URL RSS-лент')
    parser.add_argument('-f', '--file', help='Файл со списком RSS-лент')
    parser.add_argument('-i', '--include', type=str, help='Фильтр по ключевому слову')
    parser.add_argument('-l', '--limit', type=int, help='Лимит записей на вывод')
    
    print(f"{Fore.RED}·▄▄▄▄              • ▌ ▄ ·.  ▄· ▄▌     ▄▄▄·  ▐ ▄ ·▄▄▄▄       ▄▄ • ▄▄▌              • ▌ ▄ ·.  ▄· ▄▌\n██▪ ██ ▪     ▪     ·██ ▐███▪▐█▪██▌    ▐█ ▀█ •█▌▐███▪ ██     ▐█ ▀ ▪██•  ▪     ▪     ·██ ▐███▪▐█▪██▌\n▐█· ▐█▌ ▄█▀▄  ▄█▀▄ ▐█ ▌▐▌▐█·▐█▌▐█▪    ▄█▀▀█ ▐█▐▐▌▐█· ▐█▌    ▄█ ▀█▄██▪   ▄█▀▄  ▄█▀▄ ▐█ ▌▐▌▐█·▐█▌▐█▪\n██. ██ ▐█▌.▐▌▐█▌.▐▌██ ██▌▐█▌ ▐█▀·.    ▐█ ▪▐▌██▐█▌██. ██     ▐█▄▪▐█▐█▌▐▌▐█▌.▐▌▐█▌.▐▌██ ██▌▐█▌ ▐█▀·.\n▀▀▀▀▀•  ▀█▄▀▪ ▀█▄▀▪▀▀  █▪▀▀▀  ▀ •      ▀  ▀ ▀▀ █▪▀▀▀▀▀•     ·▀▀▀▀ .▀▀▀  ▀█▄▀▪ ▀█▄▀▪▀▀  █▪▀▀▀  ▀ • ")
    
    args = parser.parse_args()
    urls = []
    if args.file:
        with open(args.file, 'r') as f:
            urls = [line.strip() for line in f if line.strip()]
    
    if args.urls:
        urls += args.urls
        
    if not urls:
        print(f"{Fore.RED}Не указаны RSS-ленты! Используйте --urls или --file")
        return
    
    all_entries = []
    for url in urls:
        print(f"{Fore.LIGHTBLACK_EX}Обработка {url}...")
        all_entries += parse_feed(url)
    
    all_entries.sort(key=lambda x: x['dt'], reverse=True)
    
    if args.include:
        all_entries = [e for e in all_entries if args.include.lower() in str(e['title']).lower()]
    
    if args.limit:
        all_entries = all_entries[:args.limit]
        
    if not all_entries:
        if args.include:
            print(f"\n{Fore.RED}Новости, содержащие '{args.include}', не найдены")
        else:
            print("Новости не найдены")
        
    for idx, entry in enumerate(all_entries, 1):
        print(f"\n{Fore.LIGHTWHITE_EX}{idx}. ", end='')
        print(f"{COLORS['source']}[{entry['source']}]", end=' ')
        print(f"{COLORS['title']}{entry['title']}")
        print(f"{COLORS['date']}Опубликовано: {entry['published']}")
        print(f"{COLORS['link']}Ссылка: {entry['link']}")
        print(f"{Fore.LIGHTBLACK_EX}{'-' * 80}")             
if __name__ == "__main__":
    main()
