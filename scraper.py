import requests
from bs4 import BeautifulSoup

def search_movies(query):
    url = f"https://digimoviez.com/?s={query.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')

    # بر اساس ساختار جدید سایت
    posts = soup.select("div.grid-item")

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
            "download_link": link,
            "stream_link": link
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
