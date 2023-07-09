from telethon import TelegramClient

api_id=17349 
api_hash='344583e45741c457fe1862106095a5eb'
with TelegramClient(
    '6283114514579', 
    api_id, 
    api_hash,
    device_model="Samsung 5G",
    system_version=' Android 6.6.6',
    ) as client:
    client.start()
