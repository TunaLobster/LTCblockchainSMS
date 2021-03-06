#!/usr/bin/python

from json import json
from urllib2 impor urlopen
from requests import get
from smtplib import SMTP
import datetime

# Personal Data
address = ''
phoneService = ''
phoneNumber = ''
gmail_user = ''
gmail_pwd = ''

date = str(datetime.datetime.now().date())

# Pool-x.eu API here
poolData = json.load(urllib2.urlopen('http://pool-x.eu/api?api_key=fdc5f01a60fff78ef4191f6caee221556dd69ad1a58be4594e1457e288f39b33'))
confirmed_rewards = str(float(poolData['confirmed_rewards']))

# Blockchain Explorer API here
receivedRaw = requests.get('http://explorer.litecoin.net/chain/Litecoin/q/getreceivedbyaddress/' + address)
sentRaw = requests.get('http://explorer.litecoin.net/chain/Litecoin/q/getsentbyaddress/' + address)
received = float(receivedRaw.text)
sent = float(sentRaw.text)

walletBalance = str(received - sent)

# Message here
to = phoneNumber+'@messaging.sprintpcs.com'
smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.starttls()
smtpserver.login(gmail_user, gmail_pwd)
header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n'
msg = header + '\n Wallet says: ' + walletBalance + '.\n Mining says: ' + confirmed_rewards + '\n Date: ' + date + '.\n'
print msg
smtpserver.sendmail(gmail_user, to, msg)
print 'Message sent!'
smtpserver.close()
