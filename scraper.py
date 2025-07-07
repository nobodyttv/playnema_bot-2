import requests
from bs4 import BeautifulSoup

def search_movies(query):
    url = f"https://digimoviez.com/?s={query.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    
    posts = soup.select("div.result-item")  # اگر نتیجه نداد، باید div.grid-item یا article.post چک کنیم
    if not posts:
        posts = soup.select("article")  # ساختار جدید سایت احتمالاً اینطوره

    results = []
    for post in posts:
        a_tag = post.find("a", href=True)
        img_tag = post.find("img", class_="wp-post-image")

        if not a_tag or not img_tag:
            continue

        title = img_tag.get("alt", "بدون عنوان")
        link = a_tag["href"]
        poster = img_tag["src"]

        results.append({
            "title": title.strip(),
            "link": link,
            "poster": poster,
            "download_link": link,  # موقتاً لینک خود پست
            "stream_link": link     # چون فعلاً استخراج دقیق لینک دانلود نداریم
        })

    return results
