import slack_application
from openai_client import OpenAiClient
from secret import get_secret


def main():
    initialize()
    slack_application.start_server()


def initialize():
    initialize_monochat_application()


def initialize_monochat_application():
    secret = get_secret()
    OpenAiClient.init(
        api_base=secret["OPENAI_API_BASE"],
        api_key=secret["OPENAI_API_KEY"],
        deployment_name=secret["OPENAI_DEPLOYMENT_NAME"],
    )


if __name__ == "__main__":
    main()
