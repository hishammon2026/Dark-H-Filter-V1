import logging
import asyncio
from pyrogram import Client
from os import environ

# ലോഗ്സ് എനേബിൾ ചെയ്യുന്നു
logging.basicConfig(level=logging.INFO)

# നിന്റെ ഡീറ്റെയിൽസ്
API_ID = 28390522
API_HASH = "bb6e4438855b6c9ac8d9f0d999a664c4"
BOT_TOKEN = "8775270446:AAFUKrn6oTKO0XF5N20Scz4f4O5fRQ7Eph0"

# നിന്റെ പഴയ ആപ്പിലെ അതേ മംഗോ ലിങ്ക് ഇവിടെ ഓട്ടോമാറ്റിക് ആയി വരും
# ഒരുപക്ഷേ വേരിയബിൾ പേര് 'DATABASE_URI' എന്നാണെങ്കിൽ അത് ഉപയോഗിക്കും
MONGO_URL = environ.get("DATABASE_URI","mongodb+srv://hishammon:hishammon@cluster0.2g7bqyf.mongodb.net/?appName=Cluster0")

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Dark-H-Filter",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="plugins") # plugins ഫോൾഡറിലെ ഫയലുകൾ ലോഡ് ചെയ്യും
        )

    async def start(self):
        await super().start()
        print("Dark-H-Filter-V1 വിജയകരമായി ഓൺ ആയി! 🚀")
        print("ഹിഷാം, നിന്റെ ബോട്ട് ഇപ്പോൾ റെഡിയാണ്.")

    async def stop(self, *args):
        await super().stop()
        print("ബോട്ട് ഓഫ് ആയി..")

if __name__ == "__main__":
    app = Bot()
    app.run()
