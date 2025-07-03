import requests
from bs4 import BeautifulSoup

def search_movies(query):
    url = f"https://digimoviez.pics/?s={query.replace(' ', '+')}"
    resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(resp.text, 'html.parser')
    items = soup.select("div.result-item")
    results = []
    for item in items:
        title = item.select_one("h3.result-title").text.strip()
        link = item.select_one("a")["href"]
        poster = item.select_one("img")["src"]
        download_link, stream_link = get_download_links(link)
        results.append({
            "title": title,
            "link": link,
            "poster": poster,
            "download_link": download_link,
            "stream_link": stream_link
        })
    return results

def get_download_links(page_url):
    try:
        r = requests.get(page_url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(r.text, "html.parser")
        download_button = soup.find("a", href=True, text=lambda x: x and ("دانلود" in x or "Download" in x))
        stream_button = soup.find("a", href=True, text=lambda x: x and ("تماشا" in x or "Watch" in x))
        return download_button["href"] if download_button else page_url, stream_button["href"] if stream_button else page_url
    except:
        return page_url, page_url