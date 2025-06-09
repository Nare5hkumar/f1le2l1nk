from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, Message
from config import API_ID,API_HASH,BOT_TOKEN

app=Client("my_bot",api_id=API_ID,api_hash=API_HASH,bot_token=BOT_TOKEN)

@app.on_message(filters.private & filters.text)
async def welcome(client,message):
    user_mention = message.from_user.mention
    reply_message= f"Welcome,{user_mention}.\n Welcome to Filetolink Bot"
    join_button = InlineKeyboardButton("ᴊᴏɪɴ ❤️🚀", url="https://t.me/teraaboxxdwnloader")
    replayer= InlineKeyboardButton([[join_button]])

app.run()