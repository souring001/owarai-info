from bs4 import BeautifulSoup
import urllib.request as req
import re
import slackweb

# SlackのIncoming Webhook URLを指定
slack_url = 'https://hooks.slack.com/services/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

# HTMLを取得
url = 'https://tv.so-net.ne.jp/s/comedy'
html = req.urlopen(url)

# HTMLを解析する
soup = BeautifulSoup(html, 'html.parser')

# Slackで送信する内容をtextとする
text = ''

# 必要な部分をCSSクエリで取り出す
list = soup.select('div.utileList')
for li in list:
    title = li.select_one('h2 > a').string
    text += title + '\n'
    p = li.select_one('p:nth-of-type(1)')
    schedule = str(p).replace('<p class=\"utileListProperty\">', '').replace('<a href=\"/schedulesBySearch.action?condition.genres[0].id=105000&amp;stationPlatformId=0\">バラエティー</a>', '').replace('</p>', '').replace('\r\n', '').replace('\n', '').replace('          ', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ')
    text += schedule + '\n\n'

slack = slackweb.Slack(url=slack_url)
slack.notify(text=text, username='owarai-info')