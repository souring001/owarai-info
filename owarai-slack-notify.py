import owarai as ow
import slackweb

# SlackのIncoming Webhook URLを指定
slack_url = 'https://hooks.slack.com/services/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

# Slackで送信する内容をtextとする
text = ''

owarai_list = ow.get_owarai_list()
for li in owarai_list:
    if(li == owarai_list[-1]):
        text += li
    else:
        text += li + '\n\n'

slack = slackweb.Slack(url=slack_url)
slack.notify(text=text, username='owarai-info')
