# from telegram import Update, InputFile
# from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
# import instaloader
# import os
# import tg_tokens.token_instasaver_tgbot as token
#
# # Bot tokenini BotFather'dan olingan token bilan almashtiring
# TOKEN = token.TOKEN
#
# # Instagram yuklovchi ob'ektni yaratish
# loader = instaloader.Instaloader()
#
#
# # /start buyrug'iga javob beruvchi asinxron funksiya
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await context.bot.send_message(chat_id=update.effective_chat.id, text='Salom! Instagram video linkini yuboring.')
#
#
# # Instagram video linkini qabul qilib, yuklab olish funksiyasi
# async def download_instagram_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     url = update.message.text
#     chat_id = update.effective_chat.id
#
#     try:
#         # Instagram post identifikatori
#         shortcode = url.split('/')[-2]
#
#         # Videoni yuklab olish
#         loader.download_post(instaloader.Post.from_shortcode(loader.context, shortcode), target='downloads')
#
#         # Yuklab olingan faylni topish
#         for filename in os.listdir('downloads'):
#             if filename.endswith('.mp4'):
#                 video_path = os.path.join('downloads', filename)
#
#                 # Videoni yuborish
#                 with open(video_path, 'rb') as video_file:
#                     await context.bot.send_video(chat_id=chat_id, video=InputFile(video_file))
#
#                 # Yuklab olingan fayllarni o'chirish
#                 os.remove(video_path)
#
#         # Yuklab olingan papkani tozalash
#         os.rmdir('downloads')
#     except Exception as e:
#         await context.bot.send_message(chat_id=chat_id, text=f"Xatolik yuz berdi: {str(e)}")
#
#
# # Asosiy funksiya, botni sozlash va ishga tushirish
# def main():
#     # ApplicationBuilder yordamida botni qurish
#     application = ApplicationBuilder().token(TOKEN).build()
#
#     # /start buyrug'i uchun handler qo'shish
#     start_handler = CommandHandler('start', start)
#     application.add_handler(start_handler)
#
#     # Barcha xabarlarni qabul qilib, yuklab olish funksiyasiga o'tkazuvchi handler
#     download_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), download_instagram_video)
#     application.add_handler(download_handler)
#
#     # Botni polling rejimida ishga tushirish
#     application.run_polling()
#
#
# # Skriptning kirish nuqtasi
# if name == 'main':
#     main()