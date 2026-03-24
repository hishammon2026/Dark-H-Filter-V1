from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# നിന്റെ മാസ്സ് പോസ്റ്റർ ലിങ്ക്
START_PIC = "https://i.ibb.co/Mx2WPmXV/x.jpg"

@Client.on_message(filters.command("start") & filters.private)
async def start(client, message):
    # സ്റ്റാർട്ട് മെസ്സേജ് ടെക്സ്റ്റ്‌
    text = f"ഹലോ {message.from_user.mention},\n\nഞാൻ **Dark-H-Filter-V1** ആണ്. സിനിമകൾ തിരയാൻ എന്നെ നിങ്ങളുടെ ഗ്രൂപ്പുകളിൽ ആഡ് ചെയ്യൂ. \n\nDeveloped by **Hisham** ⚡"
    
    # നീ ചോദിച്ച ആ 7 ബട്ടണുകൾ ഇവിടെയാണ് സെറ്റ് ചെയ്യുന്നത്
    buttons = [
        [
            InlineKeyboardButton("➕ ആഡ് മീ ടു യുവർ ഗ്രൂപ്പ് ➕", url=f"http://t.me/Mamithafilterrombot?startgroup=true")
        ],
        [
            InlineKeyboardButton("❓ ഹെൽപ്പ്", callback_data="help"),
            InlineKeyboardButton("ℹ️ എബൗട്ട്", callback_data="about")
        ],
        [
            InlineKeyboardButton("⚙️ സെറ്റിംഗ്സ്", callback_data="settings"),
            InlineKeyboardButton("📊 സ്റ്റാറ്റസ്", callback_data="stats")
        ],
        [
            InlineKeyboardButton("📢 ചാനൽ", url="https://t.me/bothelpersosupport"), # നിന്റെ ചാനൽ ലിങ്ക് ഇവിടെ നൽകുക
            InlineKeyboardButton("👨‍💻 ഡെവലപ്പർ", url="https://t.me/hishammon") # നിന്റെ ടെലിഗ്രാം യൂസർനെയിം
        ]
    ]
    
    # പോസ്റ്ററോട് കൂടി മെസ്സേജ് അയക്കുന്നു
    await message.reply_photo(
        photo=START_PIC,
        caption=text,
        reply_markup=InlineKeyboardMarkup(buttons)
)
