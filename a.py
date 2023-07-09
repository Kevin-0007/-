from telethon import TelegramClient

api_id=17349 
api_hash='344583e45741c457fe1862106095a5eb'
with TelegramClient(
    '6283114514550', 
    api_id, 
    api_hash,
    use_ipv6=True,
    local_addr='2404:8c80:0:1009:ce:1165:1d01:cb9c',
    ) as client:
    client.start()
