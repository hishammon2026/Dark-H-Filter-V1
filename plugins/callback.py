from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_callback_query()
async def callback(client, query):
    data = query.data
    
    # ഹെൽപ്പ് ബട്ടൺ
    if data == "help":
        await query.message.edit_caption(
            caption="**സഹായം വേണോ?**\n\n1. എന്നെ നിങ്ങളുടെ ഗ്രൂപ്പിൽ ആഡ് ചെയ്യുക.\n2. ഗ്രൂപ്പിൽ എന്നെ അഡ്മിൻ ആക്കുക.\n3. അതിനുശേഷം സിനിമയുടെ പേര് നൽകുക.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ ബാക്ക്", callback_data="start")]
            ])
        )
        
    # എബൗട്ട് ബട്ടൺ
    elif data == "about":
        await query.message.edit_caption(
            caption="**എബൗട്ട് ഡാർക്ക് ബോട്ട്സ്**\n\nVersion: 1.0\nDeveloper: Hisham\nLanguage: Python\nFramework: Pyrogram",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ ബാക്ക്", callback_data="start")]
            ])
        )

    # സെറ്റിംഗ്സ് ബട്ടൺ (പുതിയത്)
    elif data == "settings":
        await query.answer("സെറ്റിംഗ്സ് ഫീച്ചർ ഉടൻ വരുന്നു...", show_alert=True)

    # സ്റ്റാറ്റസ് ബട്ടൺ (പുതിയത്)
    elif data == "stats":
        await query.answer("ബോട്ട് സ്റ്റാറ്റസ്: വർക്കിംഗ് ✅", show_alert=True)
        
    # മെയിൻ സ്റ്റാർട്ട് പേജിലേക്ക് തിരിച്ചു പോകാൻ
    elif data == "start":
        await query.message.edit_caption(
            caption=f"ഹലോ {query.from_user.mention},\n\nഞാൻ **Dark-H-Filter-V1** ആണ്. സിനിമകൾ തിരയാൻ എന്നെ നിങ്ങളുടെ ഗ്രൂപ്പുകളിൽ ആഡ് ചെയ്യൂ. \n\nDeveloped by **Hisham** ⚡",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("➕ ആഡ് മീ ടു യുവർ ഗ്രൂപ്പ് ➕", url="http://t.me/Mamithafilterrombot?startgroup=true")],
                [InlineKeyboardButton("❓ ഹെൽപ്പ്", callback_data="help"), InlineKeyboardButton("ℹ️ എബൗട്ട്", callback_data="about")],
                [InlineKeyboardButton("⚙️ സെറ്റിംഗ്സ്", callback_data="settings"), InlineKeyboardButton("📊 സ്റ്റാറ്റസ്", callback_data="stats")],
                [InlineKeyboardButton("📢 ചാനൽ", url="https://t.me/bothelpersosupport"), InlineKeyboardButton("👨‍💻 ഡെവലപ്പർ", url="https://t.me/your_username")]
            ])
  )
