from slackbot.bot import respond_to, listen_to, default_reply
import os

LINE_NOTIFY_ACCESS_TOKEN = os.environ["LINE_NOTIFY_ACCESS_TOKEN"]

# メンションされた全てのメッセージ
@respond_to('(.*)')
def mention_func(message, something):
    # これでslackのユーザ名を取得可能。
    name = "[" + message.channel._client.users[message._body['user']]['real_name'] + "@ slack]\n"
    # curlだったらこれ
    # -X httpメソッドの指定（今回はPOST）
    # -H "<header info>" ヘッダー情報の付与　\'Authorization: Bearer ${LINE_NOTIFY_ACCESS_TOKEN}\'
    # -F "<key-value data>" データの指定(pythonの文字列処理っぽい) \'message={0}{1}\'".format(name,message.body['text'])
    # "curl -X POST https://notify-api.line.me/api/notify -H \'Authorization: Bearer ${LINE_NOTIFY_ACCESS_TOKEN}\' -F \'message={0}{1}\'".format(name,message.body['text'])
    headers = {"Authorization: Bearer %s" % LINE_NOTIFY_ACCESS_TOKEN}
    payload = 'message=%s %s' % (name, message.body['text'])
    r = requests.post(url, data=payload, headers=headers)