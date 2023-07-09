from telethon import TelegramClient

api_id=17349 
api_hash='344583e45741c457fe1862106095a5eb'
with TelegramClient(
    '6283114514561', 
    api_id, 
    api_hash,
    device_model="MEIZU 5G",
    system_version=' Android 8.8.8',
    app_version='Telegram Android'
    ) as client:
    client.start()
