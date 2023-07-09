from telethon import TelegramClient

api_id =2040
api_hash = 'b18441a1ff607e10a989891a5462e627'
with TelegramClient(
    '6282323894484', 
    api_id, 
    api_hash,
    use_ipv6=True,
    local_addr='2404:8c80:0:1009:ce:1165:1d01:cb9c',
    device_model="OPPO a37",
    system_version='Android 8.8.8',
    app_version='Telegram Linux'
    ) as client:
    client.start()
