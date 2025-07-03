# 🎬 PlaynemaBot

ربات تلگرام فارسی برای جستجو، دانلود و تماشای آنلاین فیلم و سریال از سایت Digimovie.

## نحوه نصب در Render

1. مخزن را در GitHub خودتان Fork کنید.
2. وارد [Render.com](https://render.com) شوید → New Web Service.
3. گزینه‌ها را اینگونه وارد کنید:

- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `python main.py`

4. در بخش Environment Variable:

- **Key:** BOT_TOKEN
- **Value:** توکن ربات از BotFather

5. Deploy کنید. تمام 🎉