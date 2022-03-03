import random
import string

import requests


def get_otp(size=4, chars=string.digits):
    return "".join(random.choice(chars) for _ in range(size))


def send_sms(number, message):
    url = (
        "https://app.indiasms.com/sendsms/bulksms.php?username=learnzytaaced5&password=ru6vh8&sender=LRNZYT&mobile=%s&message=%s&type=TEXT&tempid=1207161977571813541&peid=1201161884621802357"
        % (number, message)
    )
    r = requests.get(url=url)
    data = r.content
    print(data)
    return data
