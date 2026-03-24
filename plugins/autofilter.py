from pyrogram import Client, filters
from database.mongodb import search_file

@Client.on_message(filters.group & filters.text)
async def auto_filter(client, message):
    query = message.text
    files = await search_file(query)
    
    if not files:
        return
        
    for file in files:
        await message.reply_cached_media(
            file_id=file['file_id'],
            caption=f"**{file['file_name']}**\n\nShared by Dark Botz"
  )
