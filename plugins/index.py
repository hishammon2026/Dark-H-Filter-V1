from pyrogram import Client, filters
from database.mongodb import save_file

@Client.on_message(filters.command("index") & filters.reply)
async def index_files(client, message):
    # റിപ്ലൈ ചെയ്യുന്ന മെസ്സേജിലെ ഫയൽ സേവ് ചെയ്യുന്നു
    file = message.reply_to_message.document or message.reply_to_message.video
    if file:
        data = {
            "file_name": file.file_name,
            "file_id": file.file_id
        }
        await save_file(data)
        await message.reply("ഫയൽ ഡാറ്റാബേസിൽ സേവ് ചെയ്തു! ✅")
