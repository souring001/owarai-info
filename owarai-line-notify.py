import owarai as ow
import requests

# LINE Notify のURLを指定
line_notify_url = 'https://notify-api.line.me/api/notify'
line_notify_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
headers = {"Authorization" : "Bearer "+ line_notify_token}

# LINEで送信する内容をmessageとする
message = '\n'

owarai_list = ow.get_owarai_list()
for li in owarai_list:
    if(li == owarai_list[-1]):
        message += li
    else:
        message += li + '\n\n'

payload = {'message' :  message}

r = requests.post(line_notify_url, headers=headers, params=payload)