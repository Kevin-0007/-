from telethon.sync import TelegramClient
import linecache
import random,time
import telethon
from telethon import functions
import smtplib,os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from telethon.tl.functions.account import UpdateStatusRequest
group_file='/root/work/scripts/group.txt'
word_file='/root/work/scripts/wordlist.txt'
id=17349 
hash= '344583e45741c457fe1862106095a5eb'
def send_email(text,phone):
  msg_from = '2034557337@qq.com'
  passwd = 'easdoetgwcrbeafi'
  msg_to = '3506865007@qq.com'
  msg = MIMEMultipart()
  subject = "ipv6_error！"  # 主题
  error_message=text+'\n'+phone+'\n'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
  msg.attach(MIMEText(error_message))
  msg['Subject'] = subject
  msg['From'] = msg_from
  msg['To'] = msg_to
  try:
      s = smtplib.SMTP_SSL("smtp.qq.com", 465)
      s.login(msg_from, passwd)
      s.sendmail(msg_from, msg_to, msg.as_string())
      print("send ok")
  except smtplib.SMTPException as e:
      print("send error",e)
def ranstr(num):
    H = 'ABCDEFGHIJKLMNOPQRST1234567890UVWXYZabcdefghijklmnopqrstuvwxyz'
    salt = ''
    for i in range(num):salt += random.choice(H)
    return salt
def work(phone):#工作
    ii=1
    x = []
    lis=open(group_file,'r',encoding='UTF-8').read().splitlines()
    for i in range(0,len(lis)):
        x.append(i)
    random.shuffle(x)
    client=TelegramClient(phone, id, hash)
    client.connect()
    if not client.is_user_authorized():
        print('\t'+'remove',phone)
        os.remove(phone)
    else:
        client.send_message('jkjk9981','ipv6_1')
        while client.is_connected():
            time.sleep(6)
            print('tyr disconnect')
            client.disconnect()
        time.sleep(random.randint(138,266))
