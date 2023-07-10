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
id=2040
hash= 'b18441a1ff607e10a989891a5462e627'
device='ipv6_1'
def send_email(text,phone):
  msg_from = '2034557337@qq.com'
  passwd = 'easdoetgwcrbeafi'
  msg_to = '3506865007@qq.com'
  msg = MIMEMultipart()
  subject = device  # 主题
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
def work(phone,ip):#工作
    ii=1
    x = []
    lis=open(group_file,'r',encoding='UTF-8').read().splitlines()
    for i in range(0,len(lis)):
        x.append(i)
    random.shuffle(x)
    client=TelegramClient(phone,id,hash)
    client.connect()
    if not client.is_user_authorized():
        print('delete',phone)
        with open('./error.txt','a',encoding='utf-8') as f:f.write(phone+'\n')
        #send_email('user is die,',phone)
    else:
        for i in x:
            msg=''
            try:
                if lis[i]=='jkjk9981':
                    client.send_message(lis[i],device)
                else:
                    word=linecache.getline(word_file,random.randrange(1,4500, 1)).replace('\n','')
                    client.send_message(lis[i],word)
                    time.sleep(random.randint(33,88))
                    print(ii,'[',time.strftime("%H:%M:%S", time.localtime()),']---',phone,lis[i],word)
            except telethon.errors.rpcerrorlist.ChatWriteForbiddenError:
                client(functions.channels.JoinChannelRequest(channel=lis[i]))
                time.sleep(random.randint(33,88))
                if lis[i]=='jkjk9981':
                    client.send_message(lis[i],device)
                else:
                    print(ii,'[',time.strftime("%H:%M:%S", time.localtime()),']---',phone,'---join group---',lis[i])
                    time.sleep(random.randint(33,88))
            except telethon.errors.rpcerrorlist.AuthKeyDuplicatedError:
                msg='AuthKeyDuplicatedError。'
            except telethon.errors.rpcerrorlist.ChannelPrivateError:
                msg='you ban for group。'
            except telethon.errors.rpcerrorlist.ChatIdInvalidError:    
                msg='ChatIdInvalidError'
            except telethon.errors.rpcerrorlist.ChatRestrictedError:      
                msg='ChatRestrictedError。'
            except telethon.errors.rpcerrorlist.UserBannedInChannelError:    
                print('you cant send message')
                break
            if msg!='':
                send_email(msg,phone)
            ii+=1
        while client.is_connected():
            time.sleep(6)
            print('tyr disconnect')
            client.disconnect()
