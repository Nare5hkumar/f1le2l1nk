from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup,Message
from config import API_ID,API_HASH,BOT_TOKEN

app=Client("my_bot",api_id=API_ID,api_hash=API_HASH,bot_token=BOT_TOKEN)

@app.on_message(filters.private & filters.text)
@app.on_message(filters.command("start"))
async def welcome(client,message):
    user_mention = message.from_user.mention
    reply_message= f"Welcome,{user_mention}.\n Welcome to Filetolink Bot"
    join_button = InlineKeyboardButton("ᴊᴏɪɴ ❤️🚀", url="https://t.me/filetolinkks")
    dev_button= InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ ⚡️",url="https://t.me/Nare5hkumar")
    reply_markup= InlineKeyboardMarkup([[join_button,dev_button]])

    await message.reply_text(reply_message,reply_markup=reply_markup)

@app.on_message(filters.document | filters.video | filters.audio | filters.photo)
async def file_handler(client,message:Message):
    file=message.document or message.video or message.audio or message.photo
    file_id=file.file_id
    me=await client.get_me()
    link=f"https://t.me/{me.username}?start={file_id}"
    await message.reply("File uploaded !\n Here's your link:\n `{link}`",disable_web_page_preview=True)

app.run()