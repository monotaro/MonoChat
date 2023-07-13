import requests


class SlackClient(object):
    def __init__(self, bot_token: str):
        self._bot_token = bot_token

    def get_replies(self, channel: str, ts: str):
        """
        返信を含めたスレッドメッセージを取得する.
        """
        return requests.get(
            "https://slack.com/api/conversations.replies",
            headers={
                "Authorization": "Bearer {}".format(self._bot_token),
            },
            params={
                "channel": channel,
                "ts": ts,
            },
        ).json()
