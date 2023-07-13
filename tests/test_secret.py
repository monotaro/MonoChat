import os
import unittest

from parameterized import parameterized
from secret import get_secret_from_environ


class GetSecretFromEnvironTestCase(unittest.TestCase):

    DEFAULT_ENVIRONMENTS = {
        "SLACK_API_TOKEN": "xapp-xxxxx",
        "SLACK_BOT_TOKEN": "xoxb-xxxxx",
        "OPENAI_API_KEY": "xxxxx",
        "OPENAI_API_BASE": "https://xxxxx",
        "OPENAI_DEPLOYMENT_NAME": "xxxxx",
    }

    def setUp(self):
        # 環境変数として必要な全てのキーに対してダミー値を設定する.
        os.environ |= self.DEFAULT_ENVIRONMENTS

    def test_returns_dict_if_all_keys_exists(self):
        """
        全てのキーが環境変数に存在する場合は dict が返される.
        """
        secret = get_secret_from_environ()
        self.assertEqual(self.DEFAULT_ENVIRONMENTS, secret)

    @parameterized.expand(DEFAULT_ENVIRONMENTS.keys())
    def test_returns_none_if_any_key_are_missing(self, key):
        """
        必要なキーが 1 つでも不足している場合は None が返される.
        """
        del os.environ[key]
        secret = get_secret_from_environ()
        self.assertEqual(None, secret)
