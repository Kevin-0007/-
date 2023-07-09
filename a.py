from telethon import TelegramClient

api_id=2496
api_hash='8da85b0d5bfe62527e5b244c209159c3'
with TelegramClient(
    '6283114514550', 
    api_id, 
    api_hash,
    use_ipv6=True,
    local_addr='2404:8c80:0:1009:ce:1165:1d01:cb9c',
    device_model='UFO',
    system_version='UFO8',
    lang_code='zh',
    app_version='Telelgram Desktop 4.6.5 x64'
    ) as client:
    client.start()
