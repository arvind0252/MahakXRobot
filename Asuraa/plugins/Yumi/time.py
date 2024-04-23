from pyrogram import Client, filters
from datetime import datetime
import pytz
from Asuraa import app


def get_current_time():
    tz = pytz.timezone('Asia/Kolkata')  # Setting the timezone to India (Kolkata)
    current_time = datetime.now(tz)
    return current_time.strftime("%Y-%m-%d %H:%M:%S %Z%z")

@app.on_message(filters.command(["Time"]))
def send_time(client, message):
    time = get_current_time()
    client.send_message(message.chat.id, f"✦ ᴄᴜʀʀʀɴᴛ ᴛɪᴍᴇ ᴏғ ɪɴᴅɪᴀ ⏤͟͟͞͞★\n\n✦ {time}")
    
