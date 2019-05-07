from bs4 import BeautifulSoup
import urllib.request as req
import re

# HTMLを取得
url = "https://tv.so-net.ne.jp/s/comedy"
html = req.urlopen(url)

# HTMLを解析する
soup = BeautifulSoup(html, 'html.parser')

# 必要な部分をCSSクエリで取り出す
list = soup.select("div.utileList")
for li in list:
    title = li.select_one("h2 > a").string
    print(title)
    p = li.select_one("p:nth-of-type(1)")
    schedule = str(p).replace('<p class=\"utileListProperty\">', '').replace('<a href=\"/schedulesBySearch.action?condition.genres[0].id=105000&amp;stationPlatformId=0\">バラエティー</a>', '').replace('</p>', '').replace('\r\n', '').replace('\n', '').replace('          ', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ')
    print(schedule, "\n")
