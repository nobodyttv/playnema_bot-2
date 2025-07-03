from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext
from scraper import search_movies, get_download_links
from utils import make_film_message
from config import BOT_TOKEN

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("🎬 خوش آمدی به پلینما!

نام فیلم یا سریال رو بفرست:")

async def handle_text(update: Update, context: CallbackContext):
    query = update.message.text
    results = search_movies(query)
    if not results:
        await update.message.reply_text("❌ موردی پیدا نشد.")
        return
    for film in results[:5]:
        buttons = [[
            InlineKeyboardButton("📥 لینک دانلود", url=film['download_link']),
            InlineKeyboardButton("▶️ تماشای آنلاین", url=film['stream_link'])
        ]]
        await update.message.reply_photo(photo=film['poster'], caption=make_film_message(film), reply_markup=InlineKeyboardMarkup(buttons))

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.run_polling()