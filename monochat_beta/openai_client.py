import openai


class OpenAiClient(object):
    @classmethod
    def init(self, api_base: str, api_key: str, deployment_name: str):
        openai.api_type = "azure"
        openai.api_base = api_base
        openai.api_version = "XXXXXXXXXX"  # 「2023-05-15」など
        openai.api_key = api_key
        self._deployment_name = deployment_name

    def request(self, messages: list):
        response = openai.ChatCompletion.create(
            engine=self._deployment_name, messages=messages
        )
        return response["choices"][0]["message"]["content"]
