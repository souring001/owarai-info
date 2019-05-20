# お笑い番組の情報をスクレイピング
[テレビ王国](https://tv.so-net.ne.jp)のお笑い番組表をスクレイピングします。

今日のお笑い番組の情報を教えてくれます。

* owarai.py (標準出力)
* owarai-slack-notify.py (slackのIncoming Webhook URLに通知)

## 起動方法
### 標準出力
```bash
python3 owarai.py
```

### Slack通知
Rasberry piで `crontab` に以下のように設定することで毎朝6時にSlackの通知が届くようになります。

```
0 6 * * * python3 /home/pi/Document/owarai-info/owarai-slack-notify.py
```

## 実行結果
```
$ python3 owarai.py
ダウンタウンＤＸ★キンプリ永瀬(秘)お笑いライブ＆ロバート秋山の新キャラ炸裂[字][デ]
5/16 (Thu) 22:00 ～ 23:00 (60分) 日テレ(Ch.4)  


アイドルゾーン20時
5/16 (Thu) 23:00 ～ 23:30 (30分) ＴＯＫＹＯ　ＭＸ２(Ch.9)  


アメトーーク!　サンドウィッチマン大好き芸人[字]
5/16 (Thu) 23:20 ～ 0:20 (60分) テレビ朝日(Ch.5)  

```
