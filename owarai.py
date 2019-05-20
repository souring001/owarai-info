from bs4 import BeautifulSoup
import urllib.request as req
import re
import datetime

url = 'https://tv.so-net.ne.jp/s/comedy'

def get_owarai_list():

    # HTMLを取得
    html = req.urlopen(url)

    # HTMLを解析する
    soup = BeautifulSoup(html, 'html.parser')

    # 今日の情報をリストにしたもの
    infoList = []

    # 必要な部分をCSSクエリで取り出す
    utileList = soup.select('div.utileList')
    for li in utileList:
        info = ''

        title = li.select_one('h2 > a').string
        info += title + '\n'

        p = li.select_one('p:nth-of-type(1)')
        schedule = str(p).replace('<p class=\"utileListProperty\">', '').replace('<a href=\"/schedulesBySearch.action?condition.genres[0].id=105000&amp;stationPlatformId=0\">バラエティー</a>', '').replace('</p>', '').replace('\r\n', '').replace('\n', '').replace('          ', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ')
        info += schedule

        date = schedule.split()[0]
        today = datetime.date.today()
        m = today.month
        d = today.day
        str_today = str(m) + '/' + str(d)

        # 今日の情報のみ追加
        if date == str_today:
            infoList.append(info)

    return infoList

# 出力
if __name__ == "__main__":
    owarai_list = get_owarai_list()
    for li in owarai_list:
        if(li == owarai_list[-1]):
            print(li)
        else:
            print(li, '\n\n')
