from slackbot.bot import respond_to, listen_to, default_reply
import os
import requests

LINE_NOTIFY_ACCESS_TOKEN = os.environ["LINE_NOTIFY_ACCESS_TOKEN"]

# チャンネル内の全てのメッセージに応答。これをフックとしてmention_funcが走り、line_botへリクエストを送る。
@listen_to('(.*)')
def mention_func(message):
    # これでslackのユーザ名を取得可能。
    # name = "[" + message.channel._client.users[message._body['user']]['real_name'] + "@ slack]\n"
    # curlだったらこれ
    # -X httpメソッドの指定（今回はPOST）
    # -H "<header info>" ヘッダー情報の付与　\'Authorization: Bearer ${LINE_NOTIFY_ACCESS_TOKEN}\'
    # -F "<key-value data>"フォームからファイルのアップロード。 データの指定(pythonの文字列処理っぽい) \'message={0}{1}\'".format(name,message.body['text'])
    # "curl -X POST https://notify-api.line.me/api/notify -H 'Authorization: Bearer ${LINE_NOTIFY_ACCESS_TOKEN}' -F 'message={0}{1}\'".format(name,message.body['text'])
    url = "https://notify-api.line.me/api/notify"
    headers = {"Authorization: Bearer %s" % LINE_NOTIFY_ACCESS_TOKEN}
    payload = 'message=%s' % (message.body['text'])
    r = requests.post(url, headers=headers, files=dict(payload))

@respond_to('(.*)')
def mention_func(message):
    message.reply('お前口臭くね？')