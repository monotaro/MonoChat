import unittest

from parameterized import parameterized
from slack_application import _strip_heredoc


class StripHeredocTestCase(unittest.TestCase):
    @parameterized.expand(
        [
            ("", ""),
            ("a", "a"),
            ("a", " a "),
            (
                "\n".join(
                    [
                        "(1) MonoChat をメンションすると Azure OpenAI Service (ChatGPT) からのレスポンスが返されます。",
                        "(2) スレッド内でやり取りを繰り返すと、それまでの会話を考慮した回答がおこなわれます。",
                        "(3) スレッド内でもメンションは必要です。",
                        "(4) MonoChat との DM でも利用可能です。この場合はメンション不要です。",
                        "(5) MonoChat からの返信に :del_monochat: でリアクションすると返信を削除できます。",
                    ]
                ),
                """
                    (1) MonoChat をメンションすると Azure OpenAI Service (ChatGPT) からのレスポンスが返されます。
                    (2) スレッド内でやり取りを繰り返すと、それまでの会話を考慮した回答がおこなわれます。
                    (3) スレッド内でもメンションは必要です。
                    (4) MonoChat との DM でも利用可能です。この場合はメンション不要です。
                    (5) MonoChat からの返信に :del_monochat: でリアクションすると返信を削除できます。
                """,
            ),
        ]
    )
    def test_strip_heredoc(self, expected, text):
        actual = _strip_heredoc(text)
        self.assertEqual(expected, actual)
